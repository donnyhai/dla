class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
class B:
    def __init__(self, b, c):
        self.b = b
        self.c = c

class C(A, B):
    def __init__(self, a, b, c):
        A.__init__(self, a, b)
        print(self.b)
        B.__init__(self, b+1, c)
        
cc = C(1,2,3)
print(cc.a)
print(cc.b)
print(cc.c)
