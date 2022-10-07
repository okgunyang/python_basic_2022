# 컴퓨터에서 1~10의 임의의 수를 발생시키고,
# 사용자가 입력한 수가 일치하면, 미션성공으로 출력하고,
# 만약, 일치하지 않으면, 불일치로 출력하며, 일치할 때 까지
# 사용자의 숫자 입력은 계속된다.
import random
com = random.randint(1, 10)
while True:
    su = int(input("입력 :"))
    if(su==com):
        print("미션 성공")
        break
    else:
        print("불일치")

# 클래스로 진행하는 경우
import random
class NumberGame:
    com = random.randint(1, 10)
    def numberCheck(self):
        while True:
            su = int(input("입력 :"))
            if (su == com):
                print("미션 성공")
                break
            else:
                print("불일치")
ck = NumberGame()
ck.numberCheck()
