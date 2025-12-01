from datasets import load_from_disk

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
 
    return store

dataset_path = "/data/ruoyu/dataset/dbpedia_14_saved"
each_num = 10
rand_seed = 42

test_set = fetch_data(dataset_path, each_num, rand_seed)
print(test_set)