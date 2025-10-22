# ClaimPT
Repository for the paper ClaimPT: A Portuguese Dataset of Annotated Claims in News Articles

[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC--BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)

## 🧩 Overview

We introduce ClaimPT, a dataset of European Portuguese news articles annotated for factual claims, comprising 1,308 articles and 6,875 individual annotations. Unlike most existing resources based on social media or parliamentary transcripts, ClaimPT focuses on journalistic content, collected through a partnership with LUSA, the Portuguese News Agency. To ensure annotation quality, two trained annotators labeled each article, with a curator validating all annotations according to a newly proposed scheme. We also provide baseline models for claim detection, establishing initial benchmarks and enabling future NLP and IR applications. By releasing ClaimPT, we aim to advance research on low-resource fact-checking and enhance understanding of misinformation in news media.


## 📂 Repository Structure
``` 
├── dataset_sample/
│ ├── annotations.jsonl
│ ├── annotations.pretty.json
│ ├── news_articles/
│ │ └── *.txt
│
├── ClaimPT_Annotation_Guidelines.pdf
│
├── generative_baselines/ 
│ ├── generative_baseline.ipynb
|
├── LICENSE
└── README.md
```

## ClaimPT Dataset Sample

The folder dataset_sample contains a sample of the ClaimPT dataset. It is organized to provide both the original news articles and their corresponding annotation files in accessible formats.

The news_articles folder includes the individual text files for each news article in the dataset. Each file name corresponds to a unique article identifier, allowing you to easily match it with the related annotations.

The annotations.jsonl file contains the dataset’s annotations in JSON Lines (JSONL) format, where each line represents one annotation entry in JSON structure. Each annotation includes a "document" key that specifies the ID of the associated news article, linking the annotations directly to the files in the news_articles folder.

For improved readability, the annotations.pretty.json file provides the same annotation data as the JSONL file, but formatted with indentation and line breaks. This makes it easier to visually inspect and understand the dataset structure without additional parsing tools.

## 📘 How to Use

### Requirements
```bash
python >= 3.9
transformers >= 4.30
torch >= 2.0
pandas
scikit-learn
```

## Citation
```
@inproceedings{tba
TO BE ADDED
}
```

## 📬 Contact

Ricardo Campos — ricardo.campos at ubi.pt
