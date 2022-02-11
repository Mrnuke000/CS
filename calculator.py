total = 0
count = 1


print('calculator!!')
print('enter 0 if you want to stop')
print('')

while True:
  if count == 0:
    num = int(input('input a number... '))
  else:
    num = int(input('input another number... '))
  
  if num == 0:
    print('ok - bye')
    break

  if num != 0:
    t = input('what operation?  ')




  if t == ('+'):

    total = total + num
    count = count + 1
  elif t == ('/'):
    total = total / num
    count = count + 1
  elif t == ('-'):
    total = total - num
    count = count + 1
  elif t == ('*'):
    total = total * num
    count = count + 1
  elif t == ('average'):
    total = total + num 
    count = count + 1


if t == ('average'):
  total = total / count
  print('your average is ' +str(total))
else:
  print('your total is ' +str(total))
