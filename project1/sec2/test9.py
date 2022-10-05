# 반복문 : 해당 조건이나 상황이 만족될 때 반복 수행
i=tot=0
while(i<=10):
    tot+=i      # tot=tot+i
    i+=1        # i=i+1
print("0~10 합계 : ", tot)

# 1~100 짝수의 합계
i=tot=0
while(i<=100):
    tot+=i
    i+=2
print("0~100 짝수의 합계 : ", tot)

i=tot=0
while(i<=100):
    if(i%2==0):
        tot+=i
    i+=1
print("0~100 짝수의 합계2 : ", tot)

i=tot=0
while(i<=100):
    if(i%2!=0):
        continue
    tot+=i
    i+=1
print("0~100 짝수의 합계3 : ", tot)

# 무한 루프
i=1
tot=0
while True:
    if(i>100):
        break
    tot+=i
    i+=2
print("0~100 홀수의 합계 : ", tot)

# 3의 배수의 합계
i=tot=0
while(i<=100):
    tot+=i
    i+=3
print("0~100 3의 배수의 합계 : ", tot)

i=tot=0
while(i<=100):
    if(i%3==0):
        tot+=i
    i+=1
print("0~100 3의 배수의 합계2 : ", tot)