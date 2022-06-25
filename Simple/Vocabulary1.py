out_file = open('vocabulary.txt', 'w')


while True:
    # 영어 단어 입력
    english_word = input("영어 단어를 입력하세요: ")

    # "q" 입력 시 끝
    if english_word == "q":
        break

    # 한국어 뜻 입력
    korean_meaning = input("한국어 뜻을 입력하세요: ")

    # "q" 입력 시 끝
    if korean_meaning == "q":
        break
    out_file.write("%s: %s\n" % (english_word, korean_meaning))


out_file.close()
