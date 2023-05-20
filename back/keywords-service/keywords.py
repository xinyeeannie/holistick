import yake
from flask import Flask, jsonify, request

keywords = Flask(__name__)

def kw_extractor(text):
    '''
    Keyword extraction using yake library
    '''
    kw_extractor = yake.KeywordExtractor(top=10, stopwords=None)
    keywords = kw_extractor.extract_keywords(text)
    for kw, v in keywords:
        print("Keyphrase: ",kw, ": score", v)

def get_content():
    '''
    Retrive content
    '''
    article_path = "test_article/article.txt"
    try:
        with open(article_path, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"File '{article_path}' not found.")
    except IOError:
        print(f"An error occurred while reading the file '{article_path}'.")
    return content

def main():
    text = get_content()
    kw_extractor(text)


if __name__ == "__main__":
    main()
    keywords.run(debug=True, port=16460)
