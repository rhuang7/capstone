from datasets import load_from_disk
import json
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from tqdm import tqdm
import time
import utils
import random

def fetch_data(dataset_path):
    ds = load_from_disk(dataset_path)

    train_features = ds["train"].features
    label_feature = train_features["label"]

    num_labels = label_feature.num_classes
    label_names = label_feature.names
    
    store = {name: [] for name in label_names}
   
    for t in tqdm(range(len(ds["train"])), desc="Reading dataset"):
        ex = ds["train"][t]
        label_name = label_names[ex["label"]]  
        store[label_name].append(ex["content"])
            
    return store

def set_testset(mydatasets, n, repeat):
    out_dict = {}
    labels = mydatasets.keys()
    for t in tqdm(range(len(labels)), desc="Generating testsets"):
        label = list(labels)[t]
        rand_ori_content = random.sample(mydatasets[label], repeat)
        out_dict[label] = []
        for content in rand_ori_content:
            temp_list = [content]
            sample_confusion_plan = utils.rand_nonneg_ints_sum(n-1, len(labels)-1)
            confusion_labels = [v for v in labels if v != label]
            for i in range(0, len(sample_confusion_plan)):
                if sample_confusion_plan[i] != 0:
                    temp_list.extend(random.sample(mydatasets[confusion_labels[i]], sample_confusion_plan[i]))
            random.shuffle(temp_list)
            with_true =[content]
            with_true.extend(temp_list)
            out_dict[label].append(with_true)
            
    return out_dict

def prompt_gen(label, content):
    the_prompt = """You are a sentence selection model.

[TASK]
You are given:
- A target label: "{LABEL}"
- N candidate sentences.

Choose EXACTLY ONE sentence that best matches the target label.
If none match well, still choose the closest one.

[CRITERIA]
- Prefer the sentence that is most clearly and specifically about the target label.
- Avoid sentences that are only loosely related.

[OUTPUT REQUIREMENTS]
1. You MUST output ONLY ONE JSON object. Do NOT output any explanation, comments, natural language, or Markdown.
2. JSON format (keys and structure must be identical):
{
  "index": k,
  "confidence": 0.xx
}
3. "index" is an integer from 1 to N (1-based).
4. "confidence" is your subjective confidence between 0 and 1 with two decimals.
5. Do NOT output anything before or after the JSON object.

[LABEL]
"""
    the_prompt += label + '\n' + """
[SENTENCES] 
"""
    for i in range(0, len(content)):
        the_prompt += str(i+1) + '.' + ' ' + content[i] + '\n'
    the_prompt += "\nNow output the JSON object only:\n"
    
    return the_prompt

def do_test(testset, model_id, cache_dir):

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
        prompt = prompt_gen(pair[0], pair[2:])
        
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
        pred_index = obj["index"]
        
        count_store.append([pair[2:][pred_index - 1], pair[1], pair[0]])
        # print("predict label:", pred_label)
        
        # print("original label:", pair[0])
        # if pair[0] not in raw_resp:
        #     print(pair[0])
        
    return count_store
    


