import re

# from nltk.tokenize import word_tokenize
# from nltk.corpus import stopwords


# def preprocess_text(text):
#     # text="AI Engineering is the future!!!"
#     text = text.lower()                          #Lowercase "ai engineering is the future!!!"

#     text = re.sub(r"[^\w\s]", "", text)          #Remove punctuation "ai engineering is the future"

#     tokens = word_tokenize(text)                 #Tokenize ['ai', 'engineering', 'is', 'the', 'future']

#     stop_words = set(stopwords.words("english")) #Stop words {'is', 'the'}

#     filtered_tokens = [                          #Filter out stop words
#         word
#         for word in tokens
#         if word not in stop_words 
#     ]

#     return filtered_tokens # ['ai', 'engineering', 'future']

def preprocess_text(text):

    text = text.lower().strip()

    text = re.sub(r"[^\w\s]", "", text)

    return text