# compare n to this number
x = int(input('input comparison num: '))

# loop from 0 to n-1
n = int(input('enter loop num: '))


for i in range(0, n-1) :

  if i < x:
    print(str(i) + ' is less than ' + str(x))
  if i == x:
    print(str(i) + ' is equal to ' + str(x))
