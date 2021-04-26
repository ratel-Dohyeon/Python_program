f = open("C:/새파일.txt ", 'w')

\
#파일 만들기
f = open("C:/Python/새파일.txt ", 'w')
for i in range(1,11):
    data = "%d번째 줄입니다. \n" % i
    f.write(data) #새 파일로 저장 
f.close()

#1번째줄 읽어오기
f = open("C:/Python/새파일.txt", 'r')
line = f.readline()
print(line)
f.close()


#라인 전체 읽어오기 (while문 활용)
f = open("C:/Python/새파일.txt", 'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()


#라인 전체 읽어오기 (for문 활용)
f = open("C:/Python/새파일.txt", 'r')
lines = f.readline() #readline =  한라인만 가져옴
for line in lines :
    line = f.readline()
    print(line)
f.close()


f = open("C:/Python/새파일.txt", 'r')
lines = f.readlines() #readlines =  라인을 다 가져옴
for line in lines :
    print(line)
f.close()


#스트링으로 반환 
f = open("C:/Python/새파일.txt", 'r')
data = f.read()
print(data)
f.close()


#새로운 내용 추가
f = open("C:/Python/새파일.txt", 'a')
for i in range(11,20):
    data = "%d번째 줄입니다 \n" % i
    f.write(data)
f.close()


#with문 함께 사용
f = open("C:/Python/foo.txt", 'w')
f.write("life is too short, you need Python")
f.close()

#with문 = f.close() 필요없음 
with open("C:/Python/foo1.txt", 'w') as f:
    f.write("life is too short, you need Python")
    

#파일 읽어오기
f = open("C:/Python/dream1.txt", 'r')
data = f.read()
print(data)
f.close()


#with문 = f.close() 필요없음 
with open("C:/Python/dream1.txt", 'r') as my_file:
    conti = my_file.read()
    w_list = conti.split(" ")  # 빈칸 기준으로 단어 분리 리스트
    l_list = conti.split("\n") # 한줄씩 분리하여 리스트
    
print("총 글자 수 :", len(conti)) # len <- 얘는 len 은 문자열 길이 구하는 함수 and 단어(문자열)의 수도 구함
print("총 단어 수 :", len(w_list))
print("총 줄릐 수 :", len(l_list))

#클래스

#함수
result = 0
def add(num):
    global result #전체에서 변수를 사용하기 위한 global 선언 
    result += num
    return result

#메인(입력)
print(add(3))
print(add(4))




#함수
result1 = 0
result2 = 0

def add1(num):
    global result1 #전체에서 변수를 사용하기 위한 global 선언 
    result1 += num
    return result1

def add2(num):
    global result2 #전체에서 변수를 사용하기 위한 global 선언 
    result2 += num
    return result2

#메인(입력)
print(add1(3))
print(add1(4))
print(add2(3))
print(add2(7))



#클래스 안의 독립적으로 돌아기는 계산기
#클래그 앞자리는 대문자
class Calculator:
    def __init__(self): # __init__ <-- 초기화
        self.result = 0
       
    def add(self, num):
        self.result += num
        return self.result
   
    def min(self, num):
        self.result -= num
        return self.result    
        
cal1 = Calculator()
cal2 = Calculator()
cal3 = Calculator()

print(cal1.add(3))
print(cal2.add(3))
print(cal3.add(3))
print(cal1.min(3))
print(cal2.min(3))
print(cal3.min(3))


#사칙연산 클래스
class FourCal:
    
    def __init__(a, first, second):  #<--생성자
        a.first = first
        a.second = second
    
    def setdata(a, first, second):  #<--메서드
        a.first = first
        a.second = second
        
    def add(a):                     #<-- 더하기 메서드
        result = a.first + a.second
        return result 
      
    def minu(a):                    #<-- 빼기 메서드
        result = a.first - a.second
        return result      
    
    def nanu(a):                    #<-- 나누기 메서드
        result = a.first / a.second
        return result 

    def gop(a):                     #<-- 곱하기 메서드
        result = a.first * a.second
        return result 
    
    
##a,b 객체 만들기 
a = FourCal()
b = FourCal()

a.setdata(4,3) # <--- 객체 넣은거
b.setdata(1,5)

print(a.first) # <--- 자리 확인
print(a.second)# <--- 자리 확인

a.add()
a.minu()
a.nanu()
a.gop()

b.add()
b.minu()
b.nanu()
b.gop()



#상속 클래스
class  MoreFourCal(FourCal):
    def pow(a):
        result = a.first ** a.second
        return result 
            
a = MoreFourCal(4,2)
a.pow()
a.add()


#메서드 오버라이딩 : 기능추가 덮어쓰기
class  SafeFourCal(FourCal):
    def div(a):
        if a.second == 0:
            return 0
        
        else:
            return a.first / a.second
        
a = SafeFourCal(4,0)
a.div()












































































































