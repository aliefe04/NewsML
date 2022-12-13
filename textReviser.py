import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
nltk.download('punkt')
# add punctuation to stopwords
stopwords = stopwords.words('turkish')

def textRev(filename):
    text = open(f"{filename}.txt", "r", encoding="utf-8").read()
    text_tokens = word_tokenize(text)
    tokens_without_sw = [word for word in text_tokens if not word in stopwords]
    open(f"{filename}Rev.txt", "w", encoding="utf-8").write(" ".join(tokens_without_sw))


textRev("text")
