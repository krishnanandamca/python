def compare(s1,s2,n):
    if s1[0:n]==s2[0:n]:
         return  True
    else:
          return  False
s1=str(input("enter the first string:"))
s2=str(input("enter the second string:"))
n=int(input("enter the first n characters:"))
res=compare(s1,s2,n)
print(res)