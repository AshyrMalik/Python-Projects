class Quiz:
    def __init__(self,question_list):
        self.num_of_question= 0
        self.question_list=question_list
        self.score=0


    def next_question(self):

        question = self.question_list[self.num_of_question]
        question_text = question.text
        question_ans = question.ans
        x = input( f"Q{self.num_of_question + 1}: {question_text}? (True/False): ")
        self.check_answer(ans=question_ans,user_ans=x)
        self.num_of_question += 1

    def still_has_question(self):

        return not self.num_of_question == len(self.question_list)

    def check_answer(self,ans,user_ans):
        if ans == user_ans:
            print("You got it right")
            self.score+=1
            print(f"Score : {self.score}")
        else:
            print("Wrong answer")
            print(f"Score : {self.score}")






