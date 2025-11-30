from datasets import load_from_disk

ds = load_from_disk("/data/ruoyu/dataset/dbpedia_14_saved")

# 假设你已经有 ds = load_dataset("fancyzhx/dbpedia_14")

train_features = ds["train"].features
label_feature = train_features["label"]

# 1. 有多少种 label
num_labels = label_feature.num_classes
print("label 数量：", num_labels)

# 2. 每个 label 的名字
label_names = label_feature.names
print("label 名称列表：", label_names)
