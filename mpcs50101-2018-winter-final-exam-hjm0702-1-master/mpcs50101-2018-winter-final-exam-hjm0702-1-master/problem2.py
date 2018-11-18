# Problem 2
#
# What is the worst-case complexity, in Big-O notation, of the following code
# snippets?

# A.
for i in range(n):
     print i


# B.
for i in range(10000000):
     print i


# C.
for i in range(n * n):
    print i


# D.
for i in range(n):
   print i
for j in range(n):
   print j


# E.
for i in range(n):
   for j in range(n):
       for k in range(n):
           print i,k,j


# F.
for i in range(n):
   for j in range(k*k):
      print i*j


# G.
i = 1
while i < n:
    print i
    i = i * 2


# H.
map(lambda x: x * x * x, numbers)


# I.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]
print filter(lambda x: x in prime, numbers)


# J.
reduce(lambda x, y: x if x > y else y, numbers)
