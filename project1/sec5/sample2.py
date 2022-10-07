# 3 개의 단어를 입력받아 첫 글자만 추출하여 약자를 출력하는 프로그램
# 반복문과 입력/출력/슬라이싱문 이용
# 입력예시
# 첫번째 단어 : Korea
# 두번째 단어 : Baseball
# 세번째 단어 : Organization
# 출력예시
# KBO
in1 = input("첫번째 단어 :")
in2 = input("두번째 단어 :")
in3 = input("세번째 단어 :")
print(in1[0]+in2[0]+in3[0])

# 클래스로 처리되는 경우

class WordAbbr:
    word = ""

    def inputWord(self):
        in1 = input("첫번째 단어 :")
        in2 = input("두번째 단어 :")
        in3 = input("세번째 단어 :")
        self.word = in1[0] + in2[0] + in3[0]
        return self.word

    def printWord(self):
        print(self.word)

w = WordAbbr()
w.inputWord()
w.printWord()
