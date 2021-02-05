##Computers and Python
##Functions

#Four reasons to use functions
#1. Organize programs by grouping chucks of code
#2. reUSE code in multiple places or SHARE with friends
#3. Improves READIBILITY and TESTING
#4. 

#For the following function..
#arguments: 3 and 4
#parameters:  a and b 
#results: x will be 7
def add_two(a, b):
    x = a + b
    return x

add_two(3, 4)


##
def my_ave(*args):
    #print(type(args))
    count = 0
    sum = 0
    for n in args:
        count += 1
        sum += n
    return(sum / count)

