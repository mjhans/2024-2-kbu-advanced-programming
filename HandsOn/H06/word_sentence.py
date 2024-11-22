import re
import reprlib
from collections import Counter

RE_WORD = re.compile('\w+')
file_name = "Lorem.txt"

#count_dict = {}
count_dict = Counter()

class Sentence:
    def __init__(self, file_name):
        self.file_name = file_name
    def __iter__(self):
        with open(self.file_name, 'r') as fp:
            for line in fp: # fp는 파일 객체이면서 문단단위의 iterable
                for match in RE_WORD.finditer(line):
                    yield match.group()
    def __repr__(self):
        return f"Senetence ({reprlib.repr(self.file_name)})"

if __name__ == "__main__":
    s = Sentence("Lorem.txt")
    c = Counter(s)  
    print(c)