import msvcrt
from .dictionary import char_dict, word_space


def encode_live():
    print('Enter characters (press space two times to quit): ')

    inputs = []

    while True:
        char = msvcrt.getch().decode('utf-8')
        upper_char = char.upper()

        inputs.append(upper_char)

        while len(inputs) > 2:
            inputs.pop(0)

        if inputs[0] == ' ' and inputs[-1] == ' ':
            break
        else:
            if upper_char in char_dict.keys():
                print(char_dict[upper_char])
            elif upper_char == ' ':
                print(word_space)
            else:
                print('?')