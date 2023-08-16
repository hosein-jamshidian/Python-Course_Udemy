from data import total_question
from question import Question
from quiz import Quiz
from ui import UI
import html

# ------------------------------------------ Use API to Get Our Quetions & Answers ------------------------------------
question_bank=[]
for item in total_question:
    question_bank.append(Question(question=html.unescape(item['question']),answer=item['correct_answer']))

# ---------------------------------------------------- Main Body -----------------------------------------------------
quiz=Quiz(question_bank)

ui=UI(quiz)
