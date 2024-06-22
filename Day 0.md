- Go through Scikit learn 
- Why do we need Gensim?? (solved in meet 1)
- Word embeddings??? (solved in meet 1)
- Get the dataset and get the keywords and named entities from it using TF-IDF (done)
- Read the Glove paper (done)
- where do we go from here? Graphs? Heatmaps??
- made a tree structure to view it
- now what?
- reading scikit-learn documentation
- read Harsh sir's blog (he really likes BuiltWith)
one developer managing a huge SaaS product generating millions in income 
- What is FASTAPI? do we need it here?
- Figure out how to use Kaggle
- New dataset: Google Cloud

- Read the autocorrect blog
- Glove is basically looking at the probability of 2 words occurring the vicinity of each other 


# Day 1

Meeting:
ICP - Ideal Customer Profile

FastText/Glove for word embeddings

-Todo:
- Google n-grams viewers
- Counter/Dictionaries (Python)
- Word2Vector(Gensim)
- Cosine Similarity using the word embeddings
- tSNE
- Vector Search Engines

For today:
1. FastText Embeddings data file
2. Load the files in Python
3. Have a dictionary representation
dictionary has a key. When you input the key you get a vector. Now we use cosine similarity to get the synonym 
`word_vec = {}`
`word_vec['magnificent'] = [0.1,0.43,0.432....]`
`for K,v in word_vec.items() :`
`distance[k] = dist(input_vec,v)`  //brute force approach
5. Use scikit-learn to get a word matrix and upon getting a vector gives us the nearest neighbours

Vector Index
HNSW
IVFFLAT
FAISS

Go through Annoy to try to understand it

Learn Word2Vec
what do people usually talk about when talking about S3 
try to build a simple visualisation for a bunch of keywords
