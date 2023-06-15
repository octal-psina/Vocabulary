import json
import re
import time
import random

#def timer():
    

def random_choice():
    dict_words = get_json_with_words()
    keys_words = list(dict_words.keys())
    amount_of_words = len(keys_words)
    correct = 0
    incorrect = 0
    while  amount_of_words != 0:
        amount_of_words -= 1
        random_key = random.choice(keys_words)
        # Delete word, which was randomly chosen
        keys_words.pop(keys_words.index(random_key))
        answer = input(f"{dict_words[random_key]}: ")
        if answer == 'q':
            break
        elif answer == random_key:
            correct += 1
            print('')
        elif answer != random_key:
            incorrect += 1
            print(" ")
            print(random_key)
    print(f"correct {correct}\nincorrect {incorrect}")



def get_json_with_words():
    try:
        with open('mydick.json',"r") as file:
            words_from_file = json.load(file)
            return words_from_file
    except (FileNotFoundError):
        print("No such file")

def show_all_words():
    """Show all words without sort"""
    words = get_json_with_words()
    for key,value in words.items():
        print(f'{key} - {value}')

def show_alphabetic_words():
    words = get_json_with_words()
    sorted_words = sorted(words.items())
    for word_n_translate in sorted_words:
        print(f'{word_n_translate[0]} - {word_n_translate[1]}')

def show_particular_word():
    interaction = True
    while interaction: 
        wanted_word = input("Please enter word: ")
        if wanted_word == 'q':
            interaction = False
            #break
        words = get_json_with_words()
        pattern = f'^({wanted_word})' #+(_)?[0-9]*$'
        for key,value in words.items():
            match = re.match(pattern, key)
            if match:
                #match_list.append(match.group())
                #print(f"{match.group()}")
                print(f"{key} {value}")
            else:
                match = re.match(pattern, value)
                if match:
                    print(f"{value} {key}")
                else:
                    pass
    #print(f'совпадение ключей в списке  log/pas:\n{match_list}')

#show_all_words()
#show_alphabetic_words()
#show_particular_word()
random_choice()
