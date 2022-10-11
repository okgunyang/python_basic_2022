# 급여 처리 프로그램을 작성하여라
# 키보드로 총근무시간, 기본급 등을 입력받아 총급여를 계산하여 출력하도록 한다.
# 총급여=기본급+상여금+시간외수당
# 상여금은 기본급의 25%로 한다.
# 시간외수당은 정규근무시간이 160시간 이므로 그 시간을 초과하는 시간을
# 초과근무시간으로 하며,
# 시간외수당은 초과근무시간 당 기본급의 200을 나눈 값의 초과근무시간을
# 곱한 값으로 한다.
emp_time = int(input("근무시간 : "))
emp_base = int(input("기본급 : "))
over_emp = 160 - emp_time   # 초과 근무시간
bonus = emp_base * 0.25 # 보너스
overtime = 0
if over_emp>0:
    overtime = over_emp * emp_base / 200
tot = emp_base + bonus + overtime
print("기본급 : ", emp_base)
print("상여금 : ", bonus)
print("시간외수당 : ", overtime)
print("총급여 : ", tot)