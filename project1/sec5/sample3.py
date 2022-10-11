# 항공사의 화물요금을 계산하는 프로그램을 작성하여라
# 화물의 중량을 입력받아
# 화물의 10kg 단위당 2,000원이 부과되며, 10kg 미만이면, 화물료는 없음

weight = int(input("화물의 무게 :"))
if(weight<10):
    print("화물요금은 무료~!")
else:
    print("화물요금 : {:,}".format(weight//10*2000))
    #print("화물요금 :",format(weight//10*2000,","))



# 클래스로 처리하는 경우

class WeightCalc:
    weight = 0
    def inputWeight(self):
        self.weight = int(input("화물의 무게 :"))

    def printMoney(self):
        if (self.weight < 10):
            print("화물요금은 무료~!")
        else:
            print("화물요금 : {:,}".format(self.weight // 10 * 2000))

w = WeightCalc()
w.inputWeight()
w.printMoney()