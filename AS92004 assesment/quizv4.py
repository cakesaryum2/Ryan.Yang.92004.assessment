#quiz version 4 writing to external file
#in this version the code writes to an external file and fixes printing error of the try again from the previous version
#it also makes it so if you are under age it will end the program

#getting easy gui
from easygui import*
#setting up variables
score=0
try_again=["yes","no"]
qcorrect=[]
min_age=8
lyr=1 #lowest year level
hyr=14 #highest year level
#the questions and answers and choices
qa = {"What is the symbol of gold":"Au",
      "What is the first element on the periodic table":"H",
      "What is the lightest element":"H",
      "Which element is on the second group third period":"Mg",
      "What element makes up most of the air you breathe":"N"}
choices=[["Au", "Ag", "Go", "Ga"],["H", "He", "O", "C"],["He", "Fe", "H", "N"],["Mg", "K", "Fe", "O"],["C", "N", "O", "He"]]

#asking name
name = enterbox("enter your name: ","name")
while True:
    if name==None:name = enterbox(f"you must enter a name\n\nenter your name","name")
    elif name=="":name = enterbox(f"you must enter a name\n\nenter your name","name")
    else:break
#asking age and year level(can only be between 1 and 13)
while True:
    try:
        while True:
            age = int(enterbox("enter your age"))
            if age<min_age:
                msgbox("you must be older than 8")
            else:break
        break
    except (ValueError,TypeError):
        msgbox("enter a valid integer ","error")
while True:
    try:
        year_level=int(enterbox("enter year level (1-13)"))
        if year_level not in range(lyr,hyr):
            raise(ValueError)
        else:break
    except (ValueError,TypeError):
        msgbox("enter a valid integer","error")


#function to ask all the questions
def questions(choices,qa,score):
    for choices,question in zip(choices,qa):
            user_answer=buttonbox(question,"questions", choices)
            if user_answer==qa[question]:
                qcorrect.append("correct")
                msgbox("correct","correct")
                score=score+1
            else:qcorrect.append("incorrect"), msgbox("incorrect","incorrect")
    return(score)

#functions to compile all the imformation and show the user
def history(score):    
    score=questions(choices,qa,score)
    history="\n".join(f"{question}: {correct}\nanswer: {qa[question]}\n" for correct,question in zip(qcorrect,qa))
    msgbox(f"\nName:{name}\nAge:{age}\nyear level:{year_level}\nscore: {score}/5\n{history}","history")
    with open("quiz_history.txt","a") as quiz:
        quiz.write(f"\nName:{name}\nAge:{age}\nyear level:{year_level}\nscore: {score}/5\n{history}")

#to ask the user if they want to try the quiz again
while True:
    history(score)
    again=buttonbox("do you want to try again","try again",try_again)
    if again==try_again[0]:
        qcorrect=[]
        continue
    break

