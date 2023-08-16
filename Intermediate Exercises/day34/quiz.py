#--------------------------------------------------- Quiz Class -------------------------------------------------------
class Quiz:
    def __init__(self,question_bank):
        self.score=0
        self.question_number=0
        self.question_bank=question_bank

#---------------------------------------------------- Next Question Text ----------------------------------------------
    def next_question(self):
        if self.still_question():
            current_question=self.question_bank[self.question_number]
            return f'Q.{self.question_number}: {current_question.question}?'

#--------------------------------------------------- Check Still Question Condition -----------------------------------
    def still_question(self):
        if self.question_number<len(self.question_bank):
            return True
        else:
            print('DONE🥶')
            return False