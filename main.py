# This is a sample Python script.
import random
from english_words import get_english_words_set
import tkinter as tk
from functools import partial

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class myGUI:

    def __init__(self, word):
        self.word = word

        print("frazer this code is so cringe")
        print(self)


        self.window = tk.Tk()
        self.window.geometry("500x500")

        self.label = tk.Label(self.window, text="what is the unscrambled word", font=('Comic Sans MS', 12))
        self.label.pack(padx=30,pady=30)

        scrambled_word = '   '.join(random.sample(word,len(word)))
        self.scrambled_word = scrambled_word

        self.word_display = tk.Label(self.window, text= self.scrambled_word,  font=('Comic Sans MS', 15))
        self.word_display.pack(padx=40,pady=40)

        self.entry = tk.Entry(self.window)
        self.entry.bind("<KeyPress>",self.short_cut)
        self.entry.pack(padx=20,pady=20)

        self.check_state = tk.IntVar()

        self.check = tk.Checkbutton(self.window,text="submit",variable=self.check_state,font=('Comic Sans MS',12))

        self.Button = tk.Button(self.window,text="submit",command=self.button_checker,font=('Comic Sans MS',12))
        self.Button.pack(padx =20, pady =20)

        self.window.protocol("WM_DELETE_WINDOW",self.on_closing)
        self.window.mainloop()

    def button_checker(self):
        print("cheese")
        print(self)
        print(self.entry.get())
        return self.entry
        #entered_answer = self.Entry
        #print(entered_answer)
        #answer_checker(entered_answer, )

    def short_cut(self, event):
        if event.keysym == "Return":
            enter_answer = self.entry.get()
            print(enter_answer)

    def on_closing(self):
        print("high score")
        self.window.destroy

    def addAnswer(self, continu3):

        if continu3:
            self.answerDisplay = tk.Label(self.window,text= f"you have correctly guessed that {self.scrambled_word} is {self.Entry}",
                                          font=('Comic Sans MS', 12))
        else:
            self.answerDisplay = tk.Label(self.window,
                                          text=f"I'm sorry but {self.scrambled_word} is actually {self.word[0]}",
                                          font=('Comic Sans MS', 12))

        self.answerDisplay.pack(padx = 40, pady =40 )

def word_chooser(word_length_list):
    original_word = random.choice(word_length_list) # choosing a word from a list
    original_word = original_word.lower()
    #print('   '.join(random.sample(original_word,len(original_word)))) # making the word randomized
    return original_word

def possible_answers(original_word, word_length_list):
    #print("this is original word " + str(original_word))
    answer_list = [] # list of possible answers
    matched_words = word_length_list # list of all words of a certain length
    original_list = [*original_word] # making a list out each letter of the correct word
    original_list.sort() # sorting the correct words list
    for z in matched_words: # going through every word in the list of all of them
        z = z.lower()
        maybe_answer = [*z] # made a list of that instances of the word list
        maybe_answer.sort() # sort the list of that instance of the word list
        if original_list == maybe_answer: # checking if the two sorted lists are the same
            #print("this is original list " + str(original_list))
            #print("this is maybe answer " + str(maybe_answer))
            answer_list.append(z) # if the two sorted lists are the same append the instance to the correct answers list
        else:
            pass
    #print("this is answer list " + str(answer_list))
    return answer_list

def answer_checker(guess, answer_list, properwordlength):
    alpha = False
    for x in answer_list: #going through all answers
        if len(guess) == properwordlength: #check if the input equals the length of the word
            if guess == x: #checking if the word is correct
                alpha = True
            else:
                pass
        else:
            pass
    if alpha:
        print("you have correctly guessed a word")
        continu3 = True
        return continu3

    else:
        print("my disappointment is immeasurable and my day is ruined")
        print("you could have put " + str(answer_list[0]))

        continu3 = False
        return continu3


def main():
    continu3 = True
    web2lowerset = get_english_words_set(['web2'], lower=True, alpha=True)
    properWordLength = 3  # how long word is
    # Use a breakpoint in the code line below to debug your script.
    while continu3 == True:
        word_length_list = []
        for word in web2lowerset:
            if len(word) == properWordLength:  # checking if proper word length
                word_length_list.append(word)  # adding the words to the list
            else:
                pass
        for z in range(0,5):
            word = word_chooser(word_length_list)
            answer_list = possible_answers(word, word_length_list)
            #guess = input("what word is the letters on the screen unscrambled")
            myGUI(word,)
            continu3 = answer_checker(guess, answer_list, properWordLength)
            myGUI.addAnswer(continu3)
            if continu3 == False:
                break
        properWordLength += 1

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
