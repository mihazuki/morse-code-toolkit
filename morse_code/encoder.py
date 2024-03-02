import re
from .dictionary import char_dict, letter_space, word_space


def clean_data(data):
    upper = data.upper()
    return re.sub(r'\s+', ' ', upper)


def encode():
    print('Type text to encode:')

    input_data = input()

    cleaned_data = clean_data(input_data)
    cleaned_list = list(cleaned_data)
    encoded_message = ''

    for index, character in enumerate(cleaned_list):
        if index < len(cleaned_list) - 1:
            if character in char_dict.keys():
                if cleaned_list[index + 1] == ' ':
                    encoded_message += f'{char_dict[character]}'
                else:
                    encoded_message += f'{char_dict[character]}{letter_space}'
            elif character == ' ':
                encoded_message += word_space
            else:
                if cleaned_list[index + 1] == ' ':
                    encoded_message += f'?'
                else:
                    encoded_message += f'?{letter_space}'
        else:
            if character in char_dict.keys():
                encoded_message += f'{char_dict[character]}'
            else:
                encoded_message += f'?{letter_space}'


    print(f'Output: {encoded_message}')