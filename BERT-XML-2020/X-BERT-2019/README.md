# X-bert: extreme multi-label text classification with using bidirectional encoder representations from transformers
> Chang, W. C., Yu, H. F., Zhong, K., Yang, Y., & Dhillon, I. (2019). X-bert: extreme multi-label text classification with using bidirectional encoder representations from transformers. arXiv preprint arXiv:1905.02331.

An implementation based on pytorch and allenlp provided by the authors can be found [here](https://github.com/guoqunabc/X-BERT).

X-BERT, a scalable BERT finetuning model for XMC problem. <br>
XMC is Extreme multi-label text classification, where the output label-set is extremely large. <br>
X-BERT consists of 3 conponets:
- Semantic Label Indexing: semantically indexing the labels
- Deep Neural Matching: matching the label indices using deep learning
- Ensemble Ranking: ranking the labels from the retrieved indices and taking an ensemble of different configurations

The conponents of X-BERT is partly inspired by IR. <br>
IR is information retrieval, where the goal is to find relevant documents from an extremely large set for a given query. <br>
Steps of IR: <br>
1. indexing: build an efficient data structure to index the documents
2. matching: find the document index that this document instance belongs to
3. ranking: sort the documents in the retrieved index


## 1 - Semantic Label Indexing
Utilize semantics to cluster the label sets.

1. Label embedding via label text
Instead of using label IDs, use semantic information about the labels (ex. description of categories in the Wikipedia dataset) to represent labels. <br>
Use ELMo [26], to represent the words in the label. <br>
The label embedding is created by a mean pooling over all word embeddings in the label text. <br>
(Not using BERT because without finetuning the token embedding of BERT or other variants may not be suitable for the clustering problem.)

2. Label embedding via keywords from positive instances
Another label representation derived from the sparse text embedding of instances. <br>
This type of label embedding are refered to as Positive Instance Feature Aggregation, shorthand as PIFA.

3. Label indexing 
With the above label representations, build the indexing system by clustering the labels as in label partitioning methods.
Default setting is balanced k-means clustering. 

## 2 - Deep Neural Matching
ssign relevant clusters (i.e., indices) to each instance. <br>
The problem is reduced from XMC to MLC problem (normal multi-label classification are refered to as MLC). <br>
The key to a successful search engine is high-recall matching since the subsequent ranking phase is based on the retrieved documents from the matching phase. <br>

## 3 - Ensemble Ranking
After the matching step, a small subset of label clusters is retrieved and the remaining task is to rank the labels in the clusters. <br>
A ranking model is neede to model the relevance between the instance and the retrieved labels. <br>
Given a label l and an instance x, its job is to find a mapping h(x, l) that maps the instance feature x and the label l to a score. <br>
The class label is positive if the instance belongs to the cluster, otherwise, it is negative.<br>
In this paper, mainly used ranking model is the linear one-vs-all (OVA) approach.


## Results of Different Configurations
Experiments on AmazonCat-13K and Wiki-500K dataset.

### Best Configuration
indexing: ELMo,PIFA <br>
matching: BERT <br>
ranking: linear <br>

For matching, finetuned BERT is more powerful than the X-Attention models and hierarchical linear models (Parabel). <br>
In the future they will go beyond linear to neural models for ranking. <br>
(The future seems to be this paper: [Taming Pretrained Transformers for Extreme Multi-label Text Classification](https://arxiv.org/pdf/1905.02331.pdf))

### Worst Configuration
indexing: PIFA <br>
matching: BERT <br>
ranking: tf-idf <br>

Worst result show the importance of learning rankers instead of unsupervised TF-IDF ranking. <br>
TF-IDF essentially re-ranks the labels within the retrieved clusters by word matching with the queried documents without learning any model. <br>


