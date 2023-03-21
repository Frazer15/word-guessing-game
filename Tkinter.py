import tkinter as tk

#import colorama
# look at after and after cancel in tkinter
# alot of stuff copied from him https://www.youtube.com/watch?v=ibf5cx221hk
import time

class myGUI:

    def __init__(self,word2lowerset,word_length_list):
        self.window = tk.Tk()

        self.label = tk.Label(self.window, text="what is the unscrambled word", font=('Comic Sans MS', 12))
        self.label.pack(padx=30,pady=30)

        self.Entry = tk.Entry(self.window)
        self.Entry.bind("<KeyPress>",self.short_cut)
        self.Entry.pack(padx=20,pady=20)

        self.check_state = tk.IntVar()

        self.check = tk.Checkbutton(self.window,text="submit",variable=self.check_state,font=('Comic Sans MS',12))

        self.Button = tk.Button(self.window,text="submit",command=self.button_checker,font=('Comic Sans MS',12))
        self.Button.pack(padx =20, pady =20)

        self.window.protocol("WM_DELETE_WINDOW",self.on_closing)
        self.window.mainloop()

    def button_checker(self):
        entered_answer = self.Entry.get()
        answer_checker(entered_answer,)

    def short_cut(self, event):
        if event.keysym == "Return":
            pass

    def on_closing(self):
        print("high score")
        self.root.destroy



window = tk.Tk()

window.geometry("350x300")

window.title("Word guessing Game") #gives title

display_question = tk.Label(text="what is the unscrambled word") #asks question with parameters
display_question.grid(row = 3, column =3)

submit_word = tk.Button(text="submit")
submit_word.grid(row = 7, column = 3)

guessed_word = Entry(window) #basically the input function
guessed_word.grid(row = 5,column = 3)

frame = Frame(window)
frame.pack

window.mainloop()