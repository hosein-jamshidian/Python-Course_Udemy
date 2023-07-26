from data import data
from question_class import Question
from quiz_brain import Quiz
question_bank=[]
for item in data:
    question_bank.append(Question(text=item["question"],answer=item["correct_answer"]))


quiz=Quiz(question_list=question_bank)
while quiz.still_has_question():
    quiz.next_quiz()
print("\n")
print(f"all score you collect:{quiz.score}/{len(question_bank)}".title())
