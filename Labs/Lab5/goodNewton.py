def driver():
    a = -1
    b = 1.5

    f = lambda x: (x-1)*(x-1)
    fprim = lambda x: 2(x-1)

    [astar, ier] = bisection(f, fprim, a, b)

def bisection(f, fprim, a, b):


    fa = f(a)
    fb = f(b)
    if (fa*fb>0):
       ier = 1
       astar = a
       return [astar, ier]

#   verify end points are not a root 
    if (fa == 0):
      astar = a
      ier = 0
      return [astar, ier]

    if (fb ==0):
      astar = b
      ier = 0
      return [astar, ier]

    d = 0.5*(a+b)
    while (fprim(d)>1):
      fd = f(d)
      if (fd ==0):
        astar = d
        ier = 0
        return [astar, ier]
      if (fa*fd<0):
         b = d
      else: 
        a = d
        fa = fd
      d = 0.5*(a+b)
#      print('abs(d-a) = ', abs(d-a))
      
    astar = d
    ier = 0
    return [astar, ier]


driver()