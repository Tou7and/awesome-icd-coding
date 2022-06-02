import pandas as pd

def show_datasets():
    """
    1. MIMIC-II (ICD-9-CM) (14/38)
    2. MIMIC-III (ICD-9-CM) (27/38)
    3. University of Kentucky medical centre (ICD-9-CM) (2/38)
    4. Australian hospital medical records (ICD-10-AM and ACHI) (2/38)
    5. Taiwan hospital discharge notes (ICD-10-CM) (1/38)
    6. NYU Langone Hospital (ICD-10) (1/38)
    7. Other anonymous healthcare providers (ICD-10-CM, ICD-10-PCS) (2/38)
    """
    table = [
        {"name": "MIMIC-II", "type": "ICD-9-CM", "counts": 14},
        {"name": "MIMIC-III", "type": "ICD-9-CM", "counts": 27},
        {"name": "University of Kentucky medical centre", "type": "ICD-9-CM", "counts": 2},
        {"name": "Australian hospital medical records", "type": "ICD-10-AM and ACHI", "counts": 2},
        {"name": "Taiwan hospital discharge notes", "type": "ICD-10-CM", "counts": 1},
        {"name": "NYU Langone Hospital", "type": "ICD-10", "counts": 1},
        {"name": "Other anonymous providers", "type": "ICD-10-CM, ICD-10-PCS", "counts": 1},
    ]
    df = pd.DataFrame(table)
    df2 = df.sort_values(by=['counts'], ascending=False)
    print(df2.to_markdown(index=None))
    return 


def show_preprocess():
    """
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
    """
    table = [
        {"name": "Tokenization", "counts": 19},
        {"name": "Lowercase conversion", "counts": 13},
        {"name": "Removal of stop words", "counts": 14},
        {"name": "Sentence segmentation", "counts": 5},
        {"name": "Removal of non-alphabetical characters", "counts": 13},
        {"name": "Abbreviation expansion", "counts": 2},
        {"name": "Spell error detection and correction", "counts": 3},
        {"name": "Negation detection", "counts": 3},
        {"name": "Stemming", "counts": 2},
        {"name": "Lemmatization", "counts": 2},
        {"name": "Parsing", "counts": 1},
        {"name": "Part-of-speech tagging", "counts": 1},
        {"name": "Named Entity Recognition", "counts": 2},
        {"name": "Regular expression matching", "counts": 1},
        {"name": "Built dictionary or vocabulary", "counts": 2},
        {"name": "Truncation of documents", "counts": 9},
        {"name": "Replace to UNK", "counts": 5},
        {"name": "Removal of de-identified or confidential information", "counts": 2},
        {"name": "Extracted diagnosis descriptions", "counts": 1},
        {"name": "Removing non-matching terms", "counts": 1},
    ]
    df = pd.DataFrame(table)
    df2 = df.sort_values(by=['counts'], ascending=False)
    print(df2.to_markdown(index=None))


if __name__ == "__main__":
    # show_datasets()
    show_preprocess()

