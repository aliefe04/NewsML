import nltk
import pyperclip
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from tkinter import Tk

nltk.download("stopwords")
nltk.download("punkt")
# add punctuation to stopwords
stopwords = stopwords.words("turkish")


def textRev(filename):
    text = Tk().clipboard_get()
    text_tokens = word_tokenize(text)
    tokens_without_sw = [word for word in text_tokens if not word in stopwords]
    open(f"{filename}Rev.txt", "w", encoding="utf-8").write(" ".join(tokens_without_sw))
    pyperclip.copy(" ".join(tokens_without_sw))
    print("done")


textRev("text")
