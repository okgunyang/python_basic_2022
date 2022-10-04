# 비교연산 : >,>=,<,<=,==,!=
a=40
b=30
c=70
print("a>b : ", a>b)        # 크다, 초과, 후
print("a>=b : ", a>=b)      # 크거나 같다, 이상, 이후
print("a<b : ", a<b)        # 작다, 미만, 전
print("a<=b : ", a<=b)      # 작거나 같다, 이하, 이전
print("a==b : ", a==b)      # 같다, 동일, 일치
print("a!=b : ", a!=b)      # 같지 않다, 상이, 불일치

# 논리 연산자
# and
print("a>b && b>c : ", (a>b and b>c))
print("a<b && b>c : ", (a<b and b>c))
print("a>b && b<c : ", (a>b and b<c))
print("a<b && b<c : ", (a<b and b<c))
# or
print("a>b || b>c : ", (a>b or b>c))
print("a<b || b>c : ", (a<b or b>c))
print("a>b || b<c : ", (a>b or b<c))
print("a<b || b<c : ", (a<b or b<c))
# not
print("!(a>b)", not(a>b))
print("!(a<b)", not(a<b))

# 비트 연산자 : &, |, ^, !, >>, <<
print("a & b : ", (a & b))
print("a | b : ", (a | b))
print("a ^ b : ", (a ^ b))
print("~a : ", ~a)  # complement(보수)
#1 0 0 0 0 0 0 -> 64 - 23 = (-)41
# 0  1  0 1 1 1 ~a : -41
# 32 16 8 4 2 1
# 1  0  1 0 0 0  a
# 0  1  1 1 1 0  b
# 0  0  1 0 0 0  and : 8
# 1  1  1 1 1 0  or : 62
# 1  1  0 1 1 0  xor : 54