#모듈

#C:\Python\Python_program
# import : 이미 만들어진 모듈 사용

import mod1
import Module1 
import mod2

#메인코드
Module1.func1()
Module1.func2()
Module1.func3()

from Module1 import func1,func2,func3 
func1()
func2()
func3()

from Module1 import *
func1()
func2()
func3()


import sys
sys.path
sys.path.append("C:\Python\Python_program\Mymodules")



#
















































