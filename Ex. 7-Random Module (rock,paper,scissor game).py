#How to create Rock,Paper,Scissors Game using Random Module..
  # Winning Rules as follows:
     #Rock vs Scissor -> Paper Wins
     #Rock vs Scissor -> Rock Wins
     #Paper vs Scissor -> Scissor Wins

  #Condition
     #Scissors beats paper
     #Rock beats scissors 
     #Paper beats rock


import random
l=["rock","scissor","paper"]

while True:
    Ccount=0
    ucount=0
    uc=int(input('''
Game starr.....
1 Yes
2 No/Exit
     '''    ))

    if uc==1:
        for a in range(1,6):
            userinput=int(input('''
1.Rock
2.Scissor
3.Paper
            ''' ))
            if userinput==1:
               uchoice="rock"
            elif userinput==2:
                uchoice="scissor"
            elif userinput==3:
                uchoise="paper"

            Cchoice=random.choice(l)
            #print(uchoice)
            #print(Cchoice)

            if Cchoice==uchoice:                        # Frist Condition
                print("Computer Value",Cchoice)
                print("User value",uchoice)
                print("Game Draw")
                ucount=ucount+1
                ccount=Ccount+1

            elif (uchoice=="rock" and Cchoice=="scissor") or (uchoice=="paper" and Cchoice=="rock")or (uchoice=="scissor" and Cchoice=="paper"):
                print("Computer Value",Cchoice)          # Second Condition
                print("User Value",uchoice)
                print("You Win")
                ucount=ccount+1

        if ucount==ccount:
            print("Final Game Draw...")
            print("User Score",ucount)
            print("Computer Score",ucount)
        elif ucount>ccount:
            print("Final You Win The Game...")
            print("User Score",ucount)
            print("Computer Score",ucount) 
        else:
            print("Computer Win The Game ...")
            print("User Score",ucount)
            print("Computer Score",ucount) 

    else:
        break







