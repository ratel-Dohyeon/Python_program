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





































































