from tkinter import * 
from pytube import YouTube
import os
import time
import sys
import random

global current_player
current_player = 1
global tile_counter
tile_counter = 9
global vs_comp
vs_comp = FALSE

#add a this button pressed or not attribute
global button1_pressed
button1_pressed = FALSE
global button2_pressed
button2_pressed = FALSE
global button3_pressed
button3_pressed = FALSE
global button4_pressed
button4_pressed = FALSE
global button5_pressed
button5_pressed = FALSE
global button6_pressed
button6_pressed = FALSE
global button7_pressed
button7_pressed = FALSE
global button8_pressed
button8_pressed = FALSE
global button9_pressed
button9_pressed = FALSE


root = Tk()
root.geometry('800x800')
root.resizable(0,0)
root.title("Tic Tac Toe Game")

Label(root,text = 'Tic Tac Toe', font = ("Times New Roman", 22, "bold")).place(relx=0.5, rely=0.1, anchor=CENTER)

frame = Frame(root)
frame.grid(pady=250, padx=330)

button1 = Button(frame, text="     ", font = ("Times New Roman", 14, "bold"))
button1.grid(row=0, column=0)

button2 = Button(frame, text="     ", font = ("Times New Roman", 14, "bold"))
button2.grid(row=0, column=1)

button3 = Button(frame, text="     ", font = ("Times New Roman", 14, "bold"))
button3.grid(row=0, column=2)

button4 = Button(frame, text="     ", font = ("Times New Roman", 14, "bold"))
button4.grid(row=1, column=0)

button5 = Button(frame, text="     ", font = ("Times New Roman", 14, "bold"))
button5.grid(row=1, column=1)

button6 = Button(frame, text="     ", font = ("Times New Roman", 14, "bold"))
button6.grid(row=1, column=2)

button7 = Button(frame, text="     ", font = ("Times New Roman", 14, "bold"))
button7.grid(row=2, column=0)

button8 = Button(frame, text="     ", font = ("Times New Roman", 14, "bold"))
button8.grid(row=2, column=1)

button9 = Button(frame, text="     ", font = ("Times New Roman", 14, "bold"))
button9.grid(row=2, column=2)

def button_1_click():
    global current_player
    global button1_pressed
    button1_pressed = TRUE
    global tile_counter
    tile_counter -= 1
    if (button1.cget('text') == "X" or button1.cget('text') == "O"):
        Already_Pressed()
        
    else:
        if (current_player == 1):
                button1.configure(text = "X") 
        else: 
                button1.configure(text = "O") 
        if (current_player == 1):
            current_player = 2
        else:
            current_player = 1 
            button1.configure(command = button_1_click)
            
    if (current_player == 2 and vs_comp == TRUE):
        root.after(500, computer_turn)
        Check_Win()
    else: 
        Check_Win()

def button_2_click():
    global current_player
    global button2_pressed
    button2_pressed = TRUE
    global tile_counter
    tile_counter -= 1
    if (button2.cget('text') == "X" or button2.cget('text') == "O"):
        Already_Pressed()
        
    else:
        if (current_player == 1):
                button2.configure(text = "X") 
        else: 
                button2.configure(text = "O") 
        if (current_player == 1):
            current_player = 2
        else:
            current_player = 1 
            button2.configure(command = button_2_click)
    
    if (current_player == 2 and vs_comp == TRUE):
        root.after(500, computer_turn)
        Check_Win()
    else: 
        Check_Win()

def button_3_click():
    global current_player
    global button3_pressed
    button3_pressed = TRUE
    global tile_counter
    tile_counter -= 1

    if (button3.cget('text') == "X" or button3.cget('text') == "O"):
        Already_Pressed()
        
    else:
        if (current_player == 1):
                button3.configure(text = "X") 
        else: 
                button3.configure(text = "O") 
        if (current_player == 1):
            current_player = 2
        else:
            current_player = 1 
            button3.configure(command = button_3_click) 

    if (current_player == 2 and vs_comp == TRUE):
        root.after(500, computer_turn)
        Check_Win()
    else: 
        Check_Win()
        
def button_4_click():
    global current_player
    global button4_pressed
    button4_pressed = TRUE
    global tile_counter
    tile_counter -= 1

    if (button4.cget('text') == "X" or button4.cget('text') == "O"):
        Already_Pressed()
        
    else:
        if (current_player == 1):
                button4.configure(text = "X") 
        else: 
                button4.configure(text = "O") 
        if (current_player == 1):
            current_player = 2
        else:
            current_player = 1 
            button4.configure(command = button_4_click) 

    if (current_player == 2 and vs_comp == TRUE):
        root.after(500, computer_turn)
        Check_Win()
    else: 
        Check_Win()
        
def button_5_click():
    global current_player
    global button5_pressed
    button5_pressed = TRUE
    global tile_counter
    tile_counter -= 1

    if (button5.cget('text') == "X" or button5.cget('text') == "O"):
        Already_Pressed()
        
    else:
        if (current_player == 1):
                button5.configure(text = "X") 
        else: 
                button5.configure(text = "O") 
        if (current_player == 1):
            current_player = 2
        else:
            current_player = 1 
            button5.configure(command = button_5_click) 
    
    if (current_player == 2 and vs_comp == TRUE):
        root.after(500, computer_turn)
        Check_Win()
    else: 
        Check_Win()
        
def button_6_click():
    global current_player
    global button6_pressed
    button6_pressed = TRUE
    global tile_counter
    tile_counter -= 1

    if (button6.cget('text') == "X" or button6.cget('text') == "O"):
        Already_Pressed()
        
    else:
        if (current_player == 1):
                button6.configure(text = "X") 
        else: 
                button6.configure(text = "O") 
        if (current_player == 1):
            current_player = 2
        else:
            current_player = 1 
            button6.configure(command = button_6_click)

    if (current_player == 2 and vs_comp == TRUE):
        root.after(500, computer_turn)
        Check_Win()
    else: 
        Check_Win()
        
def button_7_click():
    global current_player
    global button7_pressed
    button7_pressed = TRUE
    global tile_counter
    tile_counter -= 1

    if (button7.cget('text') == "X" or button7.cget('text') == "O"):
        Already_Pressed()
        
    else:
        if (current_player == 1):
                button7.configure(text = "X") 
        else: 
                button7.configure(text = "O") 
        if (current_player == 1):
            current_player = 2
        else:
            current_player = 1 
            button7.configure(command = button_7_click)
    
    if (current_player == 2 and vs_comp == TRUE):
        root.after(500, computer_turn)
        Check_Win()
    else: 
        Check_Win()
        
def button_8_click():
    global current_player
    global button8_pressed
    button8_pressed = TRUE
    global tile_counter
    tile_counter -= 1

    if (button8.cget('text') == "X" or button8.cget('text') == "O"):
        Already_Pressed()
        
    else:
        if (current_player == 1):
                button8.configure(text = "X") 
        else: 
                button8.configure(text = "O") 
        if (current_player == 1):
            current_player = 2
        else:
            current_player = 1 
            button8.configure(command = button_8_click)

    if (current_player == 2 and vs_comp == TRUE):
        root.after(500, computer_turn)
        Check_Win()
    else: 
        Check_Win()
        
def button_9_click():
    global current_player
    global button9_pressed
    button9_pressed = TRUE
    global tile_counter
    tile_counter -= 1

    if (button9.cget('text') == "X" or button9.cget('text') == "O"):
        Already_Pressed()
        
    else:
        if (current_player == 1):
                button9.configure(text = "X") 
        else: 
                button9.configure(text = "O") 
        if (current_player == 1):
            current_player = 2
        else:
            current_player = 1 
            button9.configure(command = button_9_click)

    if (current_player == 2 and vs_comp == TRUE):
        root.after(500, computer_turn)
        Check_Win()
    else: 
        Check_Win()
        
def Already_Pressed():
    global tile_counter

    tile_counter += 1 
    pressed_label = Label(root,text = 'This tile is already claimed', font = ("Times New Roman", 30, "bold"))
    pressed_label.place(relx=0.5, rely=0.8, anchor=CENTER)
    root.after(500, pressed_label.destroy)

def Start_Game(): 
    global tile_counter
    tile_counter = 9


    Reset_Board()
    root.title("Tic Tac Toe - 2 Player Versus Mode")
    counter = 0

    button1.configure(command = button_1_click)
    button2.configure(command = button_2_click)
    button3.configure(command = button_3_click)
    button4.configure(command = button_4_click)
    button5.configure(command = button_5_click)
    button6.configure(command = button_6_click)
    button7.configure(command = button_7_click)
    button8.configure(command = button_8_click)
    button9.configure(command = button_9_click)

def Start_Game_Comp():
    global tile_counter
    tile_counter = 9
    global current_player
    global vs_comp

    current_player = 1; 
    
    Reset_Board()
    root.title("Tic Tac Toe - Versus Computer Mode")

    button1.configure(command = button_1_click)
    button2.configure(command = button_2_click)
    button3.configure(command = button_3_click)
    button4.configure(command = button_4_click)
    button5.configure(command = button_5_click)
    button6.configure(command = button_6_click)
    button7.configure(command = button_7_click)
    button8.configure(command = button_8_click)
    button9.configure(command = button_9_click)

    vs_comp = TRUE

def computer_turn():
    global tile_counter
    global current_player

    global button1_pressed
    global button2_pressed
    global button3_pressed
    global button4_pressed
    global button5_pressed
    global button6_pressed
    global button7_pressed
    global button8_pressed
    global button9_pressed

    buttons = {
        1 : button_1_click,
        2 : button_2_click,
        3 : button_3_click,
        4 : button_4_click,
        5 : button_5_click,
        6 : button_6_click,
        7 : button_7_click,
        8 : button_8_click,
        9 : button_9_click
    }
    pressed = {
        
        1 : button1_pressed,
        2 : button2_pressed,
        3 : button3_pressed,
        4 : button4_pressed,
        5 : button5_pressed,
        6 : button6_pressed,
        7 : button7_pressed,
        8 : button8_pressed,
        9 : button9_pressed
    }  
    if (current_player == 2) :
        if tile_counter != 0:
            x = rand_num = random.randint(1,9)
            if (pressed[x] == TRUE):
                x = 1
            if (pressed[x] == TRUE):
                x = 2
            if (pressed[x] == TRUE):
                x = 3 
            if (pressed[x] == TRUE):
                x = 4 
            if (pressed[x] == TRUE):
                x = 5 
            if (pressed[x] == TRUE):
                x = 6 
            if (pressed[x] == TRUE):
                x = 7 
            if (pressed[x] == TRUE):
                x = 8 
            if (pressed[x] == TRUE):
                x = 9  
            buttons[x]()
        if (current_player == 2 and vs_comp == TRUE):
            root.after(1000, computer_turn)
    
   

    
def Check_Win():
    global button_pressed
    button_pressed = FALSE
    if (button1.cget('text') == "X" and button2.cget('text') == "X"  and button3.cget('text') == "X"): 
        Player_1_WON()
        Reset_Board()
        
    elif (button4.cget('text') == "X" and button5.cget('text') == "X"  and button6.cget('text') == "X"):
        Player_1_WON()
        Reset_Board()
        

    elif (button7.cget('text') == "X" and button8.cget('text') == "X"  and button9.cget('text') == "X"):
        Player_1_WON()
        Reset_Board()
        
    
    elif (button1.cget('text') == "X" and button4.cget('text') == "X"  and button7.cget('text') == "X"): 
        Player_1_WON()
        Reset_Board()
        

    elif (button2.cget('text') == "X" and button5.cget('text') == "X"  and button8.cget('text') == "X"):
        Player_1_WON()
        Reset_Board()
        

    elif (button3.cget('text') == "X" and button6.cget('text') == "X"  and button9.cget('text') == "X"):
        Player_1_WON()
        Reset_Board()
        
    
    elif (button1.cget('text') == "X" and button5.cget('text') == "X"  and button9.cget('text') == "X"): 
        Player_1_WON()
        Reset_Board()
        

    elif (button7.cget('text') == "X" and button5.cget('text') == "X"  and button3.cget('text') == "X"): 
        Player_1_WON()
        Reset_Board()
        
    
    

    elif (button1.cget('text') == "O" and button2.cget('text') == "O"  and button3.cget('text') == "O"): 
        Player_2_WON()
        Reset_Board()
        
    elif (button4.cget('text') == "O" and button5.cget('text') == "O"  and button6.cget('text') == "O"):
        Player_2_WON()
        Reset_Board()
        
    elif (button7.cget('text') == "O" and button8.cget('text') == "O"  and button9.cget('text') == "O"):
        Player_2_WON()
        Reset_Board()
    
    elif (button1.cget('text') == "O" and button4.cget('text') == "O"  and button7.cget('text') == "O"): 
        Player_2_WON()
        Reset_Board()
        
    elif (button2.cget('text') == "O" and button5.cget('text') == "O"  and button8.cget('text') == "O"):
        Player_2_WON()
        Reset_Board()
        
    elif (button3.cget('text') == "O" and button6.cget('text') == "O"  and button9.cget('text') == "O"):
        Player_2_WON()
        Reset_Board()
    
    elif (button1.cget('text') == "O" and button5.cget('text') == "O"  and button9.cget('text') == "O"): 
        Player_2_WON()
        Reset_Board()
        
    elif (button7.cget('text') == "O" and button5.cget('text') == "O"  and button3.cget('text') == "O"): 
        Player_2_WON()
        Reset_Board()

    elif (tile_counter == 0):
        draw_label = Label(root,text = 'Draw', font = ("Times New Roman", 30, "bold"))
        draw_label.place(relx=0.5, rely=0.8, anchor=CENTER)
        
        root.after(2000, draw_label.destroy)
        Reset_Board()
    
Button(root,text = 'Start 2 Player mode', font = ("Times New Roman", 14, "bold") ,bg = 'sky blue', padx = 2, command = Start_Game).place(relx=0.3, rely=0.5, anchor=CENTER)
Button(root,text = 'Fight Computer', font = ("Times New Roman", 14, "bold") ,bg = 'sky blue', padx = 2, command = Start_Game_Comp).place(relx=0.7, rely=0.5, anchor=CENTER)


def Reset_Board():
    global current_player
    global vs_comp
    global tile_counter
    tile_counter = 9
    current_player = 1
    vs_comp = FALSE
    root.title("Tic Tac Toe")

    global button1_pressed
    global button2_pressed
    global button3_pressed
    global button4_pressed
    global button5_pressed
    global button6_pressed
    global button7_pressed
    global button8_pressed
    global button9_pressed

    button1_pressed = FALSE
    button2_pressed = FALSE
    button3_pressed = FALSE
    button4_pressed = FALSE
    button5_pressed = FALSE
    button6_pressed = FALSE
    button7_pressed = FALSE
    button8_pressed = FALSE
    button9_pressed = FALSE

    button1.configure(text = "     ", command= NONE)
    button2.configure(text = "     ", command= NONE)
    button3.configure(text = "     ", command= NONE)
    button4.configure(text = "     ", command= NONE)
    button5.configure(text = "     ", command= NONE)
    button6.configure(text = "     ", command= NONE)
    button7.configure(text = "     ", command= NONE)
    button8.configure(text = "     ", command= NONE)
    button9.configure(text = "     ", command= NONE)


    
def Player_1_WON():
    
    win_label = Label(root,text = 'Player 1 Has Won', font = ("Times New Roman", 30, "bold"))
    win_label.place(relx=0.5, rely=0.8, anchor=CENTER)
    root.after(2000, win_label.destroy)

def Player_2_WON():
    if (vs_comp == TRUE):
        win_label = Label(root,text = 'Computer Has Won', font = ("Times New Roman", 30, "bold"))
    else :
        win_label = Label(root,text = 'Player 2 Has Won', font = ("Times New Roman", 30, "bold"))
    win_label.place(relx=0.5, rely=0.8, anchor=CENTER)
    root.after(2000, win_label.destroy)

root.mainloop()
