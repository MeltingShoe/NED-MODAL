from globals import *
import os


def join_chars(line):
    out = ''
    for char in line:
        out += char
    return out

        
class card:

    def __init__(self, text):
        self.vert_bar = BAR_CHAR
        self.horz_bar = CARD_CHAR
        self.words = text.split(' ')
        self.lines = []
        self.gen_line()
        self.padded_lines = []
        self.add_pad()
        self.render = []
        self.margined = []
        self.add_blank_lines()
        self.add_bars()
        self.index = 0
        self.add_walls()

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.fancy_box):
            raise StopIteration

        item = self.fancy_box[self.index]
        self.index+=1
        return item

    def __len__(self):
        return len(self.fancy_box)

    def __getitem__(self, key):
        return self.fancy_box[key]

    def set_active(self):
        self.vert_bar = ACTIVE_CHAR
        self.horz_bar = ACTIVE_CHAR

    def gen_line(self):
        line = ''

        for word in self.words:
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

    def add_blank_lines(self):
        out = []
        for i in range(0, CARD_PAD_LINES):
            out.append(' ' * FULL_WIDTH)
        for line in self.padded_lines:
            out.append(line)
        for i in range(0, CARD_PAD_LINES):
            out.append(' ' * FULL_WIDTH)
        self.margined = out

    def add_bars(self):
        out = []
        out.append(self.horz_bar * FULL_WIDTH)
        for line in self.margined:
            out.append(line)
        out.append(self.horz_bar * FULL_WIDTH)
        self.render = out

    def add_walls(self):
        out = []
        for line in self.render:
            out.append(self.vert_bar + line + self.vert_bar)
        out[0] = CORNER_CHAR+out[0][1:-1]+CORNER_CHAR
        out[-1] = CORNER_CHAR+out[-1][1:-1]+CORNER_CHAR
        self.fancy_box = out

        
class card_bucket:

    def __init__(self, card_text):
        self.cards = [card(x) for x in card_text]
        self.lines = []
        self.get_lines()

    def get_lines(self):
        out = []
        for card in self.cards:
            for line in card:
                out.append(line)
        self.lines = out
        return self.lines

def get_longest_len(in_list):
    if type(in_list) == str:
        return len(in_list)
    for item in in_list:
        return get_longest_len(item)

def new_new_main():
    print('new new main\n\n')
    teststr = "huge dicks in my ass dude i be feelin real good, I love stretching!"
    card_text = ['cool good wow yes very good', 'making quite a bit of progress', 'also typin bullshit idk']
    card_text_2 = [teststr, "lorum ipsum sip deez muthafukkin nuts bitch", "cool list entry"]
    bucket = card_bucket(card_text)
    bucket_2 = card_bucket(card_text_2)

    data1 = bucket.lines
    data2 = bucket_2.lines
    h = max(get_longest_len(data1),get_longest_len(data2))
    print(h)
    for i in range(0,h):
        try:
            a = data1[i]
        except:
            a =' ' * (FULL_WIDTH + 2)
        try:
            b = data2[i]
        except:
            b = ' ' *( FULL_WIDTH + 2)
        print(a+b)

def also_main():
    print('also main')
    teststr = "huge dicks in my ass dude i be feelin real good, I love stretching!"
    c1 = [teststr, "lorum ipsum sip deez muthafukkin nuts bitch", "cool list entry"]
    c2 = ['cool good wow yes very good', 'making quite a bit of progress', 'also typin bullshit idk']
    l1 = [card(x) for x in c1]
    l2 = [card(x) for x in c2]
    for line in l1[0].fancy_box:
        print(line)
    

def main():
    print(os.write(1, '\uf164'.encode('utf8')))
    teststr = "huge dicks in my ass dude i be feelin real good, I love stretching!"
    c1 = [teststr, "lorum ipsum sip deez muthafukkin nuts bitch", "cool list entry"]
    c2 = ['cool good wow yes very good', 'making quite a bit of progress', 'also typin bullshit idk']
    print('l1')
    l1 = [card(x) for x in c1]
    l2 = [card(x) for x in c2]
    con = [l1,l2]

    print('<<<<<<<<<<<<<<<<')
    for item in l1[0]:
        print(item)
    c1 = card(teststr)
    out = c1.render
    for line in out:
        print(line)
    print('>>>>>>>>>>>>>>>>>')

    t1 = l1
    l1 = []
    t2 = l2
    l2 = []

    for col in t1:
        for line in col:
            print(line)
            l1.append(line)

    for col in t2:
        for line in col:
            print(line)
            l2.append(line)

    print('\n\n\n')
    for i in range(0,len(l1)):
        try:
            a = l1[i]
        except:
            a = ' '
        try:
            b = l2[i]
        except:
            b = ' '
        delimeter_left = '+' if a[-1] == '-' else '|'
        delimeter_right = '+' if b[-1] == '-' else '|'
        print(a+delimeter_left+delimeter_right+b)

if __name__ == '__main__':
    new_new_main()
