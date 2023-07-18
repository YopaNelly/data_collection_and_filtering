# Input collection

#stage 1

len = int(input("Enter the length of your list: "))

my_list=[]

num = 0

for i in range(0, len):
    print("Enter the number at possition ", i, ":")
    num = int(input())
    my_list.append(num)

print("Your list is: ", my_list)

#stage 2

def filter_every_numbers(list):
    even_numbers = []
    for i in list:
        if i%2 == 0:
            even_numbers.append(i)
    return even_numbers


#stage 3

print("The even numbers are: ", filter_every_numbers(my_list))






