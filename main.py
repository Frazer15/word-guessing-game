# This is a sample Python script.
import random
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def word_chooser(word_list):
    word = random.choice(word_list)
    randomized_word = []
    for i in word:
        randomized_word.append(i)
    random.shuffle(randomized_word)
    randomized_word = str(randomized_word)
    wacky_word = randomized_word.strip(",'[]")
    return wacky_word, word

def tiers(word_list):
    shuffled_word, real_word = word_chooser(word_list)
    print(shuffled_word)
    guessed_word = input("what is the word on the screen unscrambled")
    if guessed_word == real_word:
        print("good job")
    else:
        print('bad job, the word was ' + real_word)

def main():
    # Use a breakpoint in the code line below to debug your script.
    iterable = 0
    word_list_3 = ["box","joy","eye","lip","rot","yet","cot","you","few","tie","men","gin","mix"]
    while iterable < 5:
        tiers(word_list_3)
        iterable += 1

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
