question_list = [
    "\nThe SI unit of length is :\n (a) deg C \n (b) metre sq \n (c) metre \n (d) litre \n",
    "\nThe melting point of ice is :\n (a) 0 deg C \n (b) 10 deg C \n (c) 100 deg C \n (d) 72 deg C \n",
    "\nThe boiling point of water is :\n (a) 1 deg C \n (b) 10 deg C \n (c) 100 deg C \n (d) 72 deg C \n",
    "\nThe SI unit of heat is :\n (a) deg C \n (b) joule \n (c) metre \n (d) litre \n",
    "\nOne calorie is equal to :\n (a) 4.2 joule \n (b) 4.4 joule \n (c) 4.5 joule \n (d) 4.184 joule \n",
]


class Question_class:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer


question_ready = [
    Question_class(question_list[0], "c"),
    Question_class(question_list[1], "a"),
    Question_class(question_list[2], "c"),
    Question_class(question_list[3], "b"),
    Question_class(question_list[4], "d"),
]


def run_test(questions):
    score = 0
    for question in questions:
        # try :
        print(question.question)
        ans = input(">>> ").lower()
        if ans == question.answer:
            score += 1
    # except :
    #     print("you did not choose right option..!")
    print(f"\nyou answered {score} / {len(questions)} correctly .\n")


run_test(question_ready)

print()
print("Program Ended.")
input
