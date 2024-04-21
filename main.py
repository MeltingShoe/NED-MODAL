LIST_WIDTH = 20
LEFT_PAD = 1
CARD_PAD_LINES = 1
TEXT_WIDTH = LIST_WIDTH - (2 * LEFT_PAD) 
BORDER_CHAR = '-'
CARD_CHAR = '='
SELECT_CHAR = '*'

container = [['dank','do stuff', 'lick toads and do drugs', 'make bois pp hard'],['finish project manager', 'celebrate by smokin weed'],['make a cool stream'],['stream setup','tmux','nerdfont']]

first_list_render = []
max_len = LIST_WIDTH - (LEFT_PAD * 2)

blank_line = (" " * LIST_WIDTH)
padding = " " * LEFT_PAD
line_break = BORDER_CHAR * LIST_WIDTH
first_list_render.append(line_break)

    #render
def render_inner_list(card_text):
    rendered_line = []
    #for card in card_text:
    rendered_line.append(render_card_char())
    rendered_line.append(render_card_pad())
    rendered_line.append(final_make_text(card_text))
    rendered_line.append(render_card_pad())
    rendered_line.append(render_card_char())
    #out = unpack_nested_list(rendered_line)
    return rendered_line


def unpack_nested_list(in_list):
    out = []
    for item in in_list:
        if type(item) == list:
            for i in unpack_nested_list(item):
                out.append(i)
        elif type(item) == str: 
            out.append(item)
        else:
            print('PANIC')
            print(item)
    return out

def render_card_char():
    return CARD_CHAR * LIST_WIDTH

def render_card_pad():
    lines = []
    for i in range(0,CARD_PAD_LINES):
        lines.append(blank_line)
    return lines

def get_list_len(val):
    count = 0
    for word in val:
        count += len(word)
        count += 1
    count -= 1
    return count

def render_text(card_text):
    out = []
    if len(card_text) <= TEXT_WIDTH:
        return [right_pad(card_text)]
    else:
        line = []
        for word in card_text.split(' '):
            count = 0
            for word2 in line:
                count += len(word2)
            if get_list_len(line) <= TEXT_WIDTH:
                line.append(word)
            else:
                out.append(line)
                line = [word]
        c1 = 0
        for item in out:
            for w in item:
                c1 += 1
        diff = len(card_text.split(' ')) - c1
        line = []
        for i in range(0,abs(diff)):
            line.append(card_text.split(' ')[-(i+1)])
        line.reverse()
        out.append(line)
        o2=[]
        for item in out:
            o2.append(right_pad(item))
        out=o2

    return out

def right_pad(line):
    if type(line) == list:
        out = ''
        for item in line:
            out += item
            out += ' '
        line = out
    if type(line) is not str:
        print('PAAAAAAAAANIIIIIIIIIIIIIIIIC')
        exit()
    out = line
    gap = LIST_WIDTH - len(out)
    while gap > 0:
        out += ' '
        gap = LIST_WIDTH - len(out)
    return out

def tts(text): # (text to string)
    if type(text) == str:
        return text
    out = ''
    print(':)')
    for word in text:
        out += word
        out += ' '
    out = out [:-1]
    while len(out) < LIST_WIDTH:
        out += ' '
    return out

def final_make_text(card_text):
    a = render_text(card_text)
    lines = []
    for line in a:
        lines.append(tts(line))
    return lines

def render_full_list(card_list):
    out = []
    for card in card_list:
        out.append(render_inner_list(card))
    out = unpack_nested_list(out)
    return out

def combine_lines(lol): #(l)ist (o)f (l)ists    x3
    out = []
    for card in lol[0]:        
        out.append([card])
    for item in lol[1:]:
        for count, card in enumerate(item):
            out[count].append(card)
    return out

def make_all_lists(container):
    out = []
    for item in container:
        out.append(render_full_list(item))
    return combine_lines(out)

def make_border(lines):
    out = ''
    for line in lines:
        outline = ''
        for item in line:
            outline += '|'
            outline += item
        outline += '|'
        out += outline
        out += '\n'
    return out
        
def main():
    print('we runnin main dude')
    txt = 'This is a super god damn long ass string like look at this shit it is for sure going to go over many lines'
    test_nest = [  [ 1 , 3, 5], ['a','b','c'],[7,6,5],[1,9,2]]
    lit = make_all_lists(container)
    lit = make_border(lit)
    print(lit)
    #bussin = render_full_list(container[0])
    #for sus in bussin:
        #print(sus)
    #dim1 = unpack_nested_list(test_nest)
    #print(dim1)
    #coolgood = render_inner_list(container[0][2])
    #for cool in coolgood:
        #print(cool)
    #fancy_words = final_make_text(container[0])
    #fancy_words = render_text(txt)
    #print(tts(fancy_words[0]))
    #print(fancy_words)
    #for line in fancy_words:
        #print(line)

if __name__ == '__main__':
    main()
