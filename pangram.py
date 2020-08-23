# program to check whether given string is pangram or not
import string #importing string from directory
# create a usermade function 
def check(str):
   letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
   for char in letters:
      if char not in str.lower():
         return 0
   return 1
# main
string=eval(input("enter a string"))
if(check(string) == 1):
   print("Given string is pangram")
else:
   print("Given string is not a pangram")
