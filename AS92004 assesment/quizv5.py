#quiz version 5 multiple quizes
#in this version there are now multiple quizes you can choose from which are chemistry math and space.

#getting easy gui
from easygui import*
#setting up variables
score=0
try_again=["yes","no"]
qcorrect=[]
quizc=["chemistry","math","space"]
quiz_type=0
min_age=8
lyr=1 #lowest year level
hyr=14 #highest year levelb
#choices for all quizes
        #chemistry quiz choices
choices=[[["Au", "Ag", "Go", "Ga"],["H", "He", "O", "C"],["He", "Fe", "H", "N"],["Mg", "K", "Fe", "O"],["C", "N", "O", "He"]],
         #math quiz choices
         [["60", "70", "67", "83"],["90", "220", "300", "270"],["isosceles", "right", "scalene", "equalateral"],["20%", "30%", "70%", "45%"],["4", "16", "32", "8"]],
         #space quiz choices
         [["satern", "earth", "jupiter", "uranus"],["mercury", "jupiter", "neptune", "mars"],["mercury", "mars", "venus", "earth"],["62", "95", "231", "14"],["murcury", "neptune", "mars", "uranus"]]]
#the question and answers for all quizes
       #chemistry quiz + answers
quizes=[{"What is the symbol of gold":"Au",
      "What is the first element on the periodic table":"H",
      "What is the lightest element":"H",
      "Which element is on the second group third period":"Mg",
      "What element makes up most of the air you breathe":"N"},
      #math quiz + answers
       {"What is 23+47":"70",
      "what is 360 if it was decreases by 25%":"270",
      "the sides of a triangle is 4, 4, 6. what triangle is it?":"isosceles",
      "there are 7 blue balls and 3 red balls,\n what is the probability of a red ball getting picked? ":"30%",
      "what is the product of 4 and 8":"32"},
      #space quiz + answers
       {"what is the largest planet in the solar system":"jupiter",
      "what is the furthest planet in the solar system":"neptune",
      "what is the smallest planet in the solar system":"mercury",
      "how many moons does jupiter have":"95",
      "the chemical element uranium was names after what planet":"uranus"}]


#asking name
def user_info():
    global name,age,year_level
    name = enterbox("enter your name: ","name")
    while True:
        if name==None:name = enterbox(f"you must enter a name\n\nenter your name","name")
        elif name=="":name = enterbox(f"you must enter a name\n\nenter your name","name")
        else:break
    #asking age and year level(can only be between 1 and 13)
    while True:
        try:
            age = int(enterbox("enter your age"))
            if age<min_age:
                msgbox("you must be older than 8 to play")
            else:break
        except (ValueError,TypeError):
            msgbox("enter a valid integer","error")
    while True:
        try:
            year_level=int(enterbox("enter year level (1-13)"))
            if year_level not in range(lyr,hyr):
                raise(ValueError)
            else:break
        except (ValueError,TypeError):
            msgbox("enter a valid integer","error")

#function to ask all the questions
def questions(choices,quizes,score):
    for choices,question in zip(choices[quiz_type],quizes[quiz_type]):
            user_answer=buttonbox(question,"questions", choices)
            if user_answer==quizes[quiz_type][question]:
                qcorrect.append("correct")
                msgbox("correct","correct")
                score=score+1
            else:qcorrect.append("incorrect"), msgbox("incorrect","incorrect")
    return(score)

#functions to compile all the imformation and show the user
def history(score):    
    score=questions(choices,quizes,score)
    history="\n".join(f"{question}: {correct}\nanswer: {quizes[quiz_type][question]}\n" for correct,question in zip(qcorrect,quizes[quiz_type]))
    msgbox(f"\nName:{name}\nAge:{age}\nyear level:{year_level}\nquiz: {quizc[quiz_type]}\nscore: {score}/5\n\nquestions\n{history}","history")
    with open("quiz_history.txt","a") as quiz_info:
        quiz_info.write(f"\nName:{name}\nAge:{age}\nyear level:{year_level}\nquiz: {quizc[quiz_type]}\nscore: {score}/5\n\nquestions\n{history}")
#the code to determine what type of quiz to play
def quiz_choice(quiz_type):
    while True:
        quiz=buttonbox("what quiz would you like to play?","quiz choice",quizc)
        if quiz==quizc[0]:quiz_type=0
        elif quiz==quizc[1]:quiz_type=1
        elif quiz==quizc[2]:quiz_type=2
        #if the user pressing the close button
        elif quiz==None:
            msgbox("you must select a quiz","select quiz")
            continue
        return quiz_type
    

#to ask the user if they want to try the quiz again and to play the quiz
user_info()
while True:
    quiz_type=quiz_choice(quiz_type)
    history(score)
    again=buttonbox("do you want to try again","try again",try_again)
    if again==try_again[0]:
        #reset the list 
        qcorrect=[]
        continue
    msgbox("thank you for playing the quiz")
    break