a = 3
b = 4
a+b

a*b
a**b

# 사칙연산 

a = 100
b = 50
result = a+b
result = a-b
result = a*b
result = a/b



국어 = 80
영어 = 75
수학 = 55

(국어+수학+영어)/3

"ㄴㅇㄴㅁㅇㅁㄴㅇㅁㄴㅇ"
"""ㄴㅇㄴㅁㅇㅁㄴㅇㄴㅁ"""
'11123213213123123'
'''123213213123123'''



food = "sadkashdkashdasdasdasdg"
say = 'asdasiudyhasifhag'
print(food)
print(say)



#계산기

a = 100
b = 50
result = a+b 
result2 = a-b
result3 = a*b
result4 = a/b

print(result)
print(a,"+", b,"=", result)
print(a,"-", b,"=", result2)
print(a,"*", b,"=", result3)
print(a,"/", b,"=", result4)


#계산기


a = int(input("첫번째 숫자"))
b = int(input("두번째 숫자"))
result = a+b 
result2 = a-b
result3 = a*b
result4 = a/b

print(result)
print(a,"+", b,"=", result)
print(a,"-", b,"=", result2)
print(a,"*", b,"=", result3)
print(a,"/", b,"=", result4)



multiline =  "sdkjhsdaskjdsakjakshasghhfghkjdhas \  nhgfhgfhfhtrhhggfhfghfgfhgfhgfhrt"

multiline = '''
sdasdasdas
sadsadasdasd
sadasdasdas
'''


head = "python"
tail = " is fun!"
head + tail

a = "python"
a*2
a*100

print("\n줄바꿈\n연습")
print("\t탭키\t연습")
print("글자가 \"강조\"되는 효과1")
print("글자가 \'강조\'되는 효과2")
print("\\\\\\ 역슬래시 세 개 출력")
print(r"\n \t \" \\를 그대로 출력")


#동전교환기

#변수선언
money, c500, c100, c50, c10 = 0,0,0,0,0


#메인코드

money = int(input("교환할 돈 얼마?"))

c500 = money // 500
money %=500

c100 = money // 100
money %=100

c50 = money // 50
money %=50

c10 = money // 10
money %=10


print("\n 500원짜리 => %d개" %c500)
print("\n 100원짜리 => %d개" %c100)
print("\n 50원짜리 => %d개" %c50)
print("\n 10원짜리 => %d개" %c10)
print("바꾸지 못한 잔돈 => %d원 \n" % money)



# # #  파이썬

아래는 print()문을 이용해서 해결해 보세요. [1~3번]
1.
이름 나이 지역
오라클 10 구로구
파이썬 3 구로구

print("이름\t나이\t지역\n오라클\t10\t구로구\n파이썬\t3\t구로구")






2. '동해물과 백두산이 마르고 닳도록 하느님이 보우하사 우리나라 만세'를 아래 같이 출력해 보세요.

동해물과 백두산이 마르고 닳도록
하느님이 보우하사 우리나라 만세

multiline = ("\n동해물과 백두산이 마르고 닳도록 \n하느님이 보우하사 우리나라 만세")
print(multiline)




3. '안녕하세요'를 아래와 같이 출력해 보세요.
안녕하세요 안녕하세요 안녕하세요

a = "안녕하세요 "
a * 3



-------------------------------------------------------------------------------------------------------
아래와 같은 결과가 나오도록 프로그램 해 보세요. [4~6번 해당]

4. 당신의 나이는 몇 살이세요?22
제 나이는 22 입니다.

#변수선언
몇살이냐, 이름은 = 0,0


#메인코드

몇살이냐 = str(input("당신의 나이는?"))

몇살이냐 = 22
나이 = 몇살이냐

print("\n 제 나이는 %d 입니다" %나이)




5. 당신의 이름은?제니

이름은 = str(input("당신의 이름은?"))

이름은 = "제니"
이름 = 이름은

print("\n 제 이름은  %s 입니다" %이름)


6.
제 나이는 22 이고, 이름은 제니 입니다.

몇살 = 22
성명 = "제니"

print("\n 제 나이는 %d 이고 이름은  %s 입니다" %(나이, 성명))

7. 대입 연산자의 활용이다. 결과를 예측하시오.
① a,b = 10,20; a+=b; print(a)
② a,b = 10,20; a%=b; print(a)
③ a,b = 10,20; a//=b; print(a)

a,b=10,20; a+=b; print(a) #30
a,b=10,20; a%=b; print(a) #10
a,b=10,20; a//=b; print(a) #0





#인덱싱
a = "sfdjldfdlkf,dfdlfkjdfdsf"
a [0] #  <=== a에 있는 첫번째 글자를 가져와, 파이썬은 숫자를 0부터 센다/
a [12]
a [-12] #뒤에서부터 세기
a [-1]

b = "안녕하세요"
b [0]
b [1]
b [2]
b [3]
b [4]


b = "안녕하세요"

b [-1]
b [-2]
b [-3]
b [-4]
b [-5]


#슬라이싱(자른다)
a = "life is too short, you need python"
b = a[0]+a[1]+a[2]+a[3]+a[4]+a[5]+a[6]
b

a [0:4] #첫번째부어 네번째 !미만!
a [0:3] 
a [0:5] #공백까지 포함
a [12:17]  

string = "python1"

string [0:8]
string [3:8]
string [0:3]
string [0:4]
string [0:7]


a[19:]      #19번때부터 끝까지
a[:17]      #처음부터 17번째까지
a[:]        #처음부터 끝까지
a[19:-7]    #19부터 -7까지

a = "20010331Rainy"
date = a[:8]
weather = a[8:]

date
weather

a = "pithon"
a[:1]
a[2:]

a[:1] +'y'+a[2:]


pin = "881120-1068234"

yyyymmdd = '19'+ pin[0:6]
yyyymmdd

num = pin[7:]
num

print(yyyymmdd)
print(num)

print(pin[-7])




#문자열 자료형

#숫자 바로 대입
"I eat %d apples." %3

#문자 바로 대입
"I eat %s apples." %"five"

#숫자값을 나타내는 변수로 대입
num = 3
"I eat %d apples." % num



num = 10
day = "three"

"I ate %d apples. so I was sick for %s days." %(num, day)


"%0.4f" % 3.42134234 #소수점 이하 날리기


print("%d" % (100+100))
print("%d %d" % (100, 200))
print("%d / %d = %d" % (100, 200, 0.5))

print("%10s" % "python") #10자리 확보후 출력 


"%10s" % "hi" #10자리(빈칸) 확보후 출력






#동전교환기

#변수선언
money, c50000, c10000, c5000, c1000 = 0,0,0,0,0


#메인코드

money = int(input("지폐로 교환할 돈 얼마?"))

c50000 = money // 50000
money %=50000

c10000 = money // 10000
money %=10000

c5000 = money // 5000
money %=5000

c1000 = money // 1000
money %=1000


print("\n 50000원짜리 => %d개" %c50000)
print("\n 10000원짜리 => %d개" %c10000)
print("\n 5000원짜리 => %d개" %c5000)
print("\n 1000원짜리 => %d개" %c1000)
print("바꾸지 못한 잔돈 => %d원 \n" % money)



## 변수 선언 부분
money, c50000, c10000, c5000, c1000 = 0,0,0,0,0
## 메인(main) 코드 부분
money=int(input("교환할 돈은 얼마 ? "))
c50000 = money // 50000; money %= 50000
c10000 = money // 10000; money %= 10000
c5000 = money // 5000; money %= 5000
c1000 = money // 1000; money %= 1000
print(" 50000원 %d장, 10000원 %d장, 5000원 %d장, 1000원 %d장" % (c50000, c10000, c5000, c1000))
print(" 바꾸지 못한 돈 ==> %d원 \n"% money)




#포맷 함수
#숫자 바로 대입
"I eat {} apples.".format(3)

#문자 바로 대입
"I eat {} apples.".format("five")

#숫자값을 나타내는 변수로 대입
num = 3
"I eat {} apples.".format(num)


#count 함수
a = "hobby"
a.count('b') #b가 몇개 있냐


#find함수
a="python is best choice"
a.find('b') # b가 몇변째 있냐?
a.find('k') # k 없으면 -1 출력 


#index함수
a= "life is too short"
a.index('t') # t가 몇번째 있냐



#문자열 삽입(조인)
a=","
a.join('abcd') #사이사이에 , 넣기


a=" "
a.join('abcd') #사이사이에 공백 넣기


#대,소문자 변경 함수
a="hi"
a.upper()
a.lower()


#공백삭제
a.strip()
a.lstrip()


a= "life is too short"
a.replace("life", "your leg")


#문자열 나누기
a="a:b:c:d"
a.split(':') #기호를 기준으로 문자열 나누기
a.split( ) #공백을 기준으로 문자열 나누기


odd = [1,3,5,7,9] #[] <--  얘로 시작하는것은 리스트임
a=[]
b=[1,2,3]
c=['life', 'is', 'too', 'short']
d=[1,2,'life', 'is' ]
e=[1,2,['life', 'is'] ]

#리스트의 인덱싱
a=[1,2,3]
    a[0]
    a[0]+a[2]
    a[-1]
    
 
#리스트 필요성
a,b,c,d=0,0,0,0
hap=0

a=int(input("1번째 숫자 : "))
b=int(input("2번째 숫자 : "))
c=int(input("3번째 숫자 : "))
d=int(input("4번째 숫자 : "))

hap = a+b+c+d

print("합계 ==> %d" % hap)


aa=[0,0,0,0]
hap = 0

aa[0]=int(input("1번째 숫자 : "))
aa[1]=int(input("2번째 숫자 : "))
aa[2]=int(input("3번째 숫자 : "))
aa[3]=int(input("4번째 숫자 : "))

hap = aa[0]++aa[1]+aa[2]+aa[3]

print("합계 ==> %d" % hap)


a = [1,2,3]
b = [4,5,6]
a+b 

a*3 #3번 반복


#수정
a[2] = 4
a

a[1:2] = ['a','b','c']
a


a[1:3]= []
a

del a[1]
a


#추가
a=[1,2,3]
a.append(4)
a

#정렬
a=[1,4,3,2]
a.sort()
a


#역순
a=['a','b','c']
a.reverse()
a

#위치반환 
a=[1,2,3]
a.index(3)


#요소삽입
a.insert(0,4) #0(첫)의 자리에 4를 넣어라
a


#요고 끄집어내기
a.pop() #마지막 요소 출력후 삭제
a

#요소의 갯수세기
a=[1,2,3,1]
a.count(1) #a에 1이 몇개임?


#리스트 확장
a=[1,2,3]
a.extend([4,5]) #리스트가 추가 
a

b=[6,7]
a.extend(b)
a




colors1 = ['red', 'blue', 'green']
colors2 = ['orange', 'black', 'white']

print(colors[0])
print(colors[1])
print(len(colors)) #리스트의 길이

print(colors1 + colors2)
print(colors1*2)
print(colors1 + colors2[0:2])



#연습
list = [30, 10, 20]

#1 40 추가
list.append(40)
list


#2 마지막 요소 제거
list.pop()
list

#3 정렬
list.sort()
list

#4 뒤로 정렬
list.reverse()
list

#5 20 위치값
list.index(20)
list

#6 삽입
list.insert(2,222) #2번 자리에 222 넣어라
list

#7 remove
list.remove(222) #222찾아서 제거
list

#8 리스트 추가 
list.extend([77,88,77])
list

list.count(list))



#답안
myList = [30, 10, 20]
print("현재 리스트 : %s" % myList)

myList.append(40)
print("append(40) 후의 리스트 : %s" % myList)

print("pop()으로 추출한 값 : %s" % myList.pop())
print("pop() 후의 리스트 : %s" % myList)

myList.sort()
print("sort() 후의 리스트 : %s" % myList)

myList.reverse()
print("reverse() 후의 리스트 : %s" % myList)

print("20값의 위치 : %d" % myList.index(20))

myList.insert(2, 222)
print("insert(2, 222) 후의 리스트 : %s" % myList)

myList.remove(222)
print("remove(222) 후의 리스트 : %s" % myList)

myList.extend( [77, 88, 77] )
print("extend([77, 88, 77]) 후의 리스트 : %s" % myList)

print("77값의 개수 : %d" % myList.count(77))






#  *튜플은 값을 변경할 수 없다.

t1 = (1, 2, 'a', 'b')
t1[0]
t1[3]
t1[1:]

t2 = (3,4)
t1+t2
t2*3


myT = (10, 20, 30)
myTl = list(myT)
9myTl.append(40)
myT = tuple(myTl)
print(myT)




#딕셔너리 

a = {1: 'a'}
a[2] = 'b'
a

a['name'] = 'pay'
a[3] = [1,2,3]


del a[1]
a

          #키    벨류
grade = {'pay' : 10, 'julliet':99}
grade['pay'] #키를 입력하면 벨류를 불러온다
grade['julliet']


#키 리스트
a = {'name':'pay', 'phone':'01044751845', 'birth':'1118'}
a.keys() #키만 가지고와라
a.items() #키-벨류 쌍으로 가져와라
a.get('name') # name의 벨류를 가져와라
a.get('phone') # phone의 벨류를 가져와라



student = {'학번':'1000', '이름':'김아이티', '학과':'컴퓨터학과'}
student

student['연락처'] = '01012341234' #연락처 추가
print(student)

student['학과'] = '전자공학과' #수정
print(student)

student.get('학과')

student.keys()




#집합 자료형

s1 =set([1,2,3])
s1

s2 = set("hello") #순서가 없고 중복을 허용하지 않은다
s2


#교집합
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9]) 
s1 & s2 #교집합
s1.intersection(s2) #교집합

#합집합
s1 | s2 #자동으로 중복이 빠짐
s1.union(s2)

#차집합
s1 - s2
s2 - s1
s1.difference(s2)
s2.difference(s1)

#대칭 차집합
s1^s2 
s1.symmetric_difference(s2)





#값 1개 추가
s1 = set([1,2,3])
s1.add(4)
s1

#값 여러개 추가
s1.update([4,5,6])
s1

#값 제거
s1.remove(2)
s1



#참과 거짓
a = [1,2,3,4]
while a:
    a.pop()


#리스트 중복 자료 제거 
a=[1,1,1,2,2,3,3,3,4,4,5]
aSet = set(a)
b = list(aSet)
print(b)


a = [1,2,3]
b = a
a[1] = 4
a
b


a = [1,2,3]
b = a[:] #몽땅 복사
a[1] = 4
a
b




#1 life is too short 만들기
a = ['life', 'is', 'too', 'short']
result = (' '.join(a))
print(result)


#2 
a = (1, 2, 3)
a = list(a)
a.append(4)
a = tuple(a)
print(a)



#3 
a={'A':90, 'B':80, 'C':70}
result = a.pop('B')
print(a)
print(result)



money = 1
if money:
    print("택시타")
    print("간식사")
else:
    print("걸어가")
    
    
#반드시 줄 맞춰야 함 아니면 오류 남     
if money:
    print("택시를")
    print("타고")
    print("가라")


money = True # 앞자리 반드시 대문자

if money: 
    print("택시를")
    print("타고")
    print("가라")




a = 200
if a < 100:
    print("100보다 작군요")
    
else: #파이썬은 명령어 위치 중요!!
    print("100보다 크군요")



kg = int(input("짐의 무게는 얼마?"))

if kg > 20:
    print("2만원")
    print("감사합니다")
else:
    print("수수료 없음")
    print("감사합니다")




x=3
y=2
x>y
x==y
x!=y

money = 2000
if money >= 3000:
    print("택시타")

else:
    print("걸어가")


print("몇살이냐")
myage = int(input())
if myage < 30:
    print("웰컴")
else:
    print("돌아가")



print("지금 날씨")
tem = int(input())
if tem > 30:
    print("반바지")
    print("운동해")
else:
    print("긴바지")
    print("운동해")


print("정수를 입력하세요")
num = int(input())
if num%2 != 0:
    print("홀수이군요")
else:
    print("짝수이군요.")


money = 2000
card = 1
if money >= 3000 or card:
    print("택시타")

else:
    print("걸어가")


1 in [1,2,3]        #리스트 안에 1이 있는가?
1 not in [1,2,3]    #리스트 안에 1이 없는가?


pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket: #pocket 안에 money가 있으면 true
    print("택시타")

else:
    print("걸어가")



pocket = ['paper', 'cellphone', 'money']
if 'card' not in pocket: #pocket 안에 card가 있으면 true, 없으면 false
    print("걸어가")

else:
    print("버스")


pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket: #pocket 안에 money가 있으면 pass
    pass #아무것도 하지 않고 if 문을 빠져나옴 
else:
    print("카드꺼내")



a= 75
if a > 50:
    if a < 100:
        print("50보다 크고 100보다 작아")
    else:
        print("100보다 큼")
else:
   print("50보다 작음") 


#다중조건 판단 elif
pocket = ['paper', 'cellphone']
card = 1
if 'money' in pocket:
    print("택시타")
elif card:
    print("택시타")
else:
    print("걸어가")
    
    
score = int(input("점수입력 : "))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else :
    print("F")

print("학점입니다.")


score = int(input("점수입력 : "))
if score >= 95:
    print("A+")
elif score >= 84:
    print("A0")
elif score >= 80:
    print("B+")
elif score >= 75:
    print("B0")
elif score >= 70:
    print("C+")   
elif score >= 65:
    print("D+")   
elif score >= 60:
    print("D")    
else :
    print("F")

print("학점입니다.")




month = int(input("월입력 : "))

if month == 2:
    print("월의 날수 29일")

elif month == 4 or 6 or 10:
    print("월의 날수 30일")

else :
    print("월의 날수 31일")


jum = 55
res = ''
res = '합격' if jum >= 60 else '불합격'



# 반복문  while
treehit = 0
while treehit < 10:
    treehit = treehit+1
    print("나무를 %d번 찍었습니다." % treehit)
    if treehit == 10:
        print("나무는 넘어갑니다.")


hi = 0
while hi < 3:
    print("%d: 안녕." % hi)
    hi = hi+1
    if hi == 3:
        print("안녕끝.")



i, hap = 0,0
i = 1
while i < 11:
    hap = hap + i
    i = i + 1
    print("1에서 10까지의 합계 : %d" % hap)


coffee = 10
money = 300
while money:
    print("돈 받음. 커피줌")
    coffee = coffee -1
    print("남은 커피 양 %d개" % coffee)
    if not coffee:
        print("커피 떨어짐. 판매중지")
    break



a = 0
while a < 10:
    a = a+1
    if a % 2 == 0: continue  #반복문으로 돌아게하는것 'continue'
print(a)

#위의 합계 구하기 
a = 0
sum_a = 0
while a < 10 :
    a = a + 1 
    if a % 2 == 0 : continue 
    sum_a += a
print("합계 %d"%sum_a)



#계산기
a,b = 0,0 
while True :
    a = int(input("첫번째 수를 입력하세요 :"))
    if a == 0 :
        print("프로그램을 종료합니다.")
        break
    b = int(input("두번째 수를 입력하세요 :"))
    c = a + b
    print("%d + %d = %d"%(a,b,c))




# 문제
    
1. //if else
100,000원을 초과한 금액에 대해 5%를 할인해 주고 있습니다.
총 금액이 110000일 경우 아래와 같은 프로그램을 작성해 보세요.

======== 결과 ==============================
구입 금액을 입력하시오: 110000
지불 금액은 104500.0 입니다.
==========================================

돈 = 0

돈 = int(input("돈내라 : "))
if 돈 >= 100000:
    할인 = 돈 * 0.95
    print("지불 금액은 %d" % 할인)
else :
    print("할인 음슴")

    
2. //if elif else

20~26세 대학생, 17세 이상이면 고등학생, 14세 이상이면 중학생,
8세 이상이면 초등학생 나머지는 나이와 학생이 아닙니다라고 출력하세요.

출력 결과)
당신이 태어난 연도를 입력하세요. 2010
초등학생

당신이 태어난 연도를 입력하세요. 1988
나이는 33세 학생이 아닙니다.


학생나이 = int(input("몇살이냐 : "))

if 학생나이 <= 20 or 학생나이 <= 26 :
    print("대딩")

elif 학생나이 <= 17:
    print("고딩")

elif 학생나이 <= 14:
    print("중딩")

elif 학생나이 <= 8:
    print("초딩")
else :
    print("예? 누구세요?")


생년 = int(input("몇년생이냐 : " ))
현재 = 2021
나이 = int(현재 - 생년)

if  나이 <= 8:
    print("초딩")

elif 나이 <= 14:
    print("중딩")

elif 나이 <= 17:
    print("고딩")

elif 나이 == 20 and 나이 <= 26:
    print("대딩")

else :
    print("예? 누구세요?")
    print("당신의 나이는 만 %d살 입니다 꺼져" % 나이)


// while
3. 시작값, 끝값, 증가값을 넣으면 합계를 출력하는 프로그램을 작성하세요.

출력 결과)
시작값을 입력하세요 : 1
끝값을 입력하세요 : 10
증가값을 입력하세요 : 1
1에서 10까지 1씩 증가시킨 값의 합계 : 55

시작값을 입력하세요 : 2
끝값을 입력하세요 : 10
증가값을 입력하세요 : 2
2에서 10까지 2씩 증가시킨 값의 합계 : 30


//while
4. 구구단 3단을 출력해 보세요.

3*1 = 3
3*2 = 6
3*3 = 9
3*4 = 12
3*5 = 15
3*6 = 18
3*7 = 21
3*8 = 24
3*9 = 27


뚜릐 = 3
곱 = 1
while 곱 < 10:
    답 = 뚜릐 * 곱
    print("%d * %d = %d" %(뚜릐, 곱, 답))
    곱 = 곱 + 1












    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    























































































































































