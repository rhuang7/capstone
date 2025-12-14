from datasets import load_from_disk
import json
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from tqdm import tqdm
import time
import utils

def fetch_data(dataset_path, each_num, rand_seed):
    ds = load_from_disk(dataset_path)

    train_features = ds["test"].features
    label_feature = train_features["answer"]

    num_labels = label_feature.num_classes

    label_names = label_feature.names
    
    train_ds = ds["test"]
    store = []
    for label_id in range(num_labels):
        label_name = label_names[label_id]

        subset = train_ds.filter(lambda e: e["answer"] == label_id)
        subset = subset.shuffle(seed=rand_seed)
        samples = subset.select(range(each_num))
        for i, ex in enumerate(samples):
            store.append([label_name, ex["question"], ex["choices"]])
 
    return store, label_names

def prompt_gen(labels, content, options):
    prompt = """You are an expert exam-taker.
For each multiple-choice question, you must pick exactly ONE best answer from A, B, C, or D.

You must respond ONLY with a JSON object:
{
  "answer": "A" | "B" | "C" | "D",
  "confidence": <a number between 0 and 1>
}

"confidence" is your estimated probability that your chosen answer is correct.
Do not output anything other than the JSON.
"""
    prompt += 'Question: {' + content + '}' + '\n\nChoices:\n'
        
    for op_loc in range(len(labels)):
        prompt += str(labels[op_loc]) + '. {' + options[op_loc] + '}\n'
    
    prompt += """
Give your final answer as JSON now.
"""
    
    return prompt

def do_test(testset, labels, model_id, cache_dir):

    tokenizer = AutoTokenizer.from_pretrained(
        model_id,
        cache_dir=cache_dir,
    )

    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        cache_dir=cache_dir,
        dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
        device_map="auto" if torch.cuda.is_available() else None,
    )
    
    count_store = []
    total_len = len(testset)
    for i in tqdm(range(total_len), desc="processing"): 
        pair = testset[i]
        prompt = prompt_gen(labels, pair[1], pair[2])
        
        messages = [
            {"role": "user", "content": prompt},
        ]

        inputs = tokenizer.apply_chat_template(
            messages,
            add_generation_prompt=True,
            tokenize=True,
            return_dict=True,
            return_tensors="pt",
            enable_thinking=False
        ).to(model.device)

        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_new_tokens=64,  
                do_sample=False,     
                top_p=1.0,
                temperature=0.0,
            )

        generated_tokens = outputs[0][inputs["input_ids"].shape[-1]:]
        raw_resp = tokenizer.decode(generated_tokens, skip_special_tokens=True).strip()

        obj = json.loads(raw_resp)
        pred_label = obj["label"]
        
        count_store.append([pred_label, pair[0], pair[1], pair[2]])
        # print("predict label:", raw_resp)
        
        # print("original label:", pair[0])
        # if pair[0] not in raw_resp:
        #     print(pair[0])
        
    return 




dataset_path = "/data/ruoyu/dataset/mmlu_saved"
each_num = 5
rand_seed = 42
model_id = "Qwen/Qwen3-4B"
cache_dir = "/data/ruoyu/model"

test_set, labels = fetch_data(dataset_path, each_num, rand_seed)
calcu_result = do_test(test_set, labels, model_id, cache_dir)

print("the perdiction accuracy: ", utils.get_accuracy(calcu_result))
utils.print_accuracy_by_category(calcu_result)