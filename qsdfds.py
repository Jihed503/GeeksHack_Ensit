import numpy as np

nb_l, nb_c = list(map(int, input().strip().split()))
pos_gx, pos_gy, pos_px, pos_py = list(map(int, input().strip().split()))
nb_obstacle = int(input().strip())
obstacles_list = []
for o in range(nb_obstacle):
    obstacles_list.append(tuple(map(int, input().strip().split())))
    
    mat_pic = np.zeros((nb_l, nb_c))
    mat_pic[pos_gx, pos_gy] = 1 # ghost
    mat_pic[pos_px, pos_py] = 2 # player
    for t in obstacles_list:
        mat_pic[t] = 3 # obstacle


print(nb_l, nb_c, pos_gx, pos_gy, pos_px, pos_py , obstacles_list)
'''
limit_list=[]
i = pos_gx-1
while i <= pos_gx+1 and i:
    j = pos_gy-1
    while j <= pos_gy+1:
        try:
            if mat_pic[i,j] != 1:
                limit_list.append(mat_pic[i,j])
        except:
            j+=1
        print(i)
        
    i+=1
print(limit_list)
'''
limit_list=[]
    
for i in range(pos_gx-1, pos_gx+2):
    
    for j in range(pos_gy-1, pos_gy+2):
        print(i,j)
        if i>=0 and i<nb_l and j>=0 and j<nb_c and mat_pic[i,j]!=1:
            print(mat_pic[i,j])
            limit_list.append(mat_pic[i,j])

print(limit_list)
