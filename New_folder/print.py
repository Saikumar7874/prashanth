# print("hello sai",end='')
# print("adding in the same line")
# print("typing something")
# print("practicing programming language")
# print(10,29,30,sep=":")
# print(10,29,30,)

a,b,c=10,20,30
print("a value is %i " % a)
print("a value is %i and b value is %i " %(a,b))

#formatting string by using replacement operator

name="saikumar"
age=24
profession="preparing for job"

print("your name is {0} and age is {1} and you are {2}".format(name,age,profession))
print()
print("your name is {} and age is {} and you are {}".format(name,age,profession))
print(f'your name is {name} your age is {age} you are currently {profession}')
