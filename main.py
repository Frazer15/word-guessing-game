# This is a sample Python script.
import random
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def dict_warehouse(number):
    dict3 = {tuple(['b','o','x']):["box"], tuple['j','o','y']:['joy'], tuple(['e','y','e']):['eye'],
             tuple(['l','i','p']):["lip"]}
    allDict = {3:dict3}
    return allDict[number]

def smart_dict_way(dict):
    k3y = dict.keys()
    val = dict[k3y]
    k3y = list(k3y)
    random.shuffle(k3y)
    return k3y, val

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
    if a == False
        print('bad job, the word was ' + real_word)
    else:
        pass


def main():
    # Use a breakpoint in the code line below to debug your script.
    iterable = 3
    for z in range(0,5):
        word_list = dict_warehouse(iterable)
        new_list = tiers(word_list)
    iterable += 1

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
