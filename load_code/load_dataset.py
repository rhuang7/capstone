from datasets import load_dataset, VerificationMode

# 先正常加载（或带 cache_dir 都行）
# ds = load_dataset("fancyzhx/dbpedia_14")
# ds = load_dataset("cais/mmlu", "abstract_algebra")
ds = load_dataset("openai/openai_humaneval", verification_mode=VerificationMode.ALL_CHECKS,)

# 保存到指定文件夹
save_path = "/data/ruoyu/dataset/openai_humaneval"
ds.save_to_disk(save_path)
