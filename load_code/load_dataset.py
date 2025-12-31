from datasets import load_dataset, VerificationMode

# 先正常加载（或带 cache_dir 都行）
# ds = load_dataset("fancyzhx/dbpedia_14")
# ds = load_dataset("cais/mmlu", "abstract_algebra")
# ds = load_dataset("openai/openai_humaneval", verification_mode=VerificationMode.ALL_CHECKS,)
# ds = load_dataset("Muennighoff/mbpp", "full")
ds = load_dataset("chansung/verifiable-coding-problems-python")

# 保存到指定文件夹
save_path = "/data/ruoyu/dataset/verifiable_coding_problems_python"
ds.save_to_disk(save_path)
