#quiz version 2 with functions
#in this version the quiz uses functions 
#the user can enter capital and lower case letters without being marked incorrect

#setting up variables
qcorrect=[]
score=0
name = input("enter your name: ")
#the questions and answers and choices
qa = {"What is the symbol of gold":"Au","What is the first element on the periodic table ":"H","What is the lightest element":"H","Which element is on the second group third period":"Mg","What element makes up most of the air you breathe":"N"}
choices=[["Au", "Ag", "Go", "Ga"],["H", "He", "O", "C"],["He", "Fe", "H", "N"],["Mg", "K", "Fe", "O"],["C", "N", "O", "He"]]

#function to ask the user the questions and check wether they are correct or incorrect 
def questions(choices,qa,score):
    for choices,question in zip(choices,qa):
        print(question)
        for choice in choices:
            print(choice)
        user_ans=input(":")
        #using .capitalize to make all useranswer equal to the answer regardless of capitilisation
        if user_ans.capitalize()==qa[question]:
            print ("correct")
            qcorrect.append("correct")
            score=score+1
        else:
            print("incorrect")
            qcorrect.append("incorrect")
    return(score)

#function to show the results
def history(score):
    score=questions(choices,qa,score)
    history="\n".join(f"{question}: {correct}\nanswer: {qa[question]}\n" for correct,question in zip(qcorrect,qa))
    print(f"\nName:{name}\nscore: {score}/5\n{history}")

#calling the function
history(score) 