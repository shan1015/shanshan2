m=int(input())
l=input()
s=""
for i in l:
    if i!=" ":
        s=s+i
k=""
m=0
i=0
j=""
while i<len(s):
    if s[i]=="0" and s[i+1]=="0":
        i=i+1
    elif s[i]=="0":
        k=k+s[m:i]
        m=i+1
        i=i+1
    else:
        i=i+1
for i in k:
    j=j+str(i)+" "

print(j.strip())
