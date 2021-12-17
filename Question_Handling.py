from Questions import data
import html

question_number = 0
correct_answer = ''

def check_more_questions_left():
    if question_number < len(data):
        return True
    return False

def next_question():
    global question_number
    global correct_answer

    get_question = data[question_number]
    question_number += 1

    correct_answer = get_question['correct_answer']
    question = html.unescape(get_question['question'])
    return question

def input_answer(answer):

    if str(answer) == correct_answer:
        return True
    else:
        return False