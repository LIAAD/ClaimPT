# ClaimPT
Repository for the paper ClaimPT: A Portuguese Dataset of Annotated Claims in News Articles

## ClaimPT Dataset Sample

The folder dataset_sample contains a sample of the ClaimPT dataset. It is organized to provide both the original news articles and their corresponding annotation files in accessible formats.

The news_articles folder includes the individual text files for each news article in the dataset. Each file name corresponds to a unique article identifier, allowing you to easily match it with the related annotations.

The annotations.jsonl file contains the dataset’s annotations in JSON Lines (JSONL) format, where each line represents one annotation entry in JSON structure. Each annotation includes a "document" key that specifies the ID of the associated news article, linking the annotations directly to the files in the news_articles folder.

For improved readability, the annotations.pretty.json file provides the same annotation data as the JSONL file, but formatted with indentation and line breaks. This makes it easier to visually inspect and understand the dataset structure without additional parsing tools.
