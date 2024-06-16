#quiz version 3 using easy gui
#in this version the quiz is now in easy gui
#it also asks for your name age and year level
#if your age is below 8 or is not between 1 to 13 than you will need to add a valid number
#you can also try again

#getting easy gui
from easygui import*
#setting up variables and constants
qcorrect=[]
score=0
try_again=["yes","no"]
lyr=1 #lowest year level
hyr=14 #highest year level
#asking name
name = enterbox("enter your name: ","name")
while True:
    if name==None:name = enterbox(f"you must enter a name\n\nenter your name","name")
    elif name=="":name = enterbox(f"you must enter a name\n\nenter your name","name")
    else:break
#asking age and year level(can only be between 1 and 13)
while True:
    try:
        age = int(enterbox("enter your age"))
        year_level=int(enterbox("enter year level (1-13)"))
        if year_level not in range(lyr,hyr):
            raise(ValueError)
        else:break
    except (ValueError,TypeError):
        msgbox("enter a valid integer","error")


#the questions and answers and choices
qa = {"What is the symbol of gold":"Au","What is the first element on the periodic table ":"H","What is the lightest element":"H","Which element is on the second group third period":"Mg","What element makes up most of the air you breathe":"N"}
choices=[["Au", "Ag", "Go", "Ga"],["H", "He", "O", "C"],["He", "Fe", "H", "N"],["Mg", "K", "Fe", "O"],["C", "N", "O", "He"]]

#function to ask all the questions
def questions(choices,qa,score):
    for choices,question in zip(choices,qa):
            user_answer=buttonbox(question,"questions", choices)
            if user_answer==qa[question]:
                qcorrect.append("correct")
                score=score+1
            else:qcorrect.append("incorrect")
    return(score)

#functions to compile all the imformation and show the user
def history(score):    
    score=questions(choices,qa,score)
    history="\n".join(f"{question}: {correct}\nanswer: {qa[question]}\n" for correct,question in zip(qcorrect,qa))
    msgbox(f"\nName:{name}\nAge:{age}\nyear level:{year_level}\nscore: {score}/5\n{history}","history")
    
#to ask the user if they want to try the quiz again
while True:
    history(score)
    again=buttonbox("do you want to try again","try again",try_again)
    if again==try_again[1]:
        break
    
