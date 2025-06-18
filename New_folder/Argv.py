# from sys import argv
#print(type(argv))
#print(argv[1:])

# print("The number of command line arguments :",len(argv))
# print("The list of command line arguments :",argv)
# print("command line arguments one by one")
# for i in argv:
#     print(i)

# args=argv[1:]
# sum=0
# for i in args:
#     n=int(i)
#     sum=sum+n
# print("sum :",sum)    

# 

a=4
sum=0

for i in range(1,4):
    sum+=i
print("sum:",sum)    
# Calculate sum of numbers from 1 to 3 (range excludes 4)
# total_sum = sum(range(4))

# print("Sum:", total_sum)
b=1234
count=0

while b>0:
    b=b//10
    count += 1
print("count:",count)    