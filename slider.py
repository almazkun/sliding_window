"""This is example of the Closing Sliding Window"""


def main():
    slider("qwertyuiop")


def number_of_win(s, win_size):
    n = len(s) - win_size + 1
    return n


def get_sub(s, start, win_size):
    ns = s[start : start + win_size]
    return ns


def _all(s):
    win_size = len(s)
    while win_size > 0:
        for i in range(number_of_win(s, win_size)):
            sub = get_sub(s, i, win_size)
            yield sub
        win_size -= 1


def slider(s):
    for s in _all(s):
        print(s)


if __name__ == "__main__":
    main()
