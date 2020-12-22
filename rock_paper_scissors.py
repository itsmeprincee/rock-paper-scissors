from tkinter import *
import tkinter.font as font
import random

player_score = 0
computer_score = 0
options = [("rock",0),("paper",1),("scissors",2)]
def player_choice(player_input):
    global player_score,computer_score
    computer_input = computer_choice()
    player_choice_label.config(text = "Your Selected :"+str(player_input[0]))
    computer_choice_label.config(text = "Computer:"+str(computer_input[0]))
    if(player_input==computer_input):
        game_start.config(text = "Tie")
    elif((player_input[1]-computer_input[1])%3 == 1):
        player_score +=1
        game_start.config(text = "You Won!!")
        player_score_label.config(text = "Your Score :"+str(player_score))
    else:
        computer_score += 1
        game_start.config(text = "Computer Won!!!")
        computer_score_label.config(text="computer Score:"+str(computer_score))



def computer_choice():
    return random.choice(options)





mywindow = Tk()
mywindow.geometry("800x400")
mywindow.title("Rock Paper Scissors Game")
current_font = font.Font(family="Helvetica",size = 20)
#displaying game title
game_title = Label(mywindow,text="Rock Paper Scissors",font = current_font,fg = "red")
game_title.pack()
#diaplaying game description
game_start = Label(mywindow,text ="Let's start the Game!!!",font = font.Font(size = 15),fg = "green",pady = 10)
game_start.pack()
#displaying game options
input_frame = Frame(mywindow)
input_frame.pack()
player_options = Label(input_frame,font = font.Font(size = 12),fg = "grey",text = "Your Options:")
player_options.grid(row = 0,column = 0,pady = 10)
paper_options = Button(input_frame,text = "Rock",font = font.Font(size = 12),bd = 0,bg="silver",pady = 5,padx = 10,width = 12,activebackground = "pink",command = lambda:player_choice(options[0]))
paper_options.grid(row = 1,column = 1,pady = 10,padx = 8)
rock_options = Button(input_frame,text = "Paper",font = font.Font(size = 12),bg = "pink",bd = 0,pady = 5,padx = 10,width = 12,activebackground = "lightblue",command = lambda:player_choice(options[1]))
rock_options.grid(row = 1,column = 2,padx = 8,pady = 10)
scissors_options = Button(input_frame,text ="Scissors",font = font.Font(size = 12),bd = 0,bg = "lightblue",pady = 5,padx = 10,width = 12,activebackground = "silver",command = lambda:player_choice(options[2]))
scissors_options.grid(row = 1,column = 3,padx = 8,pady = 10)
#displaying score and player choice
score = Label(input_frame,text = "Score :",font = font.Font(size = 13),pady = 10,fg = "grey")
score.grid(row = 2,column = 0,pady = 10)
player_choice_label = Label(input_frame,text ="Your Selected :--",font = font.Font(size = 12),fg = "black")
player_choice_label.grid(row = 3,column = 1,pady = 10)
player_score_label = Label(input_frame,text ="Your Score :--",font = font.Font(size = 12),fg = "black")
player_score_label.grid(row = 3,column = 3,pady = 10)
computer_choice_label = Label(input_frame,text = "Computer Selected :--",font = font.Font(size= 12),fg = "black")
computer_choice_label.grid(row=4,column = 1,pady = 8)
computer_score_label = Label(input_frame,text = "computer Score :--",font = font.Font(size = 12))
computer_score_label.grid(row = 4,column = 3,pady = 8)


mywindow.mainloop()