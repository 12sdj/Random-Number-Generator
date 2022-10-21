#Version 1.0.2_Alpha03
from random import*
from time import*
begin = int(input("Please enter a smaller value: "))
end = int(input("Please enter a larger value: "))
interval = int(input("Please enter the time interval for each output: "))
while(True):
    number = randint(begin,end)
    print(number)
    number = 0
    sleep(interval)
