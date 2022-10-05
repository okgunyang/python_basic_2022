# sec2 > test7.py
su1 = int(input("점수 입력 : "))
print("점수 : ", su1)
# 제어문 : 조건문(if), 반복문(while, for), 기타 제어문(break, continue)
# 프로그램 블록 : if, while, for, function,... 에서 다른 언어와 같이 {}를
# 사용하지 않으며, 탭으로 들여쓰기하여 해당 블록을 구분한다.
# if(조건식) :
#       해당 조건이 참일 때 실행할 문장
# else :
#       해당 조건이 거짓일 때 실행할 문장
if(su1>=80):
    print("합격")
else:
    print("불합격")

# if(조건식1):
#       실행문1
# elif(조건식2):
#       실행문2
# elif(조건식3):
#       실행문3
# ....
# else :
#       실행문n

if(su1>=90):
    print("A")
elif(su1>=80):  # 90미만~80이상
    print("B")
elif(su1>=70):  # 80미만~70이상
    print("C")
elif(su1>=60):  # 70미만~60이상
    print("D")
else :          # 60미만
    print("F")