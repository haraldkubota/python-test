# Read a file line by line
# Via a generator
from memory_profiler import profile


def return_a_line(fh: object) -> str:
    while True:
        s=fh.readline()
        if s == '':
            break
        yield s


@profile
def main():
    with open('./largefile.txt', 'r') as fh:
        n = 1

        # Read the whole file and split lines (remove EOL)
        # lines = fh.read().split('\n')

        # Read all lines (keep EOL)
        # lines = fh.readlines()

        # for i in lines:
        for i in return_a_line(fh):
            # print(f'Line {n}: {i}')
            n = n + 1
            if n > 100:
                break

        print(f'I got {n} lines')


main()