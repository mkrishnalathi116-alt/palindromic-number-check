def palindrome_numcheck(num) :
   num=int(input("enter a number"))
   absnum=abs(num)
   rev=absnum%10
   num=absnum//10
   while absnum>0 :
      r=num%10
      num=num//10
      rev=rev*10+r
   if num<=0:
      rev=rev-2*rev
   if num==rev:
      print(f"the number {num} is a palindrome")
   else:
      print(f"the number {num} is not a palindrome")
               
