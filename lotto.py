#로또 번호 만들기
import random

#함수선언
def getnum():
        return random.randrange(1,46)
    

#전역변수
lotto=[]
num = 0


#메인코드
print("** 로또를 추첨한다 ** \n")
while True :
    num = getnum()
    if lotto.count(num) == 0 :
        lotto.append(num)
        
    if len(lotto) >= 6:
        break

print("추첨된 로또 번호 ==> ", end = '')
lotto.sort()
for i in range(0,6) :
    print("%d " % lotto[i], end ='')
    
