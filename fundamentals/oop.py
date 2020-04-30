#!/usr/bin/env python3
#coding:utf-8
"""
  Author:  Joel Tiogo --<>
  Purpose: OOP principle
  Created: 04/29/20
"""
class Student:
    """The principle of object oriented programming"""

    def __init__(self, names, classes):
        """Constructor"""
        self.name = "Joel"
        self.classes = classes
        self.names = names
        
    def walk(self):
            print(" My name is ", self.names)
            print(" My name is ", self.name)
            print(" My name is ", self.classes)
            

s1 = Student('xyz', 12)
s1.walk()

s2 = Student('xyz', 18)
s2.walk()

# Inheritance

class Father():
    """Inheritance of children from father"""
        
    def lastname(self):
        print("Father surname")
        
class Mother():
    """"""
    def lastnameMother(self):
        print("Father surname")

class Son(Father):
    """Implement the Inheritance of son from father"""
    
    def firstname(self):
        """"""
        print("My firstname")
        
so1 = Son()
so1.firstname()
so1.lastname()
        
        
    
    
        
    
    
    