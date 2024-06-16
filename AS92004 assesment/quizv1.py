#quiz version 1
#in the version the quiz uses lists and dictionaries to show a chemistry quiz

#setting up variables
s=0
qcorrect=[]
score=0

name = input("enter your name: ")
#the questions and answers and choices
qa = {"What is the symbol of gold":"Au","What is the first element on the periodic table ":"H","What is the lightest element":"H","Which element is on the second group third period":"Mg","What element makes up most of the air you breathe":"N"}
choices=[["Au", "Ag", "Go", "Ga"],["H", "He", "O", "C"],["He", "Fe", "H", "N"],["Mg", "K", "Fe", "O"],["C", "N", "O", "He"]]

#code for asking the questions and counting score
for choices,question in zip(choices,qa):
    print(question)
    for choice in choices:
        print(choice)
    user_ans=input(":")
    if user_ans==qa[question]:
        print ("correct")
        qcorrect.append("correct")
        score=score+1
    else:
        print("incorrect")
        qcorrect.append("incorrect")
    
#code prints out the question if you got it correct or not and the correct answer
history="\n".join(f"{question}: {correct}\nanswer: {qa[question]}\n" for correct,question in zip(qcorrect,qa))
print(f"\nName:{name}\nscore: {score}/5\n{history}")


 