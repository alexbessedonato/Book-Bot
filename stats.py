from typing import TypedDict

class CharacterCount(TypedDict):
    char: str
    num: int

def get_num_words(text: str)-> int:
    words = text.split()
    return len(words)

def get_num_characters(text: str)-> dict[str, int]:
    character_dict: dict = {}
    for character in text:
        character = character.lower()
        if character in character_dict:
            character_dict[character] += 1
        else:
            character_dict[character] = 1
    return character_dict

def sort_on(CharacterCount):
    return CharacterCount["num"]

def dictionary_to_list(dictionary):
    list_of_dictionaries = []
    for entry in dictionary:
        new_dict = {
            "char": entry,
            "num": dictionary[entry]
            }
        list_of_dictionaries.append(new_dict)
    list_of_dictionaries.sort(reverse=True, key=sort_on)
    return list_of_dictionaries

