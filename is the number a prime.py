num = int 
num = input ("what is num: ")
if num == 2:
    print ("true")
if num > 2:
    for i in range (2, num):
        if num % i == 0:
            print ("false")
            break
        else:
            print ("true")
            break