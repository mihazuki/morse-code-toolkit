from morse_code.decoder import decode
from morse_code.decoder_live import decode_live
from morse_code.encoder import encode
from morse_code.encoder_live import encode_live


def main():
    print('Welcome to Morse Coder')

    while True:
        print('1. Decoder')
        print('2. Decoder Live')
        print('3. Encoder')
        print('4. Encoder Live')
        print('5. Exit')

        input_number = input()

        if input_number == '1':
            decode()
        if input_number == '2':
            decode_live()
        if input_number == '3':
            encode()
        if input_number == '4':
            encode_live()
        if input_number == '5':
            break
        else:
            pass

if __name__ == "__main__":
    main()