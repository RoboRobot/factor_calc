list = []
def factor(x):
  for y in range (1,x+1):
    z = bool(x % y == 0)
    if z == True:
      list.append(y)
  for a in range (0,(len(list)/2)):
    print("%s,%s" %(list[a],list[len(list)-(a+1)]))
    
  print(list)

if len(list) == 2:
  print("Prime")
  
factor(90)
