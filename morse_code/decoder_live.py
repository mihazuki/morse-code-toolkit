import msvcrt
from .dictionary import char_dict, sign_space


def decode_live():
    print('Use respectively:\n . and - to enter code,\n single space to accept symbol,\n single space to add breaks.\nPress space three times to exit.')

    inputs = ['']
    symbol = ''
    code = ''

    while True:
        while len(inputs) > 3:
            inputs.pop(0)

        if len(inputs) >= 3 and inputs[0] == ' ' and inputs[-1] == ' ' and inputs[-2] == ' ':
            break

        symbol = ''
        code = ''

        while symbol != ' ':
            symbol = msvcrt.getch().decode('utf-8')
            inputs.append(symbol)
            code += f"{symbol}{sign_space}"

        code = code.strip()

        if code in char_dict.values():
            for key, value in char_dict.items():
                if code == value:
                    print(key)
        elif code == '':
            print(' ')
        else:
            print('?')