import json
import re
import time
import random

class Word_finder:
    def __init__(self):
        self.name = "Paul"


    def random_choice(self):
        interact_user = True
        while interact_user:
            answer = input("Chose language:\nnative - 1\nforeign - 2\n> ")
            if answer == 'q':
                break
            elif answer == "1":
                Word_finder.random_choice_native_lang(self)
            elif answer == "2":
                Word_finder.random_choice_foreign_lang(self)
    
    def random_choice_native_lang(self):
        dict_words = Word_finder.get_json_with_words(self)
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
    
    def random_choice_foreign_lang(self):
        dict_words = Word_finder.get_json_with_words(self)
        keys_words = list(dict_words.keys())
        
        amount_of_words = len(keys_words)
        while amount_of_words != 0:
            amount_of_words -= 1
            random_key = random.choice(keys_words) 
            keys_words.pop(keys_words.index(random_key))
            answer = input(f"{random_key}: ")
            correct = 0
            incorrect = 0
            if answer == 'q':
                break
            else:
                list_of_words = dict_words[random_key].split()
                if answer in list_of_words:
                    correct += 1
                    print('')
                elif answer not in list_of_words:
                    incorrect += 1
                    print("")
                    print(dict_words[random_key])
        print(f"correct {correct}\nincorrect {incorrect}")
        #amount_of_words = len(keys_words)
        #correct = 0
        #incorrect = 0
        #while  amount_of_words != 0:
        #    amount_of_words -= 1
        
        #    # Delete word, which was randomly chosen
        #    
        #
        #    elif answer == random_key:
        #    elif answer != random_key:
        #        incorrect += 1
        #        print(" ")
        #        print(random_key)
        #print(f"correct {correct}\nincorrect {incorrect}")
    
    
    def get_json_with_words(self):
        try:
            with open('mydick.json',"r") as file:
                words_from_file = json.load(file)
                return words_from_file
        except (FileNotFoundError):
            print("No such file")
    
    def show_all_words(self):
        """Show all words without sort"""
        words = Word_finder.get_json_with_words(self)
        for key,value in words.items():
            print(f'{key} - {value}')
    
    def show_alphabetic_words(self):
        words = Word_finder.get_json_with_words(self)
        sorted_words = sorted(words.items())
        for word_n_translate in sorted_words:
            print(f'{word_n_translate[0]} - {word_n_translate[1]}')
    
    def show_particular_word(self):
        interaction = True
        while interaction: 
            wanted_word = input("Please enter word: ")
            if wanted_word == 'q':
                interaction = False
                #break
            words = Word_finder.get_json_with_words(self)
            pattern = f'({wanted_word})' #+(_)?[0-9]*$'
            for key,value in words.items():
                match = re.match(pattern, key)
                if match:
                    #match_list.append(match.group())
                    #print(f"{match.group()}")
                    print(f"{key} {value}")
                else:
                    list_translated_words = value.split()
                    
                    for translated_word in list_translated_words:
                        match = re.match(pattern, translated_word)
                        if match:
                            print(f'{value} {key}')
    
                    #list_translated_words = value.split()
                    ##print(list_translated_words)
                    #if wanted_word in list_translated_words:
                    #    print(f"{value} {key}")    
                    #counter = len(list_translated_words)
                    #for translated_word in list_translated_words:
                    #        
                    #    while counter != 0:
                    #        counter -= 1   
                    #        index = list_translated_words.index(translated_word)
    
                    #        print(index)
                    #        word = list_translated_words.pop(index)
                    #        match = re.match(pattern, word)
                    #        if match:
                    #            print(f"{value} {key}")
                    #        elif not match:
                    #            print('no')
                    #        #    continue
        #print(f'сов#падение ключей в списке  log/pas:\n{match_list}')
wf = Word_finder()
#wf.show_all_words()
#wf.show_alphabetic_words()
#wf.show_particular_word()
#wf.random_choice_native_lang()
#wf.random_choice_foreign_lang()
wf.random_choice()

# Add some coments
