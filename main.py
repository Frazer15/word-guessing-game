
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import random

from pygame import mixer
from tkinter import *
from tkinter import ttk
import random as rnd
from english_words import get_english_words_set
import asyncio
import queue
import math
import csv  #https://www.geeksforgeeks.org/saving-text-json-and-csv-to-a-file-in-python/#

class word:
    #global proper_word_length
    global word_length_list

    web2lowerset = get_english_words_set(['web2'], lower=True, alpha=True)
    proper_word_length = 3
    def __init__(self,really_big_number,word_length_list):
        if really_big_number % 6 == 0:
            word_length_list = []
            if really_big_number != 0:
                word.proper_word_length += 1
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
        matched_words = word_length_list  # list of all words of a certain length
        original_list = [*original_word]  # making a list out each letter of the correct word
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
def possible_answers(original_word, word_length_list):
    # print("this is original word " + str(original_word))
    answer_list = []  # list of possible answers
    matched_words = word_length_list  # list of all words of a certain length
    original_list = [*original_word]  # making a list out each letter of the correct word
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

async def are_you_fast(window):
    window.after(10000,print("you are so slow"))
    window.after(2000,window.destroy())





def main():
    global word_length_list
    word_length_list = []

    global really_big_number
    really_big_number = 0

    #global proper_word_length


    global answers
    answers = []

    global truth
    truth = False

    global after_var
    after_var = None

    timer_start  = 20

    current_mode = "easy mode"

    my_font = "Jokerman"

    fields = []


    global score
    score = 0

    scrabble_dict = {"a": 1, "b": 4, "c": 4, "d": 2, "e": 1, "f": 4,
                     "g": 3, "h": 3, "i": 1, "j": 10, "k": 5, "l": 2,"m": 4,
                     "n": 2, "o": 1, "p": 4, "q": 10, "r": 1,  "s": 1,
                     "t": 1, "u": 2, "v": 5, "w": 4, "x": 8, "y": 3,"z": 10}
    #global absolute

    print("This is a check" + str(really_big_number))
    #big_variable = word(really_big_number)
    #print(big_variable)
    window = Tk()

    the_queue = queue.Queue()

    big_variable = word(really_big_number,word_length_list)
    print(big_variable)

    if really_big_number % 6 == 0 and really_big_number != 0 and really_big_number != 1:
        word_length_list = big_variable.word_length_list

    elif really_big_number == 0:
        word_length_list = big_variable.word_length_list
    else:
        pass

    filler = ""


    #answers = word.possible_answers(filler,big_variable.original_word,big_variable.word_length_list)
    answers = possible_answers(big_variable.original_word, big_variable.word_length_list)
    print("This is a check" + str(really_big_number))


    scrambled_word = StringVar()

    counting_down = IntVar()
    counting_down.set(timer_start)

    string_score = IntVar()
    string_score.set(score)

    integer = IntVar()

    mode = StringVar()


    #words = ["orf", "acb", "ilp"]

    lab = Label(window, text="what is the scrambled word", font=(my_font,20))
    lab.place(x=320,y=20)

    #stop_watch = Label(window, textvariable=counting_down)
    #stop_watch.pack(padx=10)

    time_word = Label(window,text="timer:", font=(my_font,20))
    time_word.place(x=850,y=10)

    time_piece = Label(window, textvariable=counting_down, font=(my_font,20))
    time_piece.place(x=940,y=10)

    scrambled_lab = Label(window, textvariable=scrambled_word, font=(my_font,20))
    scrambled_lab.place(x=450,y=70)

    entry_field = Entry(window,font=(my_font),width=20)
    entry_field.place(x=340,y=130)

    score_word = Label(window, text="score:", font=(my_font,20) )
    score_word.place(x=20,y=10)

    actual_score = Label(window, textvariable=string_score, font=(my_font,20))
    actual_score.place(x=110,y=10)

    scrambled_word.set(str(big_variable))

    print("This is a check" + str(really_big_number))

    ran_num = random.randint(1,100)

    if ran_num == 100:
        mixer.init()
        mixer.music.load(r"C:\Users\FrazerSmith\Downloads\mixkit-bells-of-mystery-581.wav")
        mixer.music.play()

    # def timer(display_watch):
    #     counting_down.set(str(display_watch))
    #     window.update()
    #
    # def queue_adder():
    #     for x in range(1, 11):
    #         absolute = abs(x - 11)
    #         display_watch = "amount of time left" + str(absolute)
    #         the_queue.put(timer(display_watch))
    #
    #
    #     the_queue.put(None)
    #
    #
    # def function_of_functions():
    #     x = 0
    #     while x < 10:
    #         message = window.after(1000, the_queue.get())
    #
    #         if message == None:
    #             window.after(10000, print("you are so slow"))
    #             try:
    #                 window.after(2000, window.destroy())
    #             except:
    #                 print("it is over")




    # async def are_you_fast():
    #     window.after(10000, print("you are so slow"))
    #     window.after(2000, window.destroy())
    # def timers():
    #     #for x in range(1, 11):
    #     absolute = abs(x - 11)
    #     counting_down.set(str(absolute))
    #     window.update()

    #asy = asyncio.create_task(are_you_fast())
    #absolute = 10
    # for x in range(1, 11):
        #window.after(1000, timers)
    #queue_adder()
    #function_of_functions()
    def timer(x):
        global truth
        global after_var
        print(truth)
        if truth == True:
            truth = False
            x = 20

            #window.reset(after_var)
        x -= 1
        if x == 0:
            window.destroy()

        counting_down.set(str(x))
        window.update()

        after_var = window.after(1000, lambda :timer(x))
        return after_var

    #def timer_stop():


    # if "normal" == window.state:
    #     for x in range(100):
    #         window.after(1000)
    #         print(x)
    #         integer.set(x)
    #         exerciseLabel = Label(window, textvariable=integer)
    #         exerciseLabel.pack(padx=10,pady=10)
    after_var = timer(timer_start)

    print(after_var)


    def stand_in():
        global really_big_number
        global answers
        global after_var
        global score

        print("This is a check" + str(really_big_number))
        guess = entry_field.get()

        entry_field.delete(0, "end")
        print("this is a really big number" + str(really_big_number))

        print("this is halloween " + str(answers) + " on " + str(type(answers)))

        power = len(guess)
        base_score = 10 ** power

        q = False

        for x in answers:

            if guess == x:
                print("congrats")

                #is_cancelled = asy.cancel()

                #print("was cancelled " + str(is_cancelled))
                #scrabble_dict ={"a":1,"b":4,"c":4,"d":2,"e":1,"f":4,"g":3,"h":3,"i":1,"j":10,"k":5,"l":2,"m":4,
                                #"n":2,"o":1,"p":4,"q":10,"r":1,"s":1,"t":1,"u":2,"v":5,"w":4,"x":8,"y":3,"z":10}

                q = True

                print(after_var)
                window.after_cancel(after_var)

                timer_start = 20

                big_variable = word(really_big_number,word_length_list)

                after_var = timer(timer_start)

                scrambled_word.set(big_variable)

                really_big_number += 1

                answers = possible_answers(big_variable.original_word, big_variable.word_length_list)

                fancy = Label(window, text="congrats you don't suck")
                fancy.place(x=350,y=400)

                window.after(1500, fancy.destroy)

                # this is how lambda works lambda:congratulations(fancy)





            else:
                print(answers)
                # mixer.init()
                # mixer.music.load(r"C:\Users\FrazerSmith\Downloads\womp-womp.mp3")
                # mixer.music.play()


        if q == True:
            print("yes")
            for z in guess:
                add_to = scrabble_dict[z]
                add_more = add_to * (10 ** (power - 1))
                base_score += add_more
                score += base_score
                string_score.set(score)
                mixer.init()
                mixer.music.load(r"C:\Users\FrazerSmith\Downloads\mixkit-arcade-score-interface-217.wav")
                mixer.music.play()
        else:
            print("no")
            mixer.init()
            mixer.music.load(r"C:\Users\FrazerSmith\Downloads\womp-womp.mp3")
            mixer.music.play()
            for z in guess:
                add_to = scrabble_dict[z]
                add_more = add_to * (10 ** (power - 2))
                base_score += add_more
                score -= base_score
                string_score.set(score)

        window.update

        truth = True

    def lam(current_modde):
        global current_mode
        nonlocal my_font
        nonlocal timer_start
        if current_modde == "easy mode":
            my_font = "wingdings"
            timer_start = 10
            current_mode = "hard mode"




        else:
            my_font = "Jokerman"
            timer_start = 20
            current_mode = "easy mode"

        window.update()

    def stand_inn(event):
        global really_big_number
        global answers
        global after_var
        global score

        print("This is a check" + str(really_big_number))
        guess = entry_field.get()

        entry_field.delete(0, "end")
        print("this is a really big number" + str(really_big_number))

        print("this is not halloween " + str(answers) + " on " + str(type(answers)))

        power = len(guess)
        base_score = 10 ** power

        q = False

        for x in answers:

            if guess == x:
                print("congrats")

                # is_cancelled = asy.cancel()

                # print("was cancelled " + str(is_cancelled))

                q = True

                print(after_var)
                window.after_cancel(after_var)

                timer_start = 20

                big_variable = word(really_big_number, word_length_list)

                after_var = timer(timer_start)

                scrambled_word.set(big_variable)

                really_big_number += 1

                answers = possible_answers(big_variable.original_word, big_variable.word_length_list)

                fancy = Label(window, text="congrats you don't suck")
                fancy.place(x=350,y=400)

                window.after(1500, fancy.destroy)

                # this is how lambda works lambda:congratulations(fancy)

            else:
                print("answer key " + str(answers))
                # mixer.init()
                # mixer.music.load(r"C:\Users\FrazerSmith\Downloads\womp-womp.mp3")
                # mixer.music.play()


        print(base_score)
        print(score)
        if q == True:
            print("yes")
            for z in guess:
                add_to = scrabble_dict[z]
                add_more = add_to * (10 ** (power - 1))
                base_score += add_more
                score += base_score
                string_score.set(score)
                mixer.init()
                mixer.music.load(r"C:\Users\FrazerSmith\Downloads\mixkit-arcade-score-interface-217.wav")
                mixer.music.play()
        else:
            print("no")
            mixer.init()
            mixer.music.load(r"C:\Users\FrazerSmith\Downloads\womp-womp.mp3")
            mixer.music.play()
            for z in guess:
                add_to = scrabble_dict[z]
                add_more = add_to * (10 ** (power - 2))
                base_score += add_more
                score -= base_score
                string_score.set(score)

        #score += base_score
        #string_score.set(score)
        window.update

        truth = True

    BUTTon = Button(window, text="submit", command=stand_in)
    BUTTon.place(x=470,y=175)

    mode.set(current_mode)


    mode_selection = Button(window,textvariable=mode, command=lambda: lam(current_mode))
    mode_selection.place(x=460,y=210)

    window.bind('<Return>', stand_inn)

    #scrambled_lab = Label(window, textvariable=scrambled_word)
    #scrambled_lab.pack(padx=10,pady=10)

    #after_var = timer(timer_start)

    window.title("guessing game")
    window.geometry("1000x500")

    window.mainloop()

main()

#Saving
#
# path = r"C:\Users\FrazerSmith\Downloads\user_info.txt"
# baa = False
# try:
#     myFile = open(path, "x")
#     myFile.close()
#     x = "the input"
#     redLines =""
# except:
#     myFile = open(path, "r")
#     redLines = myFile.readlines()
#     for z in redLines:
#         if "the Input" in z:
#             myFile.truncate()
#             myFile.close
#             baa = True
#             redLines.remove(z)
#             newList = list(z.strip(" "))
#             player_highscore = newList[1]
#             word_length = newList[2]
#         else:
#             pass
#     if baa == False:
#         myFile.close()
#
#
# newEntry = "Name" + " " + "Highscore" + " " + "wordLength"
# redLines.append(newEntry)
# myFile = open(path, "w")
# myFile.writelines(redLines)
# myFile.close()