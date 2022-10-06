# 셋(set) : 데이터 중복이 발생되지 않으며, 인덱스가 없으므로 순서제어를 할 수 없다.
import random
lst0 = [60,90,80,70,90,60,100,80]
set0 = {60,90,80,70,90,60,100,80}
print("리스트 : ",lst0, "원소수 : ",len(lst0))
print("셋 : ", set0, "원소수 : ", len(set0))

# 로또 번호 발생기
lst1 = [0,0,0,0,0,0]
for i in range(6):
    lst1[i]=random.randint(1,45)
    print(lst1[i])
set1 = set(lst1)
while True:
    if(len(set1)<6):
        a=random.randint(1, 45)
        set1.add(a)
    if(len(set1)==6):
        lst1=list(set1)
        lst1.sort()
        break
print("로또번호 : ",lst1)

set2 = {10,20,30,40}
set3 = {20,40,60,80}
print(type(set2), set2)
set2.add(60)    # 하나의 원소 추가
set3.add(100)
print(set2)
set2.clear()    # 모든 원소 제거
print(set2)
union1 = set2 | set3        # 합집합 - 컬렉션이 아니면 2진수 연산
union2 = set2.union(set3)
print(union1)
print(union2)
# 교집합 (set2 & set3, set2.intersection(set3)
inter1 = set2 & set3    # 컬렉션이 아니면 2진수 연산
print(inter1)
minus1 = set2 - set3    # 차집합 set2.difference(set3)
print(minus1)

