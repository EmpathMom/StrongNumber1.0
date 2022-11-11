## 
# Author :  Gaylene
# Created by : Gaylene
# Architect(s): Gaylene
# Developer(s): Gaylene
# Created Date: 11/8/22
# Description : Edit to Fibonacci with class
# Version: 2.0
# Modified by:Gaylene
# Modified Date: 11/9/2022
# Description: Assignment class and definitions for  change assignments
#
##Write program  for if a strong number or not

##### WILL RUN ####

#N = int(input("Enter a number: "))  #get user input
#sum = 0 #  initialize variable to store factorial of N
#temp_N = N  #value of n gets stored here
#Last_digit = N %10 #store factorial for last digit in variable

#while(N): 
    #k = 1
   # fact = 1 #last digit stored in variable
   # r = N % 10
   # while(k <= r):
    #    fact = fact * k
    #    k = k + 1
 #   sum = sum + fact #every time the sum of the factorial is found needs to be added to sum
#    N = N//10 #input number needs to be reduced by / 10
#if(sum == temp_N):
 #   print(str(temp_N) + " is a strong number")
#else:
 #   print(str(temp_N) + " is not a strong number")



#cant figure out why it wont run. 


##class Strong():
##   
##    def isStrong(self):
##        N = int(input("please enter number:"))
##        sum = 0
##        temp_N = N
##        last_digit = N%10
##        
##        while (N):
##           k=1
##           fact=1
##           r=N%10
##        while(k<=r):
##            fact=fact*k
##            k=k+1
##            sum=sum +fact
##            N=N//10
##        if(sum==temp_N):
##            print(str(temp_N) + "its a strong number")
##        else:
##            print(str(temp_N)+ "is not a strong number")
##st = Strong()
##st.isStrong()







#also wont run

class Strong_num:
   
    def __init__(self,num):
        self.num = num
    def isStrong(self):
        sum1 = 0
        temp = self.num
        n = int(input("please enter number:"))
        while temp > 0:
            digit = temp % 10 #extracting the last digit of number and storing in a variable called digit
            if (digit == 0 or digit == 1) or (digit !=0 and self.num % digit==0):#checking whether the digits are divisible by itself or not 
                sum1 += 1 #adding to the sum if it is true 
            else:
                return False #returning false if any one of them is not divisible by itself 
            temp //= 10 # dividing the number by 10 to get the next digit from right side  
            if sum1 == len(str(self.num)): # checking whether length of string equals to sum which i have calculated above 
                print("The given number ",self.num,"is a strong number")# print statement when all conditions are satisfied 
            else:
                print("The given number",self.num,"is not a strong number")

st = Strong_num()
st.isStrong() 