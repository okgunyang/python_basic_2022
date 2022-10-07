class Rectangle:
    count = 0

    def __int__(self, width, height):
        self.width = width
        self.height = height
        Rectangle.count += 1
        print("사각형 생성")

    # 면적 구하는 멤버 메소드 - calcArea
    def calcArea(self):
        area = self.width*self.height
        return area

    # 정사각형인지 확인하는 메소드 - isSquare
    # static(정적) 메소드로 구현
    @staticmethod
    def isSquare(w, h):
        return w==h

    # 사각형의 개수를 출력하는 메소드 - printCount
    # 객체(클래스)를 매개변수로 받을 수 있도록 클래스 메소드로 구현
    @classmethod
    def printCount(rect):
        print(rect.count)

    def __add__(self, other):
        obj = Rectangle(self.width+other.width, self.height+other.height)
        print("객체 연산")
        return obj

    def __del__(self):
        print("사각형 소멸")

# rect1 = Rectangle(20, 10)
# rect2 = Rectangle(15, 15)
# rect3 = Rectangle(8, 12)
# rect4 = rect2 + rect3
# print("rect1의 면적 : ",rect1.calcArea())
# print("너비:18, 높이:20 사각형은 정사각형? ",Rectangle.isSquare(18,20))
# print("rect4의 면적 : ", rect4.calcArea())
# rect4.printCount()

import project1.sec4.test17
obj2 = project1.Test(60, 80)
print(obj2.plus())
print(obj2.minus())