import random
s="abcdef123"

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

original_word = random.choice(word_length_list) # choosing a word from a list
original_word = original_word.lower()
print('   '.join(random.sample(original_word,len(original_word)))) # making the word randomized

def possible_answers:
    answer_list = []
    matched_words = word_length_list
    original_list = original_word.split("")
    sorted_list = original_list.sort()
    for z in matched_words:
        maybe_answer = z.split()
        closer_answer = maybe_answer.sort()
        if sorted_list == closer_answer:
            answer_list.append(z)

def answer_checker(guess):
    if len(guess) == properWordLength: #check if the input equals the length of the word
        if guess == original_word: #checking if the word is correct
            print("you have correctly guessed a word")
        else:
            print("my disappointment is immeasurable and my day is ruined")
    else:
        pass
