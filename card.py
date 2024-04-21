from globals import *


def join_chars(line):
    out = ''
    for char in line:
        out += char
    return out

        
class card:

    def __init__(self, text):
        print('init dis bitch')
        self.words = text.split(' ')
        self.lines = []
        self.gen_line()
        print('exit init')
        self.padded_lines = []
        self.add_pad()

    def gen_line(self):
        line = ''

        for word in self.words:
            print(line)
            if len(line) + len(word) >= LIST_WIDTH:
                self.lines.append(line)
                line = word
            elif len(line)==0:
                line = word
            else:
                line += ' ' + word

        if len(line) > 0:
            self.lines.append(line)

    def add_pad(self):
        t1 = []
        for line in self.lines:
            t1.append(' ' + line) 
        t2 = []
        for line in t1:
            diff = FULL_WIDTH - len(line) 
            t2.append(line + ' ' * diff)
        self.padded_lines = t2


def main():
    teststr = "huge dicks in my ass dude i be feelin real good, I love stretching!"
    c1 = card(teststr)
    print(c1.padded_lines)
    print(len(c1.lines[-1]))

if __name__ == '__main__':
    main()
