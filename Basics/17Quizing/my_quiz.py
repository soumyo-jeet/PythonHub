questions = {
    "The sky is red." : "false",
    "Moon is a sattelite of Jupitor." : "false",
    "Earth is the second biggest plannet in the sun-family" : "true",
    "Sun-family is in the Milk-Way galxy." : "true"
}


class Judge:
    def __init__(self,question,answer):
        self.answer = answer
        self.right= questions[question]

    def check(self) :
        if self.answer == self.right :
            return True
        else:
            return False

def start_quiz():
    score= 0
    q_no = 1
    for qs in questions:
        answer= input(f"Q.{q_no} {qs} (True/False): ").lower()
        judge = Judge(qs, answer)
        if judge.check():
            score += 1
            print("You're Right!!")
        else:
            print("You're Wrong!!")

        print(f"Your Score {score}")
        q_no += 1

    print(f"Congratulations! You've Completed The Quiz And Your Final Score Is {score}")

retry = 'y'
while retry == 'y':
    print("\n" * 50)
    start_quiz()
    retry= input("Retry? 'y' for yes 'n' for no: ")


