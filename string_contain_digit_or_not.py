s=input()
a="0123456789"
count=0
for i in s:
    if i in a:
        count+=1
if count==0:
    print("Doesn't contain digit")
else:
    print("Contains",count,"digit")
