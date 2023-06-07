import json
from os import walk
from pylanguagetool import api


def fill_in_dictionary():
    user_interaction = True
    new_words_list = []
    while user_interaction:    
        word = input("Please insert word: ")
        if word == 'q':
            user_interaction = False
            break
    
        translation = input("Please insert translation: ")
        if translation == 'q':
            user_interaction = False
            break
        new_word = {word:translation}
        if new_word:
            new_words_list.append(new_word)
        #else:
        #    pass
    #return new_words_list
    save_words_into_json(new_words_list)


def check_repeated_words(main_dict, list_of_dictionaries):
    '''
    function sort words if there're repited words so
    it just add another defenition to existing word
    '''
    # list main dict keys
    keys_main_dict = main_dict.keys()
    # get dict from list
    for dictionary in list_of_dictionaries:
        # get it key obj. like kinda list
        key = dictionary.keys()
        # get key from list if not it doesn't work  
        for key_word in key:    
            # check if key in main dict keys
            if key_word in keys_main_dict:
                # if is add another defenition to already existing word
                main_dict[key_word] += ', '+(dictionary[key_word])
            else:
                # if not just add another {word:defenition} into main dictionary
                main_dict.update(dictionary)
                #print(False)
    return main_dict

def save_words_into_json(list_dict_words):
    try: 
        with open('mydick.json',"r") as file:
            list_old_words = json.load(file)
        a = check_repeated_words(list_old_words,list_dict_words,)
        #for word in list_dict_words:
        #   list_old_words.update(word) 
        #dictionary['saved_words'].update(new_word)
        print (a)
        with open('mydick.json','w') as file:
            json.dump(a, file, indent=4, ensure_ascii=False)
            
    except (FileNotFoundError):
        dictionary = {}
        for word in list_dict_words:
           dictionary.update(word) 
        with open('mydick.json', 'w') as file:
            json.dump(dictionary, file, indent=4, ensure_ascii=False)
    
def check(checking_word):
    """returns possible word after errors checking as a string"""
    check=api.check(
    checking_word,
    api_url='https://languagetool.org/api/v2/',
    lang='en-US',
    )
    #with open('test_grammar_check.json','w') as file:
    #    json.dump(check, file, indent=4, ensure_ascii=False)
    # 
    #with open('test_grammar_check.json',"r") as file:
    #    check_result = json.load(file)
    try:
        for result in check["matches"][0]["replacements"]:
            return(result["value"])
    except(KeyError, IndexError):
        print("Probably there is no errors")

fill_in_dictionary()




















