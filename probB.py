def GO(NK):
    gallery = []
    n = int(NK[0])
    k = int(NK[1])
    for i in range(0, n):
        gallery.append(input("").split())   
    gallery = sum(gallery, [])
    for i in range(0, n*2):
        gallery[i]=int(gallery[i])
    a, b, c = n, k+1, 3
    cache = [[[-100 for x in range(0,c)] for y in range(0,b)] for z in range(0,a)]
    cache[0][0][0] = -100
    cache[0][0][1] = -100
    cache[0][0][2] = gallery[0] + gallery[1]
    for i in range(1, n):
      cache[i][0][0] = -100
      cache[i][0][1] = -100
      cache[i][0][2] = cache[i - 1][0][2] + gallery[2*i] + gallery[2*i + 1]
    if k > 0:
      cache[0][1][0] = gallery[1]
      cache[0][1][1] = gallery[0]
      cache[0][1][2] = -100
    for i in range(1, n):
        for j in range(1, min(i+1,k) + 1):
          cache[i][j][0] = gallery[2*i + 1] + max(cache[i - 1][j - 1][2], cache[i - 1][j - 1][0])
          cache[i][j][1] = gallery[2*i] + max(cache[i - 1][j - 1][2], cache[i - 1][j - 1][1])
          cache[i][j][2] = gallery[2*i] + gallery[2*i+1] + max(cache[i - 1][j][0], max(cache[i - 1][j][1], cache[i - 1][j][2]))
    answer = max(cache[n - 1][k][0], max(cache[n - 1][k][1], cache[n - 1][k][2]))
    print(answer)

NK = [100,100]
while int(NK[0])+int(NK[1])>0:
    NK = input("").split()
    if int(NK[0])+int(NK[1])>0:
        GO(NK)