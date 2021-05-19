#pg109

#4-3 counting to 20

for value in range(1, 21):
    print(value)

#4-4 one million
#for value in range(1, 1000001):
 #   print(value)

#4-5 summing a Million 

num_list = list(range(1, 10000001))

print(max(num_list))
print(min(num_list))
print(sum(num_list))

#4-6 Odd Numbers 

for value in range(1, 21, 2):
    print(value)

#4-7 Threes 

num_list2 = [] 
for value in range(3, 31):
    num_list2.append(value*3)
print(num_list2)

#more comprehensive way 

num_list2 = [value*3 for value in range(3, 31)]
print(num_list2)

#4-8 Cubes 

num_list3 = [] 
for value in range(1, 11):
    num_list3.append(value**3)
print(num_list3)

#more comprehensive way 

num_list3 = [value**3 for value in range(1, 11)]
print(num_list3)

#asdasd