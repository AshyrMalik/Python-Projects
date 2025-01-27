from question_model import Question
from data import question_data
from quiz_brain import Quiz
question_Bank = []

for question in question_data:
    question_text = question["text"]
    question_ans = question["answer"]

    question_Bank.append(Question(text=question_text,ans=question_ans))


quiz = Quiz(question_list=question_Bank)

while quiz.still_has_question():
    quiz.next_question()



