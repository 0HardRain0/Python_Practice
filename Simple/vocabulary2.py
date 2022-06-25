in_file = open('vocabulary.txt', 'r')

for line in in_file:
    data = line.strip().split(": ")
    korean_meaning = data[0]
    english_word = data[1]
    user_answer = input("%s: " % korean_meaning)

    if user_answer == english_word:
        print("맞았습니다!")

    else:
        print("아쉽습니다. 정답은 %s입니다." % english_word)


in_file.close()
