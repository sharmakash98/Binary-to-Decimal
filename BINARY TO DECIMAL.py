num = input("Enter a Binary Number : ")
p = 0
newlist = 0
num_list = list(num)
for i in range(len(num_list),0,-1):   
   newlist = newlist + int(num_list[i-1])*pow(2,p)
   p = p+1
print("The Decimal Number is: ",newlist)
   

   
   
