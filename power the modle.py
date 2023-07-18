class module:
    def __init__(self,A, B, C):
        self.res = (A ** B) % C
        
obj_1=module(2,3,3)
obj_2=module(5,2,4)
print("output 1:",obj_1.res)
print("output 2:",obj_2.res)

