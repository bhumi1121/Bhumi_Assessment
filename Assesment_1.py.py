def mainmenu():
    m = '''
        WELCOME TO TOPS QUIZ GAMINGING CHALLANGE
        Select your role:
                    --> Quiz master   (press 1)
                    --> Quiz cracker  (press 2)

       '''
    print(m)
    role = input("Enter your role: ")

    if role == "1":
        print("Welcome master")
        print("SHAKE YOUR BRAIN AND ADD SOME CHALLANGING QUESTIONS..")
        question_dict = {}

        while True:
            a = '''
                press 1 for add question
                press 2 for view question
                press 3 for delete question
                press 4 for exit

               '''
            print(a)
            op = input("Which operation do you want to perform? ")

            if op == "1":
                qno = int(input("Q.no: "))
                q = input("Enter your question: ")
                op1 = input("Enter option 1: ")
                op2 = input("Enter option 2: ")
                ans = input("Enter the correct answer (1 or 2): ")

                question_dict[qno] = {
                    'question': q,
                    'option 1': op1,
                    'option 2': op2,
                    'answer': ans
                }
                print(question_dict)
                print("Question added successfully....")

            elif op == '2':
                if not question_dict:
                    print("No question added yet ....")
                else:
                    print("Current questions: ")
                    for qno, que in question_dict.items():
                        print(f"Q{qno}: {que['question']}")
                        print(f"  1. {que['option 1']}")
                        print(f"  2. {que['option 2']}")
                        print()

            elif op == '3':
                qno = int(input("Enter question number to delete: "))
                if qno in question_dict:
                    del question_dict[qno]
                    print("Question deleted successfully...")
                else:
                    print("Question not found")

            elif op == '4':
                print("Exit")
                break

            else:
                print("Invalid option please try again")

    elif role == '2':
        print("Welcome quiz cracker")
        print("Get ready to solve some challenging questions")
    else:
        print("Invalid role. Please enter 1 or 2")


mainmenu()
def quiz_cracker(questions_dict):
    score = 0
    print("SCORE =", score)

    for question, correct_answer in questions_dict.items():
        print(question)
        ans = input("Enter your answer: ")

        if ans.lower() == correct_answer.lower():
            score += 5
        else:
            score -= 10

    print("Your Score:", score)


d1 = {
    "Who developed the Python language?": 'guido van rossum',
    "When was the Python language released?": 'february 20,1991',
    "Who is the Prime Minister of India?": 'narendra modi',
    "In which language is Django used?": 'python',
    "How much population is there in India?": '142cr',
    "At which position is India placed about population in the whole world?": '1',
    "Who is the best cricket player in the world?": 'Virat kohli',
    "Who is the 1st hacker in the world?": 'john draper',
    "Which thing was hacked 1st in the world?": 'land line',
    "Who was the 1st person to go into space from India?": 'rakesh sharma'
}

mainmenu()

role = input("Enter your role: ")

if role == '2':
    print("Welcome quiz cracker")
    print("Get ready to solve some challenging questions")
    quiz_cracker(d1)
