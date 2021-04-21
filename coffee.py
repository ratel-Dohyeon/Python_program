
#커피 자판기
coffee = 10
while True:
    money = int(input("돈넣어 : "))
    if money == 300:
        print("커피줌")
        coffee = coffee -1
    elif money > 300:
        print("거스름돈  %d를 주고 커피 줌" % (money -300))
        coffee = coffee -1
    else:
        print("돈 돌려주고 커피 안줌")
        print("남은 커피 양 %d개" % coffee)
    if coffee == 0:
        print("커피 떨어짐. 판매중지")
        break



















































