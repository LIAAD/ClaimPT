
# ClaimPT: A Portuguese Dataset of Annotated Claims in News Articles

##  Overview
We introduce **ClaimPT**, a dataset of European Portuguese news articles annotated for **factual claims**, comprising **1,308 articles** and **6,875 individual annotations**. Unlike most existing resources based on social media or parliamentary transcripts, ClaimPT focuses on journalistic content, collected through a partnership with **LUSA, the Portuguese News Agency**. To ensure annotation quality, two trained annotators labeled each article, with a curator validating all annotations according to a newly proposed scheme. We also provide **baseline models** for claim detection, establishing initial benchmarks and enabling future NLP and IR applications. By releasing ClaimPT, we aim to advance research on low-resource **fact-checking** and enhance understanding of misinformation in news media.


## Repository Structure
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
---

## Corpus Statistics

| Property | Description |
|-----------|--------------|
| **Total Documents** | 1,308 |
| **Average Length** | 542.8 words per document |
| **Total Claims** | 463 |
| **Total Non-Claims** | 4,393 |




---

## Data Format

The **ClaimPT** dataset is provided in **JSONL** format, where each line corresponds to an annotated span.  

| Field | Description |
|--------|-------------|
| `document` | News article filename |
| `publication_time` | Date of the news publication |
| `claim` | Boolean indicating whether the annotation is a claim (`true`) or non-claim (`false`) |
| `begin_character` | Begin character offset of the annotated text span |
| `end_character` | End character offset of the annotated text span |
| `text_segment` | Text segment corresponding to the annotated span |
| `claim_topic` | Topic of the news article (e.g., politics, environment, health) |
| `claim_span` | Object containing `text`, `begin`, and `end` positions of the claim span |
| `claim_object` | Text and character offsets of the claim’s object (if applicable) |
| `claimer` | Text and offsets of the entity making the claim |
| `Time` | Temporal expression associated with the claim (if annotated) |

---

### Example (JSON excerpt)

```json
[
  {
    "document": "input_part008.txt",
    "publication_time": "04 dez 2023",
    "claim": true,
    "begin_character": 501,
    "end_character": 685,
    "text_segment": "foi convidado para aderir não pelo lado monárquico, no qual, aliás, não insistiam muito, mas por se empenhar, acima de tudo, na defesa do ambiente e na preservação da qualidade de vida",
    "claim_topic": "politics",
    "claim_span": {
      "text": "foi convidado para aderir não pelo lado monárquico, no qual, aliás, não insistiam muito, mas por se empenhar, acima de tudo, na defesa do ambiente e na preservação da qualidade de vida",
      "begin": 501,
      "end": 685
    },
    "claim_object": {
      "text": "por se empenhar, acima de tudo, na defesa do ambiente",
      "begin": 594,
      "end": 647
    },
    "claimer": {
      "text": "Pinto Balsemão",
      "begin": 438,
      "end": 452
    },
    "Time": ""
  }
]
````

---

## Annotation Guidelines

Detailed annotation instructions, including procedures, quality-control measures, and schema definitions, are available in the document:

📄 [ClaimPT Annotation Manual (PDF)](https://github.com/LIAAD/ClaimPT/blob/main/ClaimPT%20Annotation%20Manual.pdf)

This manual describes:

* The annotation process and methodology
* The annotation scheme and entity structures
* The definition of a claim
* Metadata and label taxonomy
* Examples and boundary cases

Researchers interested in replicating the annotation or training models should refer to this guide.

---

## Dataset Access

### Sample Dataset

A sample subset (20 annotated articles) is included in the repository under the dataset_sample/ directory

### Full Dataset

The complete dataset (1,308 articles) is protected by a **Data Use Agreement** and will be made available through the following DOI once the research paper is published:

🔗 **[https://rdm.inesctec.pt/dataset/cs-2025-008](https://rdm.inesctec.pt/dataset/cs-2025-008)**

Please visit the DOI link for access details and usage terms.

---

## Dataset Split

The dataset is divided into **train** and **test** subsets, maintaining the same Claim:Non-Claim ratio (1:9.48) as the full set.

| Split     | Size | # News Articles |
| --------- | ---- | --------------- | 
| **Train** | 80%  | 1,046           | 
| **Test**  | 20%  | 262             | 

---

## Baselines

Claim detection is modeled as a **span classification task**:
Given a text *t*, the model predicts a set of triples *(b, e, c)*, where *b* and *e* indicate the start and end of a span, and *c ∈ {Claim, Non-Claim}* denotes the class.

#### Encoder-based Model

* **Model:** BERTimbau (Portuguese BERT)
* **Approach:** Fine-tuned for token classification
* **Model link:** N/A

#### Generative LLM-based Model

* **Model:** Gemini 2.5 Pro
* **Method:** Few-shot structured extraction
* **Prompt used:**

```
"Identifique claims (alegações factuais) e non-claims no texto, de acordo com as seguintes regras:
Claim:
Definição: Uma claim é uma afirmação factual, verificável e de interesse público, expressa em discurso direto (entre aspas), atribuída a alguém que não seja o jornalista.
Segmento textual: Extraia apenas frases declarativas completas, com sentido próprio, sem incluir aspas ou ponto final.
Critérios de inclusão:
Claims geralmente aparecem ligadas a verbos de relato (afirmar, frisar, referir, disse, explicou).
Cada claim deve ser extraída individualmente, mesmo que esteja numa mesma citação.
Critérios de exclusão:
Não extrair frases incompletas ou sem sentido.
Não extrair frases informativas, de senso comum ou sem relevância pública.
Não extrair frases sobre possibilidades futuras ou hipóteses.
Non-Claim:
Definição: Frases subjetivas (opiniões, crenças, juízos pessoais), especulativas ou com referência a acontecimentos futuros não comprováveis.
Regras:
Devem ser frases declarativas completas em discurso direto (entre aspas).
Não incluir aspas nem ponto final.
Exclusão: frases narrativas do jornalista ou sem sentido completo.
Instruções Gerais:
Analise cada frase individualmente dentro de citações diretas.
Numa mesma citação podem existir claims e non-claims; classifique cada frase separadamente."
```
```


---

## License

**License:** [CC-BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/deed.en)

This work is licensed under the **Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License**.

**You are free to:**

* Share — copy and redistribute the material in any medium or format

**Under the following terms:**

* **Attribution** — Credit must be given to the authors
* **NonCommercial** — The material may not be used for commercial purposes
* **NoDerivatives** — Modified versions may not be distributed

---

## Citation

If you use this dataset, please cite:

```bibtex
@dataset{claimpt2025,
  author       = {Ricardo Campos and Raquel Sequeira and Sara Nerea and Inês Cantante and Diogo Folques and Luís Filipe Cunha and João Canavilhas and António Branco and Alípio Jorge and Sérgio Nunes and Nuno Guimarães and Purificação Silvano},
  title        = {ClaimPT: A Portuguese Dataset of Annotated Claims in News Articles},
  year         = {2025},
  doi          = {https://rdm.inesctec.pt/dataset/cs-2025-008},
  institution  = {INESC TEC}
}
```

---

## Credits and Acknowledgements

This dataset was developed by **[INESC TEC – Institute for Systems and Computer Engineering, Technology and Science](https://www.inesctec.pt)**, specifically by the **[NLP Group](https://nlp.inesctec.pt/)** within the **[LIAAD – Laboratory of Artificial Intelligence and Decision Support](https://www.inesctec.pt/pt/centros/LIAAD)** research center.

### Affiliated Institutions

* [University of Beira Interior (UBI)](https://www.ubi.pt/en/)
* [University of Porto (UP)](https://www.up.pt/portal/en/)

### Acknowledgements

*To be completed with funding and grant numbers.*

---

## Contact

For support, questions, or collaboration inquiries:

📧 [ricardo.campos@ubi.pt](mailto:ricardo.campos@ubi.pt)

For bug reports or feature requests:
👉 Open an issue at the [GitHub repository](https://github.com/LIAAD/ClaimPT/issues)

```
```
