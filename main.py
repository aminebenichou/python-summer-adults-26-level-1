# a=0

# while a<10:
#     print("hello")
#     a = a+2


# numbers=[1, 2, 3, 4, 5]
# i=0
# while i<5:
#     print(numbers[i])
#     i = i + 2

# 0, 1, 1, 2, 3, 5, 8

fibunnaci=[0, 1]
limit=18
i=0
while i<limit:
    fibunnaci.append(fibunnaci[i]+fibunnaci[i+1])
    
    i = i+1

print(fibunnaci)


# pneumo
word= "pneumonoultramicroscopicsilicovolcanoconiosis"

result=""
b=0
while b<6:
    result= result + word[b]
    b = b+1

print(result)