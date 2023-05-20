import openai
import pandas as pd
import os
import re
import json
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
    article_path = "../testing-article/NN-article.txt" # linked to sample article, please change this connection with txt retrieval from frontend later

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

    For example :
    What is the Captital City of Malaysia?
    A. Kuantan
    B. George Town
    C. Kuala Lumpur

    Correct Answer: Kuala Lumpur

    Please check if the answers are correct and can be found based on the article.

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

def quiz_qna_extraction(text):
    '''
    Extract Questions and Answers into two different strings
    '''
    # Use regular expressions to extract the questions, answer choices, and correct answers

    pattern_question = r"\d.+[^\n]"
    question_matches = re.findall(pattern_question, text)

    pattern_choices = r"([A-Z]\. \w+.+\n)+"
    choices_matches = re.findall(pattern_choices, text)

    pattern_answer = r"Correct Answer:+.\w.+[^\n]"
    answer_matches = re.findall(pattern_answer, text)

    # Combine every answer choice (A-C) per question
    data = []
    choices_array = []

    for i in range(0, len(choices_matches),3):
        combined_choices = ' '.join(choices_matches[i:i+3]) + ' '
        choices_array.append(combined_choices)


    for i in range(len(question_matches)):
        question_data = {
            'question': question_matches[i],
            'choices': choices_array[i],
            'correct_answer': answer_matches[i]
        }
        data.append(question_data)

    json_data = json.dumps(data, indent=4)

    print(json_data)

    # send this to frontend



def main():
    print("test")
    retrieve_key()
    article_content = read_article()
    quiz_content = prompt_quiz_generation(article_content)
    quiz_qna_extraction(quiz_content)

if __name__ == "__main__": 
    main()



    

