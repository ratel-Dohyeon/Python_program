#단간한 메모장 만들기 

import sys

option = sys.argv[1]
#memo = sys.argv[2]

if option == '-a':
    memo = sys.argv[2]
    f = open('memo.txt', 'a')
    f.write(memo)
    f.write('\n') #줄바꿈
    f.close()
elif option == '-v':
        f = open('memo.txt')
        memo = f.read()
        f.close()
        print(memo)
    
    
    
    