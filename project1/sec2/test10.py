# for 반복 : for~in, for~not in, for~in~range
data = [90,80,100,60,70]
a=tot=0
for i in data:
    a+=1
    tot+=i
    print("점수 : ", i)
print("총점 : ", tot)
print("평균 : ", float(tot / a))

jum = [(100,80,70),(90,100,80),(80,90,60),(90,100,100)]
for (kor, eng, mat) in jum:
    tot = kor+eng+mat
    avg = float(tot / 3)
    hak = ""
    if(avg>=90):
        hak = "A"
    elif(avg>=80):
        hak = "B"
    elif(avg>=70):
        hak = "C"
    elif(avg>=60):
        hak = "D"
    else:
        hak = "F"
    print("총점 : ", tot)
    print("평균 : ", avg)
    print("학점 : ", hak)

lst = [80, 90, 70, 100, 75]
i=0
for pt in lst:
    i+=1
    if(pt<80):
        continue    
    print("%d 번째 학생~! 점수가 %d점으로 합격을 축하합니다.~!" % (i, pt))

#  range(start[, end][, step]) : 해당 범위의 값을 자동으로 발생

b1 = range(10)      # 0~9
for i in b1:
    print(i)

b2 = range(0, 6)    # 0~5
for i in b2:
    print(i)

b3 = range(0, 10, 2)
for i in b3:
    print(i)

tot=0
for i in range(1, 101):     # i는 1~100 변화됨
    tot+=i
print("1~100 합계 : ", tot)

data1 = [40,65,70,90,85]        # list
data2 = [num * 2 for num in data1]      # for~in을 list에 내포
data3 = [num * 2 for num in data1 if num%2==0]   # for~in을 list에 내포
print(data2)
print(data3)
