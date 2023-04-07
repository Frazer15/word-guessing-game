    # import tkinter as tk
    # import random
    #
    # def button_checker():
    #     global word
    #     guess = entry.get()
    #     right_or_wrong = tk.StringVar()
    #     if guess == word:
    #         right_or_wrong.set("You are correct very good")
    #     else:
    #         pass
    #
    # def short_cut():
    #
    #
    # def main():
    #     window = tk.Tk()
    #     word = "can"
    #
    #     label = tk.Label(window, text="what is the unscrambled word", font=('Comic Sans MS', 12))
    #     label.pack(padx=30,pady=30)
    #
    #
    #     scrambled_word = tk.StringVar()
    #     scrambled_word.set( '   '.join(random.sample(word,len(word))))
    #     #self.scrambled_word = scrambled_word
    #
    #     word_display = tk.Label(window, textvariable= scrambled_word,  font=('Comic Sans MS', 15))
    #     word_display.pack(padx=40,pady=40)
    #
    #     global entry
    #     entry = tk.Entry(window)
    #     entry.bind("<KeyPress>",short_cut)
    #     entry.pack(padx=20,pady=20)
    #
    #     check_state = tk.IntVar()
    #
    #     check = tk.Checkbutton(window,text="submit",variable=check_state,font=('Comic Sans MS',12))
    #
    #     Button = tk.Button(window,text="submit",command=button_checker,font=('Comic Sans MS',12))
    #     Button.pack(padx =20, pady =20)
    #
    #     window.mainloop()
    # main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
from tkinter import *
from tkinter import ttk
import random as rnd
from english_words import get_english_words_set


class word:
    web2lowerset = get_english_words_set(['web2'], lower=True, alpha=True)
    proper_word_length = 3
    def __init__(self,really_big_number):
        if really_big_number == 6 or really_big_number == 0:
            word_length_list = []
            for x in word.web2lowerset:
                if len(x) == word.proper_word_length:  # checking if proper word length
                    word_length_list.append(x.lower())  # adding the words to the list
                else:
                    pass
        original_word = rnd.choice(word_length_list)  # choosing a word from a list
        #print("this is " + str(original_word)+ "and" + str(type(original_word)))
        #original_word = original_word.lower()

        self.original_word = original_word
        self.word_length_list = word_length_list

    def __str__(self):
        s = self.original_word
        s = s.lower()
        scrambled_word = '   '.join(rnd.sample(s, len(s)))
        # print("this is "+ scrambled_word + "and type is " + str(type(scrambled_word)))
        return scrambled_word

    def possible_answers(self,original_word, word_length_list):
        # print("this is original word " + str(original_word))
        answer_list = []  # list of possible answers
        matched_words = self.word_length_list  # list of all words of a certain length
        original_list = [*self.original_word]  # making a list out each letter of the correct word
        original_list.sort()  # sorting the correct words list
        for z in matched_words:  # going through every word in the list of all of them
            z = z.lower()
            maybe_answer = [*z]  # made a list of that instances of the word list
            maybe_answer.sort()  # sort the list of that instance of the word list
            if original_list == maybe_answer:  # checking if the two sorted lists are the same
                # print("this is original list " + str(original_list))
                # print("this is maybe answer " + str(maybe_answer))
                answer_list.append(z)  # if the two sorted lists are the same append the instance to the correct answers list
            else:
                pass
        # print("this is answer list " + str(answer_list))
        return answer_list

    # def scrambler(self):
    #     # choosing a word from a list
    #     # print('   '.join(random.sample(original_word,len(original_word)))) # making the word randomized
    #     s = self.original_word
    #     s = s.lower()
    #     scrambled_word = '   '.join(rnd.sample(s, len(s)))
    #     #print("this is "+ scrambled_word + "and type is " + str(type(scrambled_word)))
    #     return scrambled_word



def main():
    global really_big_number
    really_big_number = 0
    big_variable = word(really_big_number)
    print(big_variable)
    window = Tk()

    scrambled_word = StringVar()

    #words = ["orf", "acb", "ilp"]

    lab = Label(window, text="what is the scrambled word")
    lab.pack(padx=10,pady=10)

    entry_field = Entry()
    entry_field.pack(padx=10,pady=10)

    scrambled_word.set(big_variable)

    def stand_in():

        guess = entry_field.get()

        entry_field.delete(0, "end")



        if guess == big_variable:
            print("congrats")
            scrambled_word.set(big_variable = word(really_big_number))

            really_big_number += 1
        else:
            pass
        window.update

    BUTTon = Button(window, text="submit", command=stand_in)
    BUTTon.pack(padx=10, pady=10)

    scrambled_lab = Label(window, textvariable=scrambled_word)
    scrambled_lab.pack(padx=10,pady=10)

    window.title("guessing game")
    window.geometry("500x500")

    window.mainloop()

main()

# def phrase_so_far(letter, inPhrase, inSet) -> list:
#     phraseToDisplay = ""
#     letterOccurrenceCount = 0
#     punct = [" ", ",", ".", "?", "!"]
#     vowels = ["a", "e", "i", "o", "u"]
#
#     if letter in inSet:
#         letterOccurrenceCount = 0
#     else:
#         if letter in inPhrase:
#             for char in inPhrase:
#                 if char == letter:
#                     letterOccurrenceCount += 1
#         if letter in vowels:
#             letterOccurrenceCount *= -1
#
#         inSet.add(letter)
#
#     for char in inPhrase:
#         if char in punct:
#             phraseToDisplay += char
#         elif char in inSet:
#             phraseToDisplay += char
#         else:
#             phraseToDisplay += "*"
#
#     outList = [phraseToDisplay.upper(), letterOccurrenceCount]
#     return outList
#
#
# # Converts the set of guessed letters to a string of uppercase letters
# def set_to_string(inSet) -> str:
#     outStr = ""
#     for e in inSet:
#         outStr += e.upper()
#     return outStr
#
#
# # Global variable that keeps track of how much money you have so far
# myWinnings = 0
#
#
# # The main application
# def main():
#     phrase = "Lorem ipsum dolor sit amet, consectetur adipiscing elit,"
#     guessedLetters = set()  # creates an empty set; {} creates an empty dictionary
#     global myWinnings
#
#     window = Tk()
#     # https://www.askpython.com/python-modules/tkinter/stringvar-with-examples
#     displayPhrase = StringVar()
#     displayLetters = StringVar()
#     displaySpin = StringVar()
#     displayCount = StringVar()
#     displayAmount = StringVar()
#
#     displayPhrase.set(phrase)
#     displayLetters.set(set_to_string(guessedLetters))
#
#     # https://www.pythontutorial.net/tkinter/tkinter-label/
#     lbl1  = ttk.Label(window, text="Enter a letter: ")
#     lbl2a = ttk.Label(window, text="Letters already entered: ")
#     lbl3a = ttk.Label(window, text="Unknown phrase so far: ")
#     lbl4a = ttk.Label(window, text="Wheel spin: ")
#     lbl4c = ttk.Label(window, text="Number of occurrences: ")
#     lbl5a = ttk.Label(window, text="Your total so far: ")
#
#     # https://www.pythontutorial.net/tkinter/tkinter-entry/
#     t1 = ttk.Entry()
#
#     # Updates labels on output window
#     def update_label():
#         global myWinnings
#         letter = t1.get()
#         # clears the entry box
#         t1.delete(0, 'end')
#
#         # updates guessedLetters with the new letter that was guessed
#         newList = phrase_so_far(letter, phrase.lower(), guessedLetters)
#
#         showGuessedLetters = set_to_string(guessedLetters)   # string containing letters already guessed
#         displayLetters.set(showGuessedLetters)
#
#         phraseToDisplay = newList[0]      # the phrase revealing successfully guessed letters so far
#         displayPhrase.set(phraseToDisplay)
#
#         occurrenceCount = newList[1]      # the number of times letter occurs in the phrase
#         displayCount.set(str(occurrenceCount))
#
#         print(phraseToDisplay + ": " + letter.upper(), 'occurs', occurrenceCount, 'times')
#
#         spinResult = spin_wheel()
#         print('result of wheel spin:', spinResult)
#
#         if spinResult < 0:        # bankrupt: myWinnings is zeroed out
#             myWinnings = 0
#         else:                     # adds to myWinnings
#             if occurrenceCount < 0:
#                 myWinnings -= 100
#             else:
#                 myWinnings += spinResult * occurrenceCount
#         print('my winnings so far:', myWinnings, '\n')
#
#         displaySpin.set(str(spinResult))
#         displayAmount.set(str(myWinnings))
#         window.update()
#
#     # Spins the wheel, and returns a monetary amount, 0 (lose a turn), or -1 (bankrupt)
#     def spin_wheel() -> int:
#         wheel = [0, -1, 100, 100, 100, 100, 100, 100, 100, 100, 200, 200, 200, 200, 500, 500, 1000]
#         n = len(wheel)
#         i = rnd.randint(0, n-1)
#         return wheel[i]
#
#     # https://www.pythontutorial.net/tkinter/tkinter-button/
#     b1 = ttk.Button(window, text="Guess", command=update_label)
#     b1.pack()
#
#     # this only runs once to initialize the displayed phrase
#     myList = phrase_so_far("", phrase.lower(), guessedLetters)
#     initialStr = myList[0]
#     displayPhrase.set(initialStr)
#     showGuessedLetters = set_to_string(guessedLetters)
#     displayLetters.set(showGuessedLetters)
#
#     # update labels on output window with text to display
#     lbl2b = ttk.Label(window, textvariable=displayLetters, font=("Courier", 14, "bold"))
#     lbl3b = ttk.Label(window, textvariable=displayPhrase, font=("Courier", 14, "bold"))
#     # set up labels lbl4b, lbl4d, and lbl5b corresponding to labels lbl4a, lbl4c, and lbl5a above
#     lbl4b = ttk.Label(window, textvariable=displaySpin, font=("Courier", 14, "bold"))
#     lbl4d = ttk.Label(window, textvariable=displayCount, font=("Courier", 14, "bold"))
#     lbl5b = ttk.Label(window, textvariable=displayAmount, font=("Courier", 14, "bold"))
#
#     # set positions of labels, text entry box, and button on output window
#     dx = -10
#     dy = -2
#     lbl1.place(x=20, y=20)
#     t1.place(x=150, y=15)
#     lbl2a.place(x=20, y=60)
#     lbl2b.place(x=180+dx, y=60+dy)
#     lbl3a.place(x=20, y=100)
#     lbl3b.place(x=180+dx, y=100+dy)
#     lbl4a.place(x=20, y=140)
#     lbl4b.place(x=180+dx, y=140+dy)
#     lbl4c.place(x=250, y=140)
#     lbl4d.place(x=400, y=140+dy)
#     lbl5a.place(x=20, y=180)
#     lbl5b.place(x=180+dx, y=180+dy)
#     b1.place(x=325, y=220)
#
#     # set title and size of output window
#     window.title('Wheel of Fortune')
#     window.geometry("825x260+5+5")
#     window.resizable(False, False)
#
#     # https://realpython.com/python-gui-tkinter/
#     window.mainloop()
#     print("Thanks for playing ... goodbye!")
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     main()
#main()