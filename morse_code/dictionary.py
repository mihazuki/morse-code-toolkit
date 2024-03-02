import json


char_dict = {}

sign_space = 0
letter_space = 0
word_space = 0

with open('config.json') as file:
    data = json.load(file)
    sign_space = ' ' * data['space_between_sign']
    letter_space = ' ' * data['space_between_letter']
    word_space = ' ' * data['space_between_words']

char_dict = {'A': f'.{sign_space}-',
            'B': f'-{sign_space}.{sign_space}.{sign_space}.',
            'C': f'-{sign_space}.{sign_space}-{sign_space}.',
            'D': f'-{sign_space}.{sign_space}.',
            'E': f'.',
            'F': f'.{sign_space}.{sign_space}-{sign_space}.',
            'G': f'-{sign_space}-{sign_space}.',
            'H': f'.{sign_space}.{sign_space}.{sign_space}.',
            'I': f'.{sign_space}.',
            'J': f'.{sign_space}-{sign_space}-{sign_space}-',
            'K': f'-{sign_space}.{sign_space}-',
            'L': f'.{sign_space}-{sign_space}.{sign_space}.',
            'M': f'-{sign_space}-',
            'N': f'-{sign_space}.',
            'O': f'-{sign_space}-{sign_space}-',
            'P': f'.{sign_space}-{sign_space}-{sign_space}.',
            'Q': f'-{sign_space}-{sign_space}.{sign_space}-',
            'R': f'.{sign_space}-{sign_space}.',
            'S': f'.{sign_space}.{sign_space}.',
            'T': f'-',
            'U': f'.{sign_space}.{sign_space}-',
            'V': f'.{sign_space}.{sign_space}.{sign_space}-',
            'W': f'.{sign_space}-{sign_space}-',
            'X': f'-{sign_space}.{sign_space}.{sign_space}-',
            'Y': f'-{sign_space}.{sign_space}-{sign_space}-',
            'Z': f'-{sign_space}-{sign_space}.{sign_space}.',
            '1': f'.{sign_space}-{sign_space}-{sign_space}-{sign_space}-',
            '2': f'.{sign_space}.{sign_space}-{sign_space}-{sign_space}-',
            '3': f'.{sign_space}.{sign_space}.{sign_space}-{sign_space}-',
            '4': f'.{sign_space}.{sign_space}.{sign_space}.{sign_space}-',
            '5': f'.{sign_space}.{sign_space}.{sign_space}.{sign_space}.',
            '6': f'-{sign_space}.{sign_space}.{sign_space}.{sign_space}.',
            '7': f'-{sign_space}-{sign_space}.{sign_space}.{sign_space}.',
            '8': f'-{sign_space}-{sign_space}-{sign_space}.{sign_space}.',
            '9': f'-{sign_space}-{sign_space}-{sign_space}-{sign_space}.',
            '0': f'-{sign_space}-{sign_space}-{sign_space}-{sign_space}-'}

print(sign_space)