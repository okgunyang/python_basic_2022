# 튜플(tuple) : 읽기 전용 - immutable(고정) 자료형으로 한 번 데이터가 저장되면 변화되지 않는 자료구조
tp=(124,False,"lee")
print(tp[0])
# tp[1]=True  튜플은 원소의 변경 불가능
print(tp)
lst=list(tp)
print(lst)
lst[1]=True
tp=tuple(lst)
print(tp)
a=tp[0:2]
print(a)
b=tp[:3]
print(b)
c=tp[1:]
print(c)
d=tp[::2]
print(d)
e=tp[::-1]
print(e)

dt1 = [10,20,30,40]
dt2 = (10,20,30,40)
dt3 = (50,60,70,80)
dt4 = dt2 + dt3
print("dt2 : ", dt2)
print("dt3 : ", dt3)
print("dt4 : ", dt4)
lst = dt1 * 3       # 반복
lst2 = [num*3 for num in dt1]   # 내포 : 원래 원소 데이터에 *3을 하여 할당
print(lst)
print(lst2)
tp1 = dt2 * 3                   # 반복
tp2 = [num*3 for num in dt2]    # 튜플의 내포는 원칙적으로 불가능하므로 리스트 내포를 활용
tp2 = tuple(tp2)
first, second, third, fourth = tp2  # 할당
data1, *data2 = tp2
print(tp1)
print(tp2)
print(first, second, third, fourth)
print(data1, data2)