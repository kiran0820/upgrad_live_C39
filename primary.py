# This is the primary file
from summation import summation

if __name__=="__main__":
    x = input("Enter any integer: ")
    y = input("Enter an Integer to be added with x: ")
    print("Result if X + Y is:==> {}".format(summation(x,y)))