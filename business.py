def fun(l):
    return l[2]


hours = int(input())
bn = int(input())

mat = []
for i in range(bn):
    mat.append(list(input().strip().split()))

mat.sort(reverse=True, key=fun)

print(mat)

meetings = mat[0][0]
hour = int(mat[0][1])
profit = int(mat[0][2])
i = 1
while i<len(mat) and hour<hours:
    
    meetings += mat[i][0]
    profit += int(mat[i][2])
    hour += int(mat[i][1])
    i+=1

    
print(' '.join(list(meetings)))
print(profit)



'''
maxi = [0, '']
for i in mat:
    max = [int(i[2]), i[0]]
    hour = int(i[1])
    for j in mat:
        if i!=j:
            if int(j[1])+hour <= hours:
                max[0]+=int(j[2])
                max[1]+=j[0]
    if max[0]>maxi[0]:
        maxi = max

print(' '.join(list(maxi[1])))
print(maxi[0])
'''


