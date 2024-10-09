import random

Voc_f = "C:/Users/AKNot/OneDrive/Documents/gre_vocab_words.csv"

def count_lines(filename):
    with open(filename, 'r') as file:
        return len(file.readlines())

def get_line(filename, line_number):
    with open(filename, 'r') as file:
        content = file.readlines()
        return content[line_number]

def write_line(filename, line_number, seen, correct, word, definition):
    with open(filename, 'r') as file:
        content = file.readlines()
    content[line_number] = str(seen) +"," + str(correct) +"," + word +"," + definition
    with open(filename, 'w') as file:
        file.writelines(content)

def get_word(filename, line_number):
    line = get_line(filename, line_number)
    return line.split(',')[2]

def get_def(filename, line_number):
    line = get_line(filename, line_number)
    return line.split(',')[3]
 
def get_seen_count(filename, line_number):
    line = get_line(filename, line_number)
    return line.split(',')[0]  

def get_correct_count(filename, line_number):
    line = get_line(filename, line_number)
    return line.split(',')[1]      

def reset_count(filename, line_number):
    write_line(filename, line_number, 0, 0, get_word(Voc_f, line_number), get_def(Voc_f, line_number))

def inc_seen_count(filename, line_number):
    write_line(filename, line_number, int(get_seen_count(Voc_f, line_number))+1, 
    get_correct_count(Voc_f, line_number), get_word(Voc_f, line_number), get_def(Voc_f, line_number))

def inc_correct_count(filename, line_number):
    write_line(filename, line_number, get_seen_count(Voc_f, line_number), 
    int(get_correct_count(Voc_f, line_number))+1, get_word(Voc_f, line_number), get_def(Voc_f, line_number))


def main():
    i = ' '
    line_count = count_lines(Voc_f)
    while i!='q':
        line = random.randint(0,line_count-1)
        print(get_word(Voc_f, line))
        print("(q) quit, any other letter to continue     ")
        i = input()
        if i=='q':
            break
        print(get_def(Voc_f, line))
        inc_seen_count(Voc_f, line)
        print("(c) correct, (q) quit, anything else for incorrect")
        i = input()
        if i=='c':
            inc_correct_count(Voc_f, line)


if __name__ == '__main__':
    main()