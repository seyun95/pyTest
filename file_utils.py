# coding=utf-8
en_list = []
kr_list = []


def read_from_dictionary():
    # english=한글 형식
    #f = open("/Users/joshua/Workroom/dic.txt", "r")
    f = open("dic.txt", "r")
    while True:
        line = f.readline()
        if not line:
            break
        line_list = line.split('=')
        en_list.append(line_list[0])
        kr_list.append(line_list[1].strip("\n"))
        print(line)
    f.close()


read_from_dictionary()
print("en_list: ", en_list)
print("kr_list: ", kr_list)

if kr_list[0] == "테스트":
    print("bingo!!")
else:
    print("why not?", kr_list[0])