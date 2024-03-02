from .dictionary import char_dict, sign_space, letter_space, word_space


def clean_data(data):
    trimmed_data = data.strip()
    first_data_list = trimmed_data.split(word_space)
    second_data_list = [data.split(letter_space) for data in first_data_list]
    return second_data_list


def decode():
    print(f'(Check config.json file for proper configuration)\nType code to decode:')

    input_data = input()

    cleaned_list = clean_data(input_data)

    decoded_data = ''

    for word in cleaned_list:
        for char in word:
            if char in char_dict.values():
                for key, value in char_dict.items():
                    if value == char:
                        decoded_data += key
            else:
                decoded_data += '?'
        decoded_data += ' '
    
    decoded_data = decoded_data.strip()

    print(f'Output: {decoded_data}')
