PI = 3.141592

class Math:
    def solve(self,r):
        return PI * (r ** 2)
    
def sum(a,b):
    return a+b

if  __name__ == "__main__": #import만 갈겼을때 실행이 되지 않게 하는거
    print(PI)
    a = Math()
    print(a.solve(2))
    print(sum(PI, 4.4))
    
    











