"""Ch.5 Hash Tables"""
from typing import List


def freq_table(names: List[str]) -> dict:
    """Creates frequency table from list of names"""
    result = {}
    for name in names:
        if result.get(name):
            result[name] += 1
        else:
            result[name] = 1
    return result

if __name__ == '__main__':
    my_names = ['foo', 'bar', 'baz', 'baz']
    print(freq_table(my_names))
