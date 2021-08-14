from pwn import *  # pip install pwntools

r = remote('auto.threatsims.com', 4224)

PI = 3.14

questions = 0


def Get():
    return r.recvline(timeout=5).decode()


def json_recv():
    global questions
    if questions == 1000 + 1:
        print(r.recvuntil("}"))

    red = Get()
    while red != "":
        print(red)
        if red[0] == "Q":
            questions = questions + 1
        red = Get()
        if "Find" in red:
            return red


def json_send(hsh):
    r.sendline(str(hsh).encode())


def Find(x: str):
    print(x)
    val = int(x.split(" ")[-1].strip())
    res = -1
    if "Find the Volume of A Semi-Sphere with a Radius" in x:
        res = 2 * PI * val * val * val / 3
    if "Find the Area of A Square with a Side Length of" in x:
        res = val * val
    if "Find the Volume of A Sphere with a Radius of" in x:
        res = 4 * PI * val * val * val / 3
    if "Find the Area of A Circle with a Radius" in x:
        res = PI * val * val
    if "Find the Area of A Semi-Circle with a Radius" in x:
        res = PI * val * val / 2
    if "Find the Volume of A Cube with a Side Length" in x:
        res = val * val * val
    return round(res)


if __name__ == '__main__':

    received = json_recv()

    while True:
        _res = Find(received)
        print(_res)
        json_send(_res)
        received = json_recv()
