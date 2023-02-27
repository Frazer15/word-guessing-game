import random
s="abcdef123"
print(''.join(random.sample(s,len(s))))

from english_words import get_english_words_set
web2lowerset = get_english_words_set(['web2'], lower=True, alpha=True)
print(web2lowerset)

properWordLength = 3 #how long word is
word_length_list = [] #going to store words of a certain length

for word in web2lowerset:
    if len(word) == properWordLength: #checking if proper word length
        word_length_list.append(word) #adding the words to the list
    else:
        pass

def answer_checker(guess):
    if len(guess) == properWordLength:
        if guess in word_length_list:
            print("you have correctly guessed a word")
        else:
            print("my disappointment is immeasurable and my day is ruined")
    else:
        pass
