from pwn import *  # pip install pwntools

r = remote('auto.threatsims.com', 5225)


def json_send(hsh):
    print(hsh)
    r.sendline(str(hsh).encode())


def Get():
    return r.recvline(timeout=10).decode()


def askMemo():
    memo = ""
    for _ in range(6):
        red = Get()
        print(red)
        if red[0:4] != "Spam":
            memo = red.split(":")[1].strip()
    json_send(memo)


def askSum():
    red = Get()
    nums = map(int, red.split("+")[:-1])
    res = int(red.split("=")[1])
    res = res - sum(nums)
    json_send(str(res))


def askTax():
    tax = float(Get().split(":")[1].strip())
    earnings = float(Get().split(":")[1].strip())
    json_send(str(round(earnings * tax)))


def askWork():
    hoursWorked = float(Get().split(":")[1].strip())
    rate = float(Get().split(":")[1].strip())
    overtime = float(Get().split(":")[1].strip())
    json_send(str(round(hoursWorked * rate + overtime * rate / 2)))


def json_recv():
    red = Get()
    cnt = 0
    while red != "":
        print(red)
        red = Get()
        if "Can you tell me what the memo is through all this spam?" in red:
            cnt = cnt + 1
            askMemo()
        elif "Can you tell me how much we are missing in this book?" in red:
            cnt = cnt + 1
            askSum()
        elif "Can you tell me how much we owe in taxes this year?" in red:
            cnt = cnt + 1
            askTax()
        elif "Can you write a check for this employee?" in red:
            cnt = cnt + 1
            askWork()
        print(cnt)
        if cnt == 1001:
            print(r.recvuntil("}"))


if __name__ == '__main__':
    for _ in range(10):
        Get()
    json_recv()
