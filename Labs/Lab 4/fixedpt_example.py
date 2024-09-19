# import libraries
import numpy as np
    
def driver():

# test functions 
     f1 = lambda x: 1+0.5*np.sin(x)
# fixed point is alpha1 = 1.4987....

     f2 = lambda x: 3+2*np.sin(x)
#fixed point is alpha2 = 3.09... 

     Nmax = 100
     tol = 1e-8

# test f1 '''
     x0 = 0.0
     [xstar,ier, guesses] = fixedpt(f1,x0,tol,Nmax)
     print('')
     print('the approximate fixed point is:',xstar)
     print('f1(xstar):',f1(xstar))
     print('Error message reads:',ier)
     
     if ier == 0:
        [fit, diff1, diff2] = convergence(xstar, guesses)
    
#test f2 '''
     x0 = 0.0
     [xstar,ier, guesses] = fixedpt(f2,x0,tol,Nmax)
     print('the approximate fixed point is:',xstar)
     print('f2(xstar):',f2(xstar))
     print('Error message reads:',ier)
     if ier == 0:
        [fit, diff1, diff2] = convergence(xstar, guesses)

# define routines
def fixedpt(f,x0,tol,Nmax):
    guesses = np.zeros((Nmax,1))
    ''' x0 = initial guess'''
    ''' Nmax = max number of iterations'''
    ''' tol = stopping tolerance'''

    count = 0
    while (count <Nmax):
       x1 = f(x0)
       count = count +1
       if (abs(x1-x0) <tol):
          xstar = x1
          ier = 0
          return [xstar,ier, guesses]
       guesses[count-1] = x1
       x0 = x1
    
    xstar = x1
    ier = 1
    return [xstar, ier, guesses]
    
def convergence(xstar, guesses):
    diff1 = np.abs(guesses[1::]-xstar)
    diff2 = np.abs(guesses[0:-1]-xstar)
   # print("diff1: ")
    #print(diff1)
   # print("diff2: ")
    #print(diff2)
    
    fit = np.polyfit(np.log(diff2.flatten()),np.log(diff1.flatten()),1)
    print('')
    print("Order")
    print("(log|p_{n+1}-p|) = log(lambda) + alpha*log|p_{n}-p| where")
    print("lambda = " + str(np.exp(fit[1])))
    print("alpha = " + str(fit[0]))
    return [fit, diff1, diff2]
    

driver()
