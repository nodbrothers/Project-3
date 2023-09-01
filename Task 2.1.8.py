def flavel(n,k):
   m = list(range(1,n+1))
   print(m)
   i = 0
   while len(m) != 1:
        if (i < len(m)) and (m[i] % k == 0) and (i != 0):
             print('i=',i)
             print(m[i])
             del m[i]
             print(m)
             
             i += 1
        elif i >= len(m)-1:
            print('hm')
            i = 0
        else:
            print('hmmm')
            i += 1
   return m[0]

n,k = int(input()), int(input())

print(flavel(5,2))

#1 2 3 4 5
#1 2    i=2
#1 3 4 5
#    