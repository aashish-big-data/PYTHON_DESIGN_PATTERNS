# -*- coding: utf-8 -*-
"""

@author: AASHISH
"""

'''
Single Responsible Principle:
    
    Idea is to have the key tasks for the Class.
    Class should not be flooded with other responsibilities 
    which it does not belong.

    Below Journel class
    we have added the task of file saving responsibilities to Journel CLass.
    which is not correct as per Single Responsible Principle:
    
    We can have another class for saving files and calling them inside 
    Journel class
        
    Hence we created another independent CLASS as File_Manager 
    
'''


import  os

class journel():
    
    def __repr__(self,):
        return " ".join(self._journel)
    
    def __init__(self,):
        self._journel={}
        
    def add_journel(self,topic,contents):
        if(topic not in self._journel):
            self._journel[topic]=[]
            self._journel[topic].append(contents)
            
        else:
            self._journel[topic].append(contents)
            
    def Print_Journel(self,):
        for key ,val in self._journel.items():
            print(f'{key}==>{val}')
            
    def save_files(self,):
        path=os.getcwd()
        
        for key,val in self._journel.items():
            file1=open(path+"\\" + key+".txt","w")
            file1.write(val[0])
            
            del(file1)    
        
class File_Manager:
    @staticmethod
    def save_files(journel):
        path=os.getcwd()
        
        
        for key,val in journel._journel.items():
            file1=open(path+"\\" + key+".txt","w")
            file1.write(val[0])
            file1.close()    
    
obj_j=journel()

cont=input("enter the topic and contents with delimeter as |")
cont=cont.split("|")

while(cont[0]!='NO'):
    obj_j.add_journel(cont[0],cont[1])
    obj_j.Print_Journel()
    cont=input("enter the topic and contents with delimeter as |")
    cont=cont.split("|")


obj_j.Print_Journel()

print(obj_j)


File_Manager.save_files(obj_j)

#obj_j.save_files()

