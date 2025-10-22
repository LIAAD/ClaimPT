
import os
#pip install dkpro-cassis


from cassis import *
# starts with CURATION_USER****.json"
import pandas as pd
import spacy

nlp = spacy.load("pt_core_news_sm")



def getData(pathname=os.path.join("claimPT_data", "curation")):
    annotations = []
    for x in os.scandir(pathname):
        for f in os.scandir(x.path):
            if f.is_file() and f.name.endswith(".json"):
                with open(f.path, 'rb') as json_file:
                    cas = load_cas_from_json(json_file)
                    annotations.append(cas)
    return annotations


def convertData(annotations):
    dataset=list()
    id=1
    for doc in annotations:
        anns_docs = list()
        for span in doc.select_all():
            if(span.type.name=="custom.Span" and span.label in ["Claim","Non-claim"]):

                temp=dict()
                temp["label"]=span.label
                temp["begin"]=span.begin
                temp["end"]=span.end

                anns_docs.append(temp)

        doc_metadata=dict()
        doc_metadata["doc_id"] = id
        doc_metadata["text"]=doc.sofas[0]._sofaString
        doc_metadata["annotations"]=anns_docs
        dataset.append(doc_metadata)
        id=id+1
    return dataset


annotations=getData()
js=convertData(annotations)

def convertDatatoPandas(annotations):
    dataset=list()
    id=1
    for doc in annotations:
        for span in doc.select_all():
            if (span.type.name == "custom.Span" and span.label in ["Claim", "Non-claim"]):

                temp=dict()
                temp["label"]=span.label
                temp["begin"]=span.begin
                temp["end"]=span.end

                temp["doc_id"] = id
                temp["text"] = doc.sofas[0]._sofaString
                temp["token_text"]=temp["text"][temp["begin"]:temp["end"]]

                dataset.append(temp)
        id=id+1

    df=pd.DataFrame.from_dict(dataset)
    return df


#df=convertDatatoPandas(annotations)
