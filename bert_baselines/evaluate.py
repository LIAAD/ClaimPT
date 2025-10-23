#read list of json files in ./nuno


import json
import os
from cassis import * 

path = "./curation"
files = []
file_names= []
for sub_folder in os.listdir(path):
    if sub_folder.startswith('input'):
        for file in os.listdir(os.path.join(path, sub_folder)):
            if file.endswith('.json'):
                with open(os.path.join(path, sub_folder,file), 'rb') as f:
                    cas = load_cas_from_json(f)
                    files.append(cas)
                file_names.append(sub_folder)


f_train_split = open("train_split.txt")
f_test_split = open("test_split.txt")

train_split = f_train_split.read().split('\n')[:-1]
test_split = f_test_split.read().split('\n')[:-1]

print(train_split)

#get train and test files
train_files = []
test_files = []
train_file_names = []
test_file_names = []
for i, file_name in enumerate(file_names):
    if file_name in train_split:
        train_files.append(files[i])
        train_file_names.append(file_name)
    elif file_name in test_split:
        test_files.append(files[i])
        test_file_names.append(file_name)


#load nuno files
path = "./nuno/gemini-2.5-flash-lite-FS"
files_nuno = []
file_names_nuno = []
for file_names in os.listdir(path):
    if file_names.endswith('.json'):
        with open(os.path.join(path,file_names), 'rb') as f:
            data = json.load(f)
            files_nuno.append(data)
        file_names_nuno.append(file_names)


annotations_nuno = []
mapping_lalbel = {"claim": "Claim", "non-claim": "Non-claim"}
for file in files_nuno:
    tmp = []
    for ann in file["extractions"]:
        if ann["char_interval"]:
            tmp.append((ann["char_interval"]["start_pos"], ann["char_interval"]["end_pos"], mapping_lalbel[ann["extraction_class"]]))
    annotations_nuno.append(tmp)

#gold annotations
gold_annotations = []
for cas in test_files:
    # create list of annotations for each file in test_files
    annotations = cas.select("custom.Span")
    labels = [(e.begin, e.end, e.label) for e in annotations if e.label and (e.label == "Claim" or e.label == "Non-claim")]
    gold_annotations.append(labels)
    
    

#compute span f1
def compute_claim_f1(pred_docs, gold_docs):
    print(len(pred_docs), len(gold_docs))
    assert len(pred_docs) == len(gold_docs), "Number of documents must match"

    labels = ["Claim", "Non-claim"]
    counts = {label: {"tp": 0, "fp": 0, "fn": 0} for label in labels}

    for pred_spans, gold_spans in zip(pred_docs, gold_docs):
        pred_set = set(pred_spans)
        gold_set = set(gold_spans)

        for label in labels:
            #filter by label
            pred_label = {ann for ann in pred_set if ann[2] == label}
            gold_label = {ann for ann in gold_set if ann[2] == label}

            counts[label]["tp"] += len(pred_label & gold_label)
            counts[label]["fp"] += len(pred_label - gold_label)
            counts[label]["fn"] += len(gold_label - pred_label)

    results = {}
    total_tp = total_fp = total_fn = 0

    for label in labels:
        tp, fp, fn = counts[label]["tp"], counts[label]["fp"], counts[label]["fn"]
        precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
        recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
        f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0.0
        results[label] = {"precision": precision, "recall": recall, "f1": f1}
        total_tp += tp
        total_fp += fp
        total_fn += fn

    # Micro-average across both labels
    micro_p = total_tp / (total_tp + total_fp) if (total_tp + total_fp) > 0 else 0.0
    micro_r = total_tp / (total_tp + total_fn) if (total_tp + total_fn) > 0 else 0.0
    micro_f1 = 2 * micro_p * micro_r / (micro_p + micro_r) if (micro_p + micro_r) > 0 else 0.0

    results["micro_avg"] = {"precision": micro_p, "recall": micro_r, "f1": micro_f1}
    return results
compute_claim_f1(annotations_nuno, gold_annotations)