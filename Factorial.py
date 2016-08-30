import numpy

x = 4
n = x

while n > 1:
  x = x * (n - 1)
  n = n - 1
  if (n == 0):
    break

print x
