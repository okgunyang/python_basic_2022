# if와 복수 조건
jum = [90,80,100]   # 파이썬의 열거형(이더레이터)
# 모든 점수가 80점 이상이면, 합격
if(jum[0]>=80 and jum[1]>=80 and jum[2]>=80):
    print("합격")
else:
    print("불합격")

# 세 점수 중에서 하나라도 90점 이상이면, "과목우수", 아니면, ""(공란)
if(jum[0]>=90 or jum[1]>=90 or jum[2]>=90):
    print("과목우수")
else:
    print("")

# 학점 : 평균이
# 90점 이상이면, A, +96:A+, +93:A0, 92~90:A-
# 80점 이상이면, B, +86:B+, +83:B0, 82~80:B-
# 70점 이상이면, C, +76:C+, +73:C0, 72~70:C-
# 60점 이상이면, D
# 60점 미만이면, F
avg = float((jum[0]+jum[1]+jum[2])/3)
print("평균 : ", avg)
# 중첩 if(if문 안에 if문이 발생)
if(avg>=90):
    if(avg>=96):
        print("A+")
    elif(avg>=93):
        print("A0")
    else:
        print("A-")
elif(avg>=80):
    if(avg>=86):
        print("B+")
    elif(avg>=83):
        print("B0")
    else:
        print("B-")
elif(avg>=70):
    if(avg>=76):
        print("C+")
    elif(avg>=73):
        print("C0")
    else:
        print("C-")
elif(avg>=60):
    print("D")
else:
    print("F")

su = 87
hak=['F','F','F','F','F','F','D','C','B','A','A']
res = hak[su//10]
print("학점 : ", res)
