from transformers import AutoTokenizer, AutoModelForCausalLM

model_id = "Qwen/Qwen3-4B"
cache_dir = "/data/ruoyu/model"  # 改成你想要的文件夹

tokenizer = AutoTokenizer.from_pretrained(
    model_id,
    cache_dir=cache_dir,
)

model = AutoModelForCausalLM.from_pretrained(
    model_id,
    cache_dir=cache_dir,
)
