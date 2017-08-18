# Recommending Articles

The goal of this project is to learn how to make a simple article recommendation engine using a semi-recent advance in natural language processing called [word2vec](http://arxiv.org/pdf/1301.3781.pdf) (or just *word vectors*). In particular, we're going to use a "database" from [Stanford's GloVe project](https://nlp.stanford.edu/projects/glove/) trained on a dump of Wikipedia.

You are going to build a web server that displays a list of [BBC](http://mlg.ucd.ie/datasets/bbc.html) articles for URL `http://localhost` (testing) or whatever the IP address is of your Amazon server (deployment):

<img src=figures/articles.png width=220>

Clicking on one of those articles takes you to an article page that shows the text of the article as well as a list of five recommended articles:

<img src=figures/article1.png width=450>

<img src=figures/article2.png width=450>

## Discussion

http://localhost


figure out how to make square bullets, font size 70%, font family Verdana, sans-serif. h1 is 130% size


http://localhost/article/business/030.txt


## Getting started

├── doc2vec.py
├── server.py
└── templates
    ├── article.html
    └── articles.html

## Deliverables

* doc2vec.py
* server.py
* templates/article.html
* templates/articles.html

## Evaluation
