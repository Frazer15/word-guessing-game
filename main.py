# This is a sample Python script.
import random
from english_words import get_english_words_set

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def word_chooser(word_length_list):
    original_word = random.choice(word_length_list) # choosing a word from a list
    original_word = original_word.lower()
    print('   '.join(random.sample(original_word,len(original_word)))) # making the word randomized
    return original_word

def possible_answers(original_word,word_length_list):
    answer_list = []
    matched_words = word_length_list
    original_list = original_word.split()
    sorted_list = original_list.sort()
    for z in matched_words:
        maybe_answer = z.split()
        closer_answer = maybe_answer.sort()
        if sorted_list == closer_answer:
            answer_list.append(z)
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
    else:
        print("my disappointment is immeasurable and my day is ruined")
        continu3 = False

def dict_warehouse(number):
    dict3 = {tuple(['b','o','x']):["box"], tuple(['j','o','y']):['joy'], tuple(['e','y','e']):['eye'],
             tuple(['l','i','p']):["lip"]}
    allDict = {3:dict3}
    return allDict[number]

def smart_dict_way(dict):
    k3y = list(dict.keys())
    randChoice = random.choice(k3y)
    val = dict.get(randChoice)
    randChoice = list(randChoice)
    random.shuffle(randChoice)
    return randChoice, val

def tiers(dict):
    shuffled_word, real_word = smart_dict_way(dict)
    print(shuffled_word)
    guessed_word = input("what is the word on the screen unscrambled")
    a = False
    for z in real_word:
        if guessed_word == real_word:
            print("good job")
            a = True
        else:
            pass
    if a == False:
        print('bad job, the word was ' + ' '.join(real_word))
        continu3 = False

    else:
        pass


def main():
    global continu3
    continu3 = True
    web2lowerset = get_english_words_set(['web2'], lower=True, alpha=True)
    properWordLength = 3  # how long word is
    word_length_list = []
    # Use a breakpoint in the code line below to debug your script.
    while continu3 == True:
        for word in web2lowerset:
            if len(word) == properWordLength:  # checking if proper word length
                word_length_list.append(word)  # adding the words to the list
            else:
                pass
        for z in range(0,5):
            word = word_chooser(word_length_list)
            answer_list = possible_answers(word, word_length_list)
            guess = input("what word is the letters on the screen unscrambled")
            answer_checker(guess, answer_list, properWordLength)
            #word_list = dict_warehouse(properWordLength)
            #new_list = tiers(word_list)
        properWordLength += 1

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
