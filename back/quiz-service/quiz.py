import openai
import pandas as pd
import os
from dotenv import load_dotenv, find_dotenv 

def retrieve_key():
    '''
    Retrieve OPENAI API KEY stored in your .env file
    '''
    load_dotenv(find_dotenv())
    openai.api_key = os.getenv("OPENAI_API_KEY") 

def read_article():
    '''
    Read content article in .txt file
    '''
    article_path = "test_article\sample_article.txt"

    try:
        with open(article_path, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"File '{article_path}' not found.")
    except IOError:
        print(f"An error occurred while reading the file '{article_path}'.")

    return content

def prompt_quiz_generation(content):
    '''
    - Inject content into prompt
    - Use GPT3.5 Turbo Model to generate question and answers
    '''
    prompt = f"""
    Read this article and create 10 questions with 3 possible answer choices per question in the following format:

    Question Text
    Answer Choice Text
    Correct Answer : Correct Answer Text
    Correct Answer Explanation

    For example :
    What is the Captital City of Malaysia?
    A. Kuantan
    B. George Town
    C. Kuala Lumpur

    Correct Answer: Kuala Lumpur
    Explanation : Kuala Lumpur (Malaysian pronunciation: [ˈkualə, -a ˈlumpo(r), -ʊ(r)]), officially the Federal Territory of Kuala Lumpur (Malay: Wilayah Persekutuan Kuala Lumpur; ) and colloquially referred to as KL, is a federal territory and the ceremonial, legislative and judicial capital city of Malaysia.
    cv 
    Explain the correct answer in a friendly and academic tone based on the article content, as if you are explaining it to a student.

    Article: {content}
    """
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": f'{prompt}'}
        ]
    )
    GENERATED_QUIZ = response['choices'][0]['message']['content']
    return GENERATED_QUIZ

def quiz_qna_extraction():
    '''
    Extract Questions and Answers into two different strings
    '''


def main():
    retrieve_key()
    article_content = read_article()
    quiz_content = prompt_quiz_generation(article_content)
    print(quiz_content)

if __name__ == "__main__": 
    main()



    

