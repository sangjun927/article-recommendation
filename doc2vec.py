import sys
import re
import string
import os
import numpy as np
import codecs
import pickle

# From scikit learn that got words from:
# http://ir.dcs.gla.ac.uk/resources/linguistic_utils/stop_words
ENGLISH_STOP_WORDS = frozenset([
    "a", "about", "above", "across", "after", "afterwards", "again", "against",
    "all", "almost", "alone", "along", "already", "also", "although", "always",
    "am", "among", "amongst", "amoungst", "amount", "an", "and", "another",
    "any", "anyhow", "anyone", "anything", "anyway", "anywhere", "are",
    "around", "as", "at", "back", "be", "became", "because", "become",
    "becomes", "becoming", "been", "before", "beforehand", "behind", "being",
    "below", "beside", "besides", "between", "beyond", "bill", "both",
    "bottom", "but", "by", "call", "can", "cannot", "cant", "co", "con",
    "could", "couldnt", "cry", "de", "describe", "detail", "do", "done",
    "down", "due", "during", "each", "eg", "eight", "either", "eleven", "else",
    "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone",
    "everything", "everywhere", "except", "few", "fifteen", "fifty", "fill",
    "find", "fire", "first", "five", "for", "former", "formerly", "forty",
    "found", "four", "from", "front", "full", "further", "get", "give", "go",
    "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter",
    "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his",
    "how", "however", "hundred", "i", "ie", "if", "in", "inc", "indeed",
    "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter",
    "latterly", "least", "less", "ltd", "made", "many", "may", "me",
    "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly",
    "move", "much", "must", "my", "myself", "name", "namely", "neither",
    "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone",
    "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on",
    "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our",
    "ours", "ourselves", "out", "over", "own", "part", "per", "perhaps",
    "please", "put", "rather", "re", "same", "see", "seem", "seemed",
    "seeming", "seems", "serious", "several", "she", "should", "show", "side",
    "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone",
    "something", "sometime", "sometimes", "somewhere", "still", "such",
    "system", "take", "ten", "than", "that", "the", "their", "them",
    "themselves", "then", "thence", "there", "thereafter", "thereby",
    "therefore", "therein", "thereupon", "these", "they", "thick", "thin",
    "third", "this", "those", "though", "three", "through", "throughout",
    "thru", "thus", "to", "together", "too", "top", "toward", "towards",
    "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us",
    "very", "via", "was", "we", "well", "were", "what", "whatever", "when",
    "whence", "whenever", "where", "whereafter", "whereas", "whereby",
    "wherein", "whereupon", "wherever", "whether", "which", "while", "whither",
    "who", "whoever", "whole", "whom", "whose", "why", "will", "with",
    "within", "without", "would", "yet", "you", "your", "yours", "yourself",
    "yourselves"])


def load_glove(filename):
    with codecs.open(filename, 'r', encoding='utf-8') as f:
        vectors = {}
        for line in f:
            vals = line.strip().split()
            word = vals[0]
            if word in ENGLISH_STOP_WORDS:
                continue
            vector = np.asarray(vals[1:], dtype='float32')
            vectors[word] = vector
        return vectors

def filelist(root):
    allfiles = []
    for path, subdirs, files in os.walk(root):
        for name in files:
            allfiles.append(os.path.join(path, name))
    return allfiles

def get_text(filename):
    with codecs.open(filename, encoding='latin-1', mode='r') as f:
        return f.read()

def words(text):
    text = text.lower()
    text = re.sub("[" + string.punctuation + '0-9\\r\\t\\n]', ' ', text)
    words = text.split()
    words = [word for word in words if len(word) >= 3 and word not in ENGLISH_STOP_WORDS]
    return words

def split_title(text):
    lines = text.strip().split("\n")
    title = lines[0]
    content = "\n".join(lines[1:])
    return title, content

def doc2vec(text, gloves):
    wordlist = words(text)
    vectors = [gloves[w] for w in wordlist if w in gloves]
    if not vectors:
        return None
    centroid = np.mean(vectors, axis=0)
    return centroid

def load_articles(articles_dirname, gloves):
    articles = []
    for filename in filelist(articles_dirname):
        if not filename.endswith('.txt'):
            continue
        text = get_text(filename)
        title, content = split_title(text)
        centroid = doc2vec(content, gloves)
        if centroid is not None:
            articles.append([filename, title, content, centroid])
    return articles

def distances(article, articles):
    dists = np.linalg.norm([article[3] - a[3] for a in articles], axis=1)
    return [(d, articles[i]) for i, d in enumerate(dists)]

def recommended(article, articles, n):
    dists = distances(article, articles)
    sorted_dists = sorted(dists, key=lambda x: x[0])
    top_articles = sorted_dists[1:n+1]
    #print(top_articles)
    return [(a[1], re.sub(r'^.*/', '', a[0]), a[2]) for d, a in top_articles]

def main():
    glove_filename = sys.argv[1]
    articles_dirname = sys.argv[2]

    gloves = load_glove(glove_filename)
    articles = load_articles(articles_dirname, gloves)

    articles_data = [[a[0], a[1], a[2]] for a in articles]  
    with open('articles.pkl', 'wb') as f:
        pickle.dump(articles_data, f)

    recommendations = {}
    for article in articles:
        key = (article[0], article[1])  
        recommendations[key] = recommended(article, articles, 5)

    with open('recommended.pkl', 'wb') as f:
        pickle.dump(recommendations, f)

if __name__ == '__main__':
    main()