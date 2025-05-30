class question:
    def __init__(self,discription,correct_answer,options):
        self.disc=discription
        self.ans=correct_answer
        self.opt=options
    def display(self,questions_num):
        print(questions_num,".",self.disc)
        for key,value in self.opt.items():
            print(key,".",value)

# Main Program


print("\t\t\t\t\tWelcome To My Football Quiz\n\n\n")
playing=input("Do you wanna play?(yes/no) ")
while(True):
    if playing=='yes' or playing=='Yes':
        print("\n")
        wrong_answer={}
        correct_answer={}
        print("Ok Let's Play :) ")
        print("\n")
        while playing=='yes' or playing=='Yes':
            score=0
            i=1
            while i<6:
                if i==1:
                    options={"A":"9","B":"10","C":"11","D":"12"}
                    q=question("What is the maximum number of players a team can have on the field during a football match?",'C',options)
                    q.display(i)
                    correct_answer["1"]=["What is the maximum number of players a team can have on the field during a football match?","11"]
                    print("\n")
                    ans=input("Enter your answer: ")
                    if ans.strip().lower()==q.ans.strip().lower():
                        score=score+1
                    else:
                        wrong_answer["1"]=["What is the maximum number of players a team can have on the field during a football match?","11",options[ans.upper()]]
                    i+=1
                    print("\n")
                elif i==2:
                    options={"A":"Brazil","B":"Germany","C":"France","D":"Argentina"}
                    q=question("Which country won the FIFA World Cup in 2018?",'C',options)
                    q.display(i)
                    correct_answer["2"]=["Which country won the FIFA World Cup in 2018?","France"]
                    print("\n")
                    ans=input("Enter your answer: ")
                    if ans.strip().lower()==q.ans.strip().lower():
                        score=score+1
                    else:
                        wrong_answer["2"]=["Which country won the FIFA World Cup in 2018?","France",options[ans.upper()]]
                    i+=1
                    print("\n")
                elif i==3:
                    options={"A":"Triple Play","B":"Hat-Trick","C":"Goal Streak","D":"Trifecta"}
                    q=question("What is the term used when a player scores three goals in a single match?",'B',options)
                    q.display(i)
                    correct_answer["3"]=["What is the term used when a player scores three goals in a single match?","Hat-Trick"]
                    print("\n")
                    ans=input("Enter your answer: ")
                    if ans.strip().lower()==q.ans.strip().lower():
                        score=score+1
                    else:
                        wrong_answer["3"]=["What is the term used when a player scores three goals in a single match?","Hat-Trick",options[ans.upper()]]
                    i+=1
                    print("\n")
                elif i==4:
                    options={"A":"Lionel Messi","B":"Cristiano Ronaldo","C":"Neymar","D":"Kylian Mbappe"}
                    q=question("Which footballer is famously known as ""CR7""?",'B',options)
                    q.display(i)
                    correct_answer["4"]=["Which footballer is famously known as ""CR7""?","Cristiano Ronaldo"]
                    print("\n")
                    ans=input("Enter your answer: ")
                    if ans.strip().lower()==q.ans.strip().lower():
                        score=score+1
                    else:
                        wrong_answer["4"]=["Which footballer is famously known as ""CR7""?","Cristiano Ronaldo",options[ans.upper()]]
                    i+=1
                    print("\n")
                elif i==5:
                    options={"A":"Italy","B":"Spain","C":"Portugal","D":"France"}
                    q=question("In which country is the football club Barcelona based?",'B',options)
                    q.display(i)
                    correct_answer["5"]=["In which country is the football club Barcelona based?","Spain"]
                    print("\n")
                    ans=input("Enter your answer: ")
                    if ans.strip().lower()==q.ans.strip().lower():
                        score=score+1
                    else:
                        wrong_answer["5"]=["In which country is the football club Barcelona based?","Spain",options[ans.upper()]]
                    i+=1
                    print("\n")
            print("Enter 1 for all answers of the questions\n")
            print("Enter 0 for all answers of the wrong questions\n")
            choice_ans=int(input())
            print("\n")
            if choice_ans==1:
                print("Here are the answers of the questions ")
                print("\n")
                for key,value in correct_answer.items():
                    print(f"{key}: {value[0]}")
                    for item in value[1:]:
                        print("Ans: ",item,"\n")
            else:
                print("Here are the answers of the wrongly answered questions ")
                print("\n")
                for key,value in wrong_answer.items():
                    print(f"{key}: {value[0]}")
                    print("Your answer: ",value[2],"  ","Correct answer: ",value[1],"\n")
                                
            print("\n")
            print("\t\t\t\tYour final Score is: ",score)
            print("\n")
            playing=input("Do you want to play again ?(yes/no) ")
            if playing=='No' or playing=='no':
                print("OK!! See You Soon :) ")
                print("Thankew For Playing :)")
                exit()
    elif playing=="No" or playing=="no":
        print("OK!! See U next time :) ")
        exit()
    else:
        playing=input("Please enter a valid answer(yes/no): ")
        