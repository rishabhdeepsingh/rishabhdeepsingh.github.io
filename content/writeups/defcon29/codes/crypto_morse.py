from pwn import *  # pip install pwntools

CODE = {'A': '.-', 'B': '-...', 'C': '-.-.',
        'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..',
        'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-',
        'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',

        '0': '-----', '1': '.----', '2': '..---',
        '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..',
        '9': '----.',

        ' ': ' ',

        ', ': '--..--', '.': '.-.-.-',
        '?': '..--..', '/': '-..-.', '-': '-....-',
        '(': '-.--.', ')': '-.--.-'
        }

CODE_REVERSED = {value: key for key, value in CODE.items()}


def to_morse(s):
    return ' '.join(CODE.get(i.upper()) for i in s)


def from_morse(s):
    return ''.join(CODE_REVERSED.get(i) for i in s.split())


r = remote('159.203.98.188', 2345)


def recv():
    while True:
        _s = r.recv().decode()
        if _s == '\n':
            return None
        print(from_morse(_s), end=" ")


def send(hsh):
    req = to_morse(hsh)
    print(req)
    r.sendline(req.encode())


if __name__ == '__main__':
    print(to_morse('y'))
    recv()
    send('Y')
    recv()
    send('1838')
    recv()
    send('CQD')
    recv()

# TELEGRAPH PUT IT IN BRACES THEN  PUT THE  LETTERS TS AT  THE  BE G I N I NG  O F I T  BE F O R E T H E B R A E S [*] Closed connection to 159.203.98.188 port 2345
