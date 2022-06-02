# A Systematic Literature Review of Automated ICD Coding and Classification Systems using Discharge Summaries
> [Kaur, R., Ginige, J. A., & Obst, O. (2021). A Systematic Literature Review of Automated ICD Coding and Classification Systems using Discharge Summaries. arXiv preprint arXiv:2107.10652. ](https://arxiv.org/pdf/2107.10652.pdf)

Select 38 studies with high quality assessment scores from 4 different academic databases (PubMed, ScienceDirect, ACM, ACL), from 2013 to 2020.
    - ACM: Association for Computing Machinery Digital Library
    - ACL: Association for Computational Linguistics Anthology

Briefly introduce the history of medical coding from ICD-1(1900) to ICD-11(2018). <br>
Use a lot of tables to list the techiques and methods used by these works. <br>

## Motivations
ICD Coding:
- With the transition from ICD-9 to ICD-10 in 1992, the number of codes increased from 3,882 to approximately 70,000.

Unconstructed Text:
- Huang et al.[36] show that more than 80% of health record data is in an unstructured form which acts as a barrier in an automated clinical decision making process.
- Unstructured text contains a lot of valuable information but lacks common structural frameworks and may contain errors, such as spelling errors, grammatical errors, and semantic ambiguities, which further increases the complexity of data processing and analysis [87]

Difficulties:
1. Idiosyncrasies of medical language
2. Scarcity of electronic health records
3. Label-space problem
4. Requirement of large amount of training data

To reduce coding errors and cost, there is a need for an automated clinical coding system, commonly referred to as computer-assisted coding system that will overcome the manual coding challenges and assist human coders to assign correct clinical codes more quickly and accurately.


## Datasets
Note that some works use multiple datasets rather than one. MIMIC-III is the most used dataset among these studies.
1. MIMIC-II (ICD-9-CM) (14/38)
2. MIMIC-III (ICD-9-CM) (27/38)
3. University of Kentucky medical centre (ICD-9-CM) (2/38)
4. Australian hospital medical records (ICD-10-AM and ACHI) (2/38)
5. Taiwan hospital discharge notes (ICD-10-CM) (1/38)
6. NYU Langone Hospital (ICD-10) (1/38)
7. Other anonymous healthcare providers (ICD-10-CM, ICD-10-PCS) (2/38)

### Pre-processing
There are several pre-processing techniques, the most 3 popular are Tokenization, Removal of stop words/non-alphabetical, and Lowercase conversion. <br>
There are 4 of the works provide no information about pre-processing, so I change the denominator to 34.
1. Tokenization (19/34)
2. Lowercase conversion (13/34) 
3. Removal of stop words (14/34)
4. Sentence segmentation (5/34)
5. Removal of non-alphabetical characters (13/34)
6. Abbreviation expansion (2/34)
7. Spell error detection and correction (3/34)
8. Negation detection (3/34)
9. Stemming (2/34)
10. Lemmatization (2/34)
11. Parsing (1/34)
12. Part-of-speech tagging (1/34)
13. Named Entity Recognition (2/34)
14. Normalization (2/34)
15. Regular expression matching (1/34)
16. Built dictionary or vocabulary (2/34)
17. Truncation of documents (9/34)
18. Replace to UNK (5/34)
19. Removal of de-identified or confidential information (2/34)
20. Extracted diagnosis descriptions (1/34)
21. Removing non-matching terms (1/34)
22. No information (4/38)

## Methods
The methods each work used is decomposed into 2 parts, feature extraction and machine learing models. <br>
Basically all works use more than one methods.



### Feature Extraion
1. TF-IDF (14/38)
2. N-grams (2/38)
3. BoW (8/38)
4. Doc2Vec ()
5. Word2Vec 
6. GloVe
7. BERT 
8. knowlege grpah
9. other word embeddings


## Future Directions
1. Data source
2. Crowd-sourcing platform
3. National adoption and coding rules
4. Reducing the complex problem
5. Transfer learning approach
6. Active learning and reinforcement learning

