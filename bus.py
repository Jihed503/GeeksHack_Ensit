n, f, t, a = map(int, input().strip().split())

dist_fuel = []
for i in range(n):
    dist_fuel.append(list(map(int, input().strip().split())))

tickets = []
for i in range(a):
    tickets.append(list(map(int, input().strip().split())))



ticket_sum = 0
for l in tickets:
    ticket_sum += l[0]*l[1] + l[2]*l[3]



fuel_price = (f-t+dist_fuel[0][0])*dist_fuel[0][1] # 6 30
for i in range(1, n):
    #fuel_price += abs(dist_fuel[i][0]-dist_fuel[i-1][0])*dist_fuel[i-1][1] + abs(dist_fuel[i][2]-dist_fuel[i-1][2]*dist_fuel[i-1][3])
    fuel_price += dist_fuel[i][0]*dist_fuel[i][1] + dist_fuel[i][2]*dist_fuel[i-1][3]  
'''
while(i>0):
    i-=1
    fuel_price += dist_fuel[i][0]*dist_fuel[i][1]
'''

print(fuel_price)
print(ticket_sum)
print(ticket_sum-fuel_price)
 
