# awesome-icd-coding
This is not an official awesome list, just my personal collection of public available resources about auto ICD medical coding. <br>
A similar awesome list of medical coding can be found here: [acadTags/Awesome-medical-coding-NLP](https://github.com/acadTags/Awesome-medical-coding-NLP) <br>
The above list is more complete for now. <br>
But I try to categorize the articles by the ICD versions and include other related resources.

## Contents
- [Related Topics](#related-topics)
- [Resource](#resource)
- [Papers](#papers)
    - [ICD-9](#icd-9)
    - [ICD-10](#icd-10)
    - [Hybird](#hybrid)


## Related Topics
List some related topics found on [awesome](https://github.com/sindresorhus/awesome).
- [acadTags/Awesome-medical-coding-NLP](https://github.com/acadTags/Awesome-medical-coding-NLP)
- [OHNLP/awesome-clinical-nlp](https://github.com/OHNLP/awesome-clinical-nlp)
- [keon/awesome-nlp](https://github.com/keon/awesome-nlp)
- [Jiakui/awesome-bert](https://github.com/Jiakui/awesome-bert)
- [cedrickchee/awesome-bert-nlp](https://github.com/cedrickchee/awesome-bert-nlp)
- [caufieldjh/awesome-bioie](https://github.com/caufieldjh/awesome-bioie)
- [harpribot/awesome-information-retrieval](https://github.com/harpribot/awesome-information-retrieval)
- [Separius/awesome-sentence-embedding](https://github.com/Separius/awesome-sentence-embedding)


## Resource
- [Paper-with-codes](https://paperswithcode.com/) leaderboard of [MIMIC-III benchmarks of ICD-9 medical coding](https://paperswithcode.com/sota/medical-code-prediction-on-mimic-iii).
- [icd10data: Free 2022 ICD-10-CM/PCS Medical Coding Reference](https://www.icd10data.com/)


## Papers

### ICD-9
- [Larkey, L. S., & Croft, W. B. (1995). Automatic assignment of icd9 codes to discharge summaries. Technical report, University of Massachusetts at Amherst, Amherst, MA.](http://ciir.cs.umass.edu/pubfiles/coding.html)
- [Larkey, L. S., & Croft, W. B. (1996, August). Combining classifiers in text categorization. In Proceedings of the 19th annual international ACM SIGIR conference on Research and development in information retrieval (pp. 289-297).](https://dl.acm.org/doi/pdf/10.1145/243199.243276)
- [Crammer, K., Dredze, M., Ganchev, K., Talukdar, P., & Carroll, S. (2007, June). Automatic code assignment to medical text. In Biological, translational, and clinical language processing (pp. 129-136).](https://aclanthology.org/W07-1017.pdf)
- [Pestian, J., Brew, C., Matykiewicz, P., Hovermale, D. J., Johnson, N., Cohen, K. B., & Duch, W. (2007, June). A shared task involving multi-label classification of clinical free text. In Biological, translational, and clinical language processing (pp. 97-104).](https://aclanthology.org/W07-1013.pdf)
- [Farkas, R., & Szarvas, G. (2008, April). Automatic construction of rule-based ICD-9-CM coding systems. In BMC bioinformatics (Vol. 9, No. 3, pp. 1-9). BioMed Central. ](https://link.springer.com/article/10.1186/1471-2105-9-S3-S10)
- [Perotte, A., Pivovarov, R., Natarajan, K., Weiskopf, N., Wood, F., Elhadad, N., 2013. Diagnosis code assignment: models and evaluation metrics. Journal of the American Medical Informatics Association 21, 231–237. URL: https://doi.org/10.1136/amiajnl-2013-002159, doi:10.1136/amiajnl-2013-002159.](https://doi.org/10.1136/amiajnl-2013-002159,)
- [Berndorfer, S., & Henriksson, A. (2017). Automated diagnosis coding with combined text representations. Stud Health Technol Inform, 235, 201-205.](pdf/SHTI235-0201.pdf)
- [Baumel, T., Nassour-Kassis, J., Cohen, R., Elhadad, M., & Elhadad, N. (2018, June). Multi-label classification of patient notes: case study on ICD code assignment. In Workshops at the thirty-second AAAI conference on artificial intelligence.](pdf/16881-75991-1-PB.pdf)
- [Mullenbach, J., Wiegreffe, S., Duke, J., Sun, J., & Eisenstein, J. (2018). Explainable prediction of medical codes from clinical text. arXiv preprint arXiv:1802.05695.](https://arxiv.org/pdf/1802.05695.pdf)
- [Rios, A., & Kavuluru, R. (2018, October). Few-shot and zero-shot multi-label learning for structured label spaces. In Proceedings of the Conference on Empirical Methods in Natural Language Processing. Conference on Empirical Methods in Natural Language Processing (Vol. 2018, p. 3132). NIH Public Access.](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6375489/)
- [Gao, S., Alawad, M., Young, M. T., Gounley, J., Schaefferkoetter, N., Yoon, H. J., ... & Tourassi, G. (2021). Limitations of transformers on clinical text classification. IEEE journal of biomedical and health informatics, 25(9), 3596-3607.](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=9364676)
- [Dong, H., Suárez-Paniagua, V., Whiteley, W., & Wu, H. (2021). Explainable automated coding of clinical notes using hierarchical label-wise attention networks and label embedding initialisation. Journal of biomedical informatics, 116, 103728.](https://www.sciencedirect.com/science/article/pii/S1532046421000575)
- [Kim, B. H., & Ganapathi, V. (2021, October). Read, attend, and code: Pushing the limits of medical codes prediction from clinical notes by machines. In Machine Learning for Healthcare Conference (pp. 196-208). PMLR.](https://proceedings.mlr.press/v149/kim21a/kim21a.pdf)


### ICD-10
- [Subotin, M., & Davis, A. (2014, June). A system for predicting ICD-10-PCS codes from electronic health records. In Proceedings of BioNLP 2014 (pp. 59-67).](https://aclanthology.org/W14-3409.pdf)
    - ICD-10-PCS, dataset unknown, micro-averaged Fscore is 0.485
- [Lin, C., Hsu, C. J., Lou, Y. S., Yeh, S. J., Lee, C. C., Su, S. L., & Chen, H. C. (2017). Artificial intelligence learning semantics via external resources for classifying diagnosis codes in discharge notes. Journal of medical Internet research, 19(11), e8344.](https://www.jmir.org/2017/11/e380/)
    - ICD-10-CM, use 103,390 discharge notes covering patients hospitalized from 2015 to 2017 in the Tri-Service General Hospital in Taipei, mean AUC 0.9696; mean F-measure 0.9086
- [Kaur, R., University., W.S., 2018. A comparative analysis of selected set of natural language processing (NLP) and machine learning (ML) algorithms for clinical coding using clinical classification standards. URL: http://hdl.handle.net/1959.7/uws:49614. a thesis presented to Western Sydney University, School of Computing, Engineering and Mathematics, in fulfilment of the requirements for the degree of Master of Research](https://researchdirect.westernsydney.edu.au/islandora/object/uws:49614/)
- [Zhang, Z., Liu, J., & Razavian, N. (2020). BERT-XML: Large scale automated ICD coding using BERT pretraining. arXiv preprint arXiv:2006.03685.](https://arxiv.org/pdf/2006.03685.pdf)
    - ICD-10-CM


### Hybrid
Papers with multiple ICD versions.
- [Xiao, C., Choi, E., & Sun, J. (2018). Opportunities and challenges in developing deep learning models using electronic health records data: a systematic review. Journal of the American Medical Informatics Association, 25(10), 1419-1428.](https://academic.oup.com/jamia/article/25/10/1419/5035024)
- [Kaur, R., Ginige, J. A., & Obst, O. (2021). A Systematic Literature Review of Automated ICD Coding and Classification Systems using Discharge Summaries. arXiv preprint arXiv:2107.10652.](https://arxiv.org/pdf/2107.10652.pdf)




