from app.factorial import factorial

def fact1To25() -> None:
    for i in range(0, 26):
        print('fact(', i, ')=', factorial(i))


if __name__ == "__main__":
    fact1To25()