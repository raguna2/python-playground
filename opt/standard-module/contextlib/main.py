from contextlib import ExitStack
from pathlib import Path
from urllib.request import urlopen
from contextlib import contextmanager

here = Path(__file__).parent
INPUT_DIR = here / 'input'


@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()


def main():
    with closing(urlopen('http://www.python.org')) as page:
        for line in page:
            print(line)
    # a_file = INPUT_DIR / 'aaa.csv'
    # b_file = INPUT_DIR / 'bbb.csv'
    # with ExitStack() as stack:
    #     file_a = stack.enter_context(a_file.open(mode='r', encoding='utf-8'))
    #     file_b = stack.enter_context(b_file.open(mode='r', encoding='utf-8'))
    #
    #     for a in file_a:
    #         print(a)
    #     for b in file_b:
    #         print(b)

        # close_files = stack.pop_all().close
        # print(close_files)




if __name__ == '__main__':
    main()
