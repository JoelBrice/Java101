###datatypes
#integers and floating points

a = 12.02
a = int(a) # Cast to int
print(a)

b = 12;
b = float(b)
print(b)

#string variable manipulation

string_var = "Hello world!"

string_var = string_var.split() #split in words
print(string_var)
for i in string_var:
    print(i)
print('\n')

for j in string_var:
    j = j.upper()
    print(j)
    
print('\n')

#array
a = ["python", "cpp", "java"]

for i in a:
    print(i) # print each item in the array 
    i = i.title() # transform each element into a title type (first letter uppercase)
    print(i)
    print(i)
print('\n')
#len of a string
for j in range(len(a)):
    a[j] = a.append("Hello ")

print(a)

#if statement and for loop
for [x,y] in [[2,4], [3,4]]:
    if x<y:
        print('%d is less than %d'% (x,y))
        
print('\n')

#Break statement
for var in "string":
    if var =='i':
        break
    else:
        print(var)
print("Hello!")
# Continue  statement
for var in "greeting":
    if var =="i":
        continue
    else:
        print(var)
        
for num in range(10,20):
    for i in range(2,num):
        if num%i==0:
            j=num/i
            print('%d equal %d * %d'%(num,i,j))
            

# Dictionary
print('\n')

dic = { 2015: 'cpp and javascript', 2016: 'java and php', 2017: 'python', 2018: 'c#', 2019: 'matlab', 2020: 'Machine Learning'}
dic_keys = dic.keys()
print(dic_keys)

dic[2021] = 'IoT' #add a key value pair to the dictrionary
for i in dic_keys:
    print(dic[i])   
dic.update() #update the dictionary

print(dic)    

del dic[2021] # delete an item in a dictionary
dic.update() #updte the dictionay
print(dic)

#function
def a():
    print("Hello there!")
a()

#Pass by value 

def add(x,y):
    return x+y

x = 13
y = 10
print(add(x,y))

print('\n')

#and pass by reference
k = [1,12,4,3,5,2]

def addAll(h):
    h = k
    for i in h:
        i +=i
    return h
addAll(k)

#modules
from mathematical_operations import * #import everything from the module

a = int(input('Enter a value: ')) #cast the value to an integer
b = int(input('Enter another value: '))#cast the value to an integer

addition = addTwo(a,b)
divide = division(a,b)
multiply = multiplication(a,b)
diff = difference(a,b)

print("Sum= ", addition)
print("Quotient=", round(divide,2))
print("Product= ", multiply)
print("difference=",diff)
print("Absolute value = %d "% abs(diff)) # print the absolute value

print("Let's calculate the surface of a circle")
r = float(input("Enter the radius of the circle: "))
surface = calculate_surface_circle(r)
print("The surface = ", round(surface,3))

#Exception handling
try:
    c = int(input("Enter a value to divide a with: "))
    division(a,c)
    #break
except:
    print("Please enter a valide value: ")
    c = int(input())
    #break
finally:
    print("Invalid value ")