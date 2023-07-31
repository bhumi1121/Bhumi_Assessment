def mainmenu():
    while True:
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
            question_dict={}


            while True:
                a = '''
                    press 1 for add question
                    press 2 for view question
                    press 3 for delete question
                    press 4 for exit
    
                   '''
                print(a)
                op=input("Which opertion do you want to perform? ")

                if op =="1":
                    qno = int(input("Q.no: "))
                    que = {}
                    question_dict={}
                    q=input("Enter your question: ")
                    op1=input("Enter option 1: ")
                    op2=input("Enter option 2: ")
                    ans=input("Enter the correct answer (1 or 2): ")
                    que['q']=q
                    question_dict[qno]=que
                    print(question_dict)
                    print("Question added successfully....")

                elif op == '2':
                    if not question_dict:
                        print("No question added yet ....")
                    else:
                        print("current questions: ")
                        for qno in question_dict.items():
                            print("Q{qno}:{que['qestion']}")
                            print("  1. {que['option 1']}")
                            print("  2. {que['option 2']}")
                            print()
                elif op == '3':
                    qno = int(input("Enter question number to delete: "))
                    if qno in question_dict:
                        del question_dict[qno]
                        print("Question delete successfully...")
                    else:
                        print("Question not found")

                elif op == '4':
                    print("Exit")
                    break

                else:
                    print("invalid option please try agian")
        elif role == '2':
              print("Get ready to solve some challanging question")
        else:
            print("Invalid role .please enter 1 or 2")


score=0
print("SCORE =",score)


d1={
    'q':q,
    'op1':op1,
    'op2':op2,
    'ans':ans,
}


ans=""

for i,k in d1.items():
    print(i)
    ans=input("Enter your answer : ")

    if ans==k:
        score+=5
    else:
        score-=10

print("your Score : ",score)


mainmenu()

