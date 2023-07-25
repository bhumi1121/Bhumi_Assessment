class Games:
    def display(self):
        print("WELCOME TO TOPS QUIZ GAMING CHALLENGE")


class Child(Games):
    def displayA(self):
        print("Select your role: ")


class Child2(Child):
    def displayB(self):
        print("Quiz master   (press 1)")
        print("Quiz cracker  (press 2)")


class Child3(Child2):
    def displayC(self):
        role = input("Enter your role: ")
        if role == "1":
            print("Selected role: Quiz master")
        elif role == "2":
            print("Selected role: Quiz cracker")
        else:
            print("Invalid number")
            
class master(Child3):
    def displayD(self):
        print("Welcome master")
        print("SHAKE YOUR BRAIN AND ADD SOME CHALLANGING QUESTION")
#-------------------------------ADD,VIEW,DELETE,EXIT------------------------------------------
class QuizMenu(master):
    def displayE(self):
        print("MENU")
        all1 = {
            'Que.1': "For Add Question (press 1)",
            'Que.2': "For View Question (press 2)",
            'Que.3': "For Delete Question (press 3)",
            'Que.4': "For Exit (press 4)"
        }
        print(all1)
#-------------------------------------Add question------------------------------------------
class AddQuestion(QuizMenu):
    def displayF(self):
        while True:
            a = input("Which operation do you want to perform: ")

            if a == "1":
                question = input("Enter the question: ")
                option1 = input("Enter Option 1: ")
                option2 = input("Enter Option 2: ")
                answer = input("Enter the correct option (1 or 2): ")

            elif a == "2":
                print(question)
                print(option1)
                print(option2)
                print(answer)
                

            elif a == "3":
                pass

            elif a == "4":
                print("Exiting the quiz menu.")
                break

            else:
                print("Invalid choice.")        


a = AddQuestion()
a.display()
a.displayA()
a.displayB()
a.displayC()
a.displayD()
a.displayE()
a.displayF()



