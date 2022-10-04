# 연산 : 산술, 관계(비교), 논리, 대입 및 할당 연산, 증감연산, 비트 연산...
a=20
b=30
c=60
d=a+b
e=a-b
f=a*b
g=b/a
h=b%a       # 나머지
i=b//a      # 몫
j=b**3      # 거듭제곱
print("a+b=", d)
print("a-b=", e)
print("a*b=", a*b)
print("b/a=", g)
print("나머지 b%a=",h)
print("몫 b//a=",i)
print("거듭제곱 b**5=",j)

# 증감 연산자
# print("a=", a++)    # 출력 20, 실제 a=21 -> 후위연산
print("b=", ++b)    # 출력 31, 실제 b=31 -> 전위연산
a=20
b=30
# print("a=", a--)    # 출력 20, 실제 a=19, 후위연산은 실행문과 같이 쓸수 없음
print("b=", --b)    # 출력 29, 실제 b=29

# 대입(할당) 연산자
a=20
b=30
a+=3                # a가 3씩 증가
a-=3                # a가 3씩 감소
a*=3                # a가 3씩 누승
a/=3                # a가 3씩 누분
a%=3                # a값에 해당하는 값을 3으로 나눈 후에 다시 나머지 저장

a1=30
a2=40
print("a1=",a1)
print("a2=",a2)

# 기존의 자바나 c언어는 데이터를 맞교환하기 위해서는 임시기억장소가 필요
imsi=a1
a1=a2
a2=imsi
print("a1=",a1)
print("a2=",a2)

b1=20;
b2=40;
print("b1=",b1)
print("b2=",b2)
b1,b2=b2,b1         # 교환 연산
print("교환 후")
print("b1=",b1)
print("b2=",b2)
c1, *arr = {20,60,50,40,30}     # 할당 연산
print("c1=",c1)
print("arr=", arr)



