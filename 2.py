n = int(input()) # tribonachi
def my_function (n):

     if  n == 2 or n == 1:
        return 1

     if(n == 0):
        return 0

     return my_function(n-1)+ my_function(n - 2) + my_function(n -3)

print(my_function(n))



