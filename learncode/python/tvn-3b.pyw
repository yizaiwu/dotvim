from Tkinter import *
import pygame.mixer

number_correct = 0
number_wrong   = 0

def play_correct_sound():
    global number_correct
    number_correct = number_correct + 1
    correct_s.play()

def play_wrong_sound():
    global number_wrong
    number_wrong = number_wrong + 1
    wrong_s.play()

app = Tk()
app.title("TVN Game Show")
app.geometry('300x110+200+100')

sounds = pygame.mixer
sounds.init()

correct_s = sounds.Sound("correct.wav")
wrong_s   = sounds.Sound("wrong.wav")

lab = Label(app, text='When you are ready, click on the buttons!', height=3)
lab.pack()

lab1 = Label(app, textvariable=number_correct)
lab1.pack(side='left')

lab2 = Label(app, textvariable=number_wrong)
lab2.pack(side='right')

b1 = Button(app, text="Correct!", width=10, command = play_correct_sound)
b1.pack(side='left', padx=10, pady=10)

b2 = Button(app, text="Wrong!", width=10, command = play_wrong_sound)
b2.pack(side='right', padx=10, pady=10)

app.mainloop()

print(str(number_correct) + " were correctly answered.")
print(str(number_wrong) + " were answered incorrectly.")


