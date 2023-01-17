number = int(input("Enter number : "))
rev_num = 0

while(number > 0):
    rem = number % 10
    
    number = number // 10
    print(rem,end= " ")

