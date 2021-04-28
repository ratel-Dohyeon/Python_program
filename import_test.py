
import sys
print(sys.argv)

import pickle
f = open("test.txt", 'wb')
data = {1: 'python', 2:'you need'}
pickle.dump(data, f) #파일을 저장한다.
f.close

import pickle
f = open("test.txt", 'rb')
data = pickle.load(f)
print(data)

import os
os.environ
os.chdir("c:\WINDOWS")
os.getcwd()
os.system("dir")
f=os.popen("dir")
print(f.read())


import shutil #파일 복사 함수 
shutil.copy("src.txt", "dst.txt")

import glob #파일 이름 모두 소환 
glob.glob("C:\Python\Python_program\names\yo*.*")
glob.glob("names\yo*.*")
glob.glob("C:\Python\Python_program\data\data\*.*")
glob.glob("data\data\*.*")

import time
time.time()
time.localtime(time.time())
time.asctime(time.localtime(time.time()))

time.strftime('%x', time.localtime(time.time())) #날짜
time.strftime('%c', time.localtime(time.time())) #시간까지 

#타임슬립(카운트 다운 같은거)
for i in range(10):
    print(i)
    time.sleep(1)

import calendar
print(calendar.calendar(2021))

calendar.prcal(2021)
calendar.prmonth(2021, 4)
calendar.weekday(2021, 4, 27)
calendar.monthrange(2021, 4)


import random
random.random() #난수 발생 
random.randint(1,10) #1~10 사이의 랜덤 리턴

data = [1,2,3,4,5,6]
random.shuffle(data)
data

#로또
lotto = sorted(random.sample(range(1,46), 6))
print(lotto)


#인터넷 열기
import webbrowser 
webbrowser.open("http://google.com")
webbrowser.open_new("http://naver.com")

























































































