N=int(input())
l=[]
for i in range(N):
    l.append(list(map(int, (input().strip().split()))))

ma=0
for i in (l):
    if max(i)>ma:
        ma=max(i)

li=[]
for i in range(N):
    lis=[]
    for j in range(ma+1):
        lis.append(0)
    li.append(lis)


for i in l:
    for j in i:
        li[l.index(i)][j]=1

# li
l=[]
test_contour = True
for i in range(len(li)):
    if i == 0 and li[i] != [1]*len(li[i]): test_contour = False
    elif  i == len(li)-1 and li[i] != [1]*len(li[i]): test_contour = False
            
    elif li[i][0] == 0 and  li[i][len(li)-1] == 0: test_contour = False
            
    elif 0 in li[i] : test_contour = False
print(test_contour)
if not test_contour:
    print(100*((len(li[0])+len(li))*2-4))
