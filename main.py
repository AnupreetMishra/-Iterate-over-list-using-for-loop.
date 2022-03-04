#  Take inputs from user to make a list. Again take one input from user and
# search it in the list and delete that element, if found. Iterate over list using for
# loop.


a=[]
elements=int(input("Enter a length of list:"))
for i in range(1,elements+1):
  num=int(input("Enter the number:"))
  a.append(num)
print("List is:",a)


delnum=int(input("Enter the number for delete:"))
if(delnum in a):
  a.remove(delnum)
  print(a)

else:
  print(a)