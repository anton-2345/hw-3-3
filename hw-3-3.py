choose = input("Введите название курса")
s = []
s_new = []
try:
    with open('input.txt', 'r') as text_file:
        for line in text_file:
            line = line.strip()
            line = line.replace(' ', '')
            line = line.rstrip(',')
            name, courses = line.split(':')
            s = courses.split(',')
            for i in s:
                if i == choose:
                    s_new.append(name)
    if len(s_new) == 0:
        print('This course does not exist')
    else:
        print(s_new)
except FileNotFoundError:
    print('This file does not exist, please come back later')