import itertools

import numpy as np
from nltk.cluster.util import cosine_distance
import networkx as nx

def get_sentence_vector(word_embeddings, sentence, we_dim):
    vector = np.zeros((we_dim, ))

    sentence_length = len(sentence) + 0.001

    if sentence:
        sentence_embeddings = sum([word_embeddings.get(word, vector) for word in sentence])

        vector = sentence_embeddings/sentence_length

    return vector

def sentence_similarity(vector1, vector2):
    similarity_score = 1 - cosine_distance(vector1, vector2)

    if np.isnan(similarity_score):
        similarity_score = 0

    return similarity_score

import scipy

def build_similarity_matrix(sentence_vectors, verbose=False):
    sentence_length = sentence_vectors.shape[0]

    if isinstance(sentence_vectors, scipy.sparse.csr.csr_matrix):
        sentence_vector_arrays = sentence_vectors.toarray()
    else:
        sentence_vector_arrays = sentence_vectors

    # Create an empty similarity matrix
    similarity_matrix = np.zeros((sentence_length, sentence_length))

    # create index of word pairs
    permutation_set = list(itertools.permutations(range(0, sentence_length), 2))

    for pair in permutation_set:
        idx1, idx2 = pair

        sent1 = sentence_vector_arrays[idx1]
        sent2 = sentence_vector_arrays[idx2]

        if verbose:
            print(f"Sentences: \n{sent1}\n{sent2}")

        similarity_matrix[idx1][idx2] = sentence_similarity(sentence_vector_arrays[idx1], sentence_vector_arrays[idx2])

    return similarity_matrix

def apply_textrank(similarity_matrix):
    sentence_similarity_graph = nx.from_numpy_array(similarity_matrix)
    scores = nx.pagerank(sentence_similarity_graph)
    return scores

def visualise_top_scores(scores, flatten_sentences, n_top):
    ranked_sentence = sorted(((scores[i], s) for i, s in enumerate(flatten_sentences)), reverse=True)    
    print(ranked_sentence[0])

    summarise_text = []

    for i in range(n_top):
        summarise_text.append(ranked_sentence[i][1])

    return summarise_text