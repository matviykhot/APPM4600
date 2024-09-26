import numpy as np

def driver():
  a = -1
  b = 1.5

  f = lambda x: (x-1)**3
  fprim = lambda x: 3*(x-1)**2

  nMax = 100
  tol = 1.e-6

  [p, astar, ier, it] = bisection(f, fprim, a, b, nMax, tol)
  print('Approx: ', astar)
  print('Error: ', ier)
  print('Itterations: ', it)


def bisection(f, fprim, a, b, nMax, tol):
  count = 0

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
    count = count+1
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
      
  p0 = d

  p = np.zeros(nMax+1)
  p[0] = p0
  for it in range(nMax): # type: ignore
    p1 = p0-f(p0)/fprim(p0)
    p[it+1] = p1
    if (abs(p1-p0) < tol):
      pstar = p1
      ier = 0
      return [p,pstar,ier,it+count]
    p0 = p1
  pstar = p1
  ier = 1
  return [p,pstar,ier,it+count]
  


driver()