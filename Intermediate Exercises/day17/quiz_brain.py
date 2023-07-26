class Quiz:
    def __init__(self,question_list):
        self.score=0
        self.question_number=0
        self.question_list=question_list

    def still_has_question(self):
        return self.question_number<len(self.question_list)

    def next_quiz(self):
        current_quiz=self.question_list[self.question_number]
        self.question_number+=1
        user_answer=input(f"Q{self.question_number} : {current_quiz.text}(True/False)").lower()
        self.check_answer(user_answer,current_quiz.answer)

    def check_answer(self,user_answer,right_answer):
        if user_answer==right_answer.lower():
            print(f"you got it right")
            self.score+=1
        else:
            print("you Wrong")
        print(f"the True answer is {right_answer}")
        print(f"the score you collect till now :{self.score}/{self.question_number}")


