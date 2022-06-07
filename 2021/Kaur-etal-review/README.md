# A Systematic Literature Review of Automated ICD Coding and Classification Systems using Discharge Summaries
> [Kaur, R., Ginige, J. A., & Obst, O. (2021). A Systematic Literature Review of Automated ICD Coding and Classification Systems using Discharge Summaries. arXiv preprint arXiv:2107.10652. ](https://arxiv.org/pdf/2107.10652.pdf)

This work selected 38 studies with high quality assessment scores from 4 different academic databases <br>
(PubMed, ScienceDirect, ACM, ACL), ranging from 2013 to 2020.
> ACM: Association for Computing Machinery Digital Library <br>
> ACL: Association for Computational Linguistics Anthology <br>

It briefly introduce the history of medical coding from ICD-1(1900) to ICD-11(2018) in introdution. <br>
It provides some nice tables to list the methods of by these works. <br>

## Motivations
ICD Coding: <br>
With the transition from ICD-9 to ICD-10 in 1992, <br> the number of codes increased from 3,882 to approximately 70,000. 

Unconstructed Text: <br>
Over 80% of health record data is in an unstructured form which acts as a barrier in an automated clinical decision making. (Huang et al.[36])<br>
Unstructured text contains a lot of valuable information but may spelling errors, grammatical errors, and semantic ambiguities, which increases the complexity of data processing and analysis [87]

Difficulties:
1. Idiosyncrasies of medical language
2. Scarcity of electronic health records
3. Label-space problem
4. Requirement of large amount of training data

To reduce coding errors and cost, there is a need for an automated clinical coding system that overcome the manual coding challenges and assist human coders to assign correct clinical codes more quickly and accurately. <br>
(This kind of system are also refered to as computer-assisted coding system)

## Datasets
Some works use multiple datasets rather than one. <br>
MIMIC-III is the most used dataset among these studies. <br>

| name                                  | type                  |   counts |
|:--------------------------------------|:----------------------|---------:|
| MIMIC-III                             | ICD-9-CM              |       27 |
| MIMIC-II                              | ICD-9-CM              |       14 |
| University of Kentucky medical centre | ICD-9-CM              |        2 |
| Australian hospital medical records   | ICD-10-AM and ACHI    |        2 |
| Taiwan hospital discharge notes       | ICD-10-CM             |        1 |
| NYU Langone Hospital                  | ICD-10                |        1 |
| Other anonymous providers             | ICD-10-CM, ICD-10-PCS |        1 |


### Pre-processing
There are several pre-processing techniques. Top 3 popular are Tokenization, Removal of stop words, and Lowercase conversion. <br>
There are 4 of the works provide no information about pre-processing, so the denominator is actual 34. <br>

| name                                                 |   counts |
|:-----------------------------------------------------|---------:|
| Tokenization                                         |       19 |
| Removal of stop words                                |       14 |
| Removal of non-alphabetical characters               |       13 |
| Lowercase conversion                                 |       13 |
| Truncation of documents                              |        9 |
| Replace to UNK                                       |        5 |
| Sentence segmentation                                |        5 |
| Spell error detection and correction                 |        3 |
| Negation detection                                   |        3 |
| Abbreviation expansion                               |        2 |
| Stemming                                             |        2 |
| Lemmatization                                        |        2 |
| Named Entity Recognition                             |        2 |
| Removal of de-identified or confidential information |        2 |
| Built dictionary or vocabulary                       |        2 |
| Extracted diagnosis descriptions                     |        1 |
| Parsing                                              |        1 |
| Regular expression matching                          |        1 |
| Part-of-speech tagging                               |        1 |
| Removing non-matching terms                          |        1 |


## Methods
The methods each work used is decomposed into 2 parts, feature extraction and machine learing models. <br>
Basically all works use two or more methods, since it is necessary to compare with others.

### Feature Extraion
TF-IDF, BOW and CBOW are commonly used within these works. <br>

| name            |   counts |
|:----------------|---------:|
| TF-IDF          |       14 |
| BOW             |        8 |
| CBOW            |        7 |
| skip-gram       |        3 |
| GloVe           |        3 |
| N-grams         |        2 |
| Doc2Vec         |        1 |
| cui2vec         |        1 |
| FastText        |        1 |
| EHR-BERT        |        1 |
| Knowledge graph |        1 |


### Proposed Methods
CNN and SVM are proposed more frequently within these works. <br>

| proposed methods                                                     |   counts |
|:---------------------------------------------------------------------|---------:|
| CNN                                                                  |        8 |
| SVM                                                                  |        4 |
| LSTM                                                                 |        3 |
| Flat SVM                                                             |        2 |
| LR                                                                   |        2 |
| DR-CAML                                                              |        2 |
| GRU                                                                  |        2 |
| Hierarchy-based SVM                                                  |        1 |
| Two-level hierarchical classification                                |        1 |
| MNB                                                                  |        1 |
| C-MemNN                                                              |        1 |
| A-MemNN                                                              |        1 |
| Hierarchical SVM                                                     |        1 |
| RNN-GRU                                                              |        1 |
| CBOW                                                                 |        1 |
| HA-GRU                                                               |        1 |
| CAML                                                                 |        1 |
| EnHAN                                                                |        1 |
| Tree-of-sequences LSTM                                               |        1 |
| ZACNN                                                                |        1 |
| ZAGCNN                                                               |        1 |
| NB                                                                   |        1 |
| Decision Tree                                                        |        1 |
| kNN                                                                  |        1 |
| RF                                                                   |        1 |
| AdaBoost                                                             |        1 |
| MLP                                                                  |        1 |
| Deep transfer learning using multi-scale CNN and Batch normalisation |        1 |
| Binary relevance                                                     |        1 |
| Label Power set                                                      |        1 |
| ML-kNN                                                               |        1 |
| MSATT-KG                                                             |        1 |
| Multi-view CNN                                                       |        1 |
| DeepLabeler (CNN and D2V)                                            |        1 |
| FastText                                                             |        1 |
| Text-CNN                                                             |        1 |
| ML-Net                                                               |        1 |
| ML-CNN                                                               |        1 |
| ML-HAN                                                               |        1 |
| HyperCore                                                            |        1 |
| BiLSTMs                                                              |        1 |
| LAAT                                                                 |        1 |
| JointLAAT                                                            |        1 |
| ZAGRNN                                                               |        1 |
| UNITE                                                                |        1 |
| ANN                                                                  |        1 |
| Bi-LSTM                                                              |        1 |
| MultiResCNN                                                          |        1 |
| G-Coder                                                              |        1 |
| Bi-GRU                                                               |        1 |
| MVC-LDA                                                              |        1 |
| MVC-RLDA                                                             |        1 |
| DCAN                                                                 |        1 |
| HAN                                                                  |        1 |
| AttentionXML (BERT-XML)                                              |        1 |

### Compared Methods
CAML and SVM are compared more frequently within these works. <br>

| compared methods                                  |   counts |
|:--------------------------------------------------|---------:|
| CAML                                              |        8 |
| DR-CAML                                           |        7 |
| SVM                                               |        6 |
| LR                                                |        6 |
| HA-GRU                                            |        5 |
| Bi-GRU                                            |        4 |
| Flat SVM                                          |        4 |
| C-MemNN                                           |        4 |
| CNN                                               |        3 |
| LEAM                                              |        3 |
| C-LSTM-Att                                        |        3 |
| MultiResCNN                                       |        3 |
| Hierarchy SVM                                     |        2 |
| Attentive LSTM                                    |        2 |
| Logistic regression                               |        2 |
| BR                                                |        1 |
| copy transformation                               |        1 |
| ECC                                               |        1 |
| End-to-End Memory Network                         |        1 |
| KV-MemNNs                                         |        1 |
| RF                                                |        1 |
| GBM                                               |        1 |
| HAN                                               |        1 |
| HierNet                                           |        1 |
| HybridNet                                         |        1 |
| BranchNet                                         |        1 |
| LET                                               |        1 |
| ACNN                                              |        1 |
| Match-CNN                                         |        1 |
| Selected Feature                                  |        1 |
| Text-CNN                                          |        1 |
| MVC-LDA                                           |        1 |
| MVC-RLDA                                          |        1 |
| Random Forest                                     |        1 |
| Feed-forward neural network                       |        1 |
| hierarchy-based SVM                               |        1 |
| LR+L2R+NERC                                       |        1 |
| averaging ensemble CNNs without transfer learning |        1 |
| Binary relevance SVM                              |        1 |
| MT-CNN-net                                        |        1 |
| C-MemNN                                           |        1 |
| C-LSTM-ATT                                        |        1 |
| DeepLabeler                                       |        1 |
| C-MemNN                                           |        1 |
| MSATT-KG                                          |        1 |
| ZAGCNN                                            |        1 |
| Topic modeling                                    |        1 |
| MLP                                               |        1 |
| Flat SVM                                          |        1 |
| CNN [45]                                          |        1 |
| C-MemNN [67]                                      |        1 |
| Multi-head Attention                              |        1 |
| BERT                                              |        1 |
| BioBERT                                           |        1 |
| ClinicalBERT                                      |        1 |


## Future Directions
1. Data source
2. Crowd-sourcing platform
3. National adoption and coding rules
4. Reducing the complex problem
5. Transfer learning approach
6. Active learning and reinforcement learning


