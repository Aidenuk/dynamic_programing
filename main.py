
# understand dynamic programming [recursive, memoization and divide and conquer]

# make the number to be 1 
x = 6

d = [0] * 30001

for i in range(2, x+1):
  
  d[i] = d[i-1] +1
  if i % 2 == 0:
    d[i] = min(d[i],d[i//2] +1)
  if i % 3 == 0:
    d[i] = min(d[i],d[i//3] +1)
    
  if i % 5 == 0:
    d[i] = min(d[i],d[i//5] +1)


print(d[x])

#colonise the house [개미전사]

n = 4

array = list(map(int,input().split()))

d = [0] * 100
d[0] = array[0]
d[1] = max(array[0],array[1])

for i in range(2,n):
  d[i] = max(d[i-1],d[i-2] + array[i])

print(d[n-1])

