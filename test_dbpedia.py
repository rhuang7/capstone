from datasets import load_from_disk
import json
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from tqdm import tqdm
import time
import utils

def fetch_data(dataset_path, each_num, rand_seed):
    ds = load_from_disk(dataset_path)

    train_features = ds["train"].features
    label_feature = train_features["label"]

    num_labels = label_feature.num_classes

    label_names = label_feature.names

    train_ds = ds["train"]
    store = []
    for label_id in range(num_labels):
        label_name = label_names[label_id]

        subset = train_ds.filter(lambda e: e["label"] == label_id)
        subset = subset.shuffle(seed=rand_seed)
        samples = subset.select(range(each_num))
        for i, ex in enumerate(samples):
            store.append([label_name, ex["content"]])
 
    return store, label_names

def prompt_gen(labels, content):
    prompt = """You are a text classification model.

[TASK]
Given a piece of English text, choose exactly one label from the following:
"""
    for label in labels:
        prompt += '- '+ label + '\n'
        
    prompt += """
[OUTPUT REQUIREMENTS]
1. You MUST output ONLY ONE JSON object. Do NOT output any explanation, comments, natural language, or Markdown.
2. JSON format (keys and structure must be identical):
{
  "label": "chosen_label",
  "confidence": 0.xx
}
3. "confidence" is your subjective confidence score between 0 and 1 (two decimal places).
4. Do NOT output anything before or after the JSON object.
    
[TEXT]
"""
    prompt += content
    
    prompt += """
Now output the JSON object only:
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
        prompt = prompt_gen(labels, pair[1])
        
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
        
        count_store.append([pred_label, pair[0], pair[1]])
        # print("predict label:", pred_label)
        
        # print("original label:", pair[0])
        # if pair[0] not in raw_resp:
        #     print(pair[0])
        
    return count_store

if __name__ == '__main__':
    dataset_path = "/data/ruoyu/dataset/dbpedia_14_saved"
    each_num = 10
    rand_seed = 42

    test_set, labels = fetch_data(dataset_path, each_num, rand_seed)

    model_id = "Qwen/Qwen3-4B"
    cache_dir = "/data/ruoyu/model"

    calcu_result = do_test(test_set, labels, model_id, cache_dir)
    print("the perdiction accuracy: ", utils.get_accuracy(calcu_result))
    utils.print_accuracy_by_category(calcu_result)
