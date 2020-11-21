# Initializing only Once.

class shape(object):
    flag=0
    
    def __new__(cls,):
        if(shape.flag==0):
            shape.flag=1
            return super(shape, cls).__new__(cls) 
        
    def __init__(self): 
        print("Init is called")        
        
    def __str__(self,):
        return f'==> {shape.flag}'

    def get(self,):
        for i in range(10):
            print("Object created once")
        

def Client(o,obj): # client should not create the singleton object again
    if(o=='a'):
        a=shape()
        a.get()
        
    else:
        obj.get()
    
try:        
    a=shape()
    key=input("enter the key")
    Client(key,a)
    
except :
    print("Error Already object created. This is a single ton object")
