import math
from mpi4py import MPI
import time

def compute_pi(n,start=0,step=1):
    h=1.0/n
    s=0.0
    for i in range(start,n,step):
        x=h*(i+0.5)
        s+=4.0/(1.0+(x*x))
    return s*h

first=time.time()
comm=MPI.COMM_WORLD
nprocs=comm.Get_size()
myrank=comm.Get_rank()

if myrank==0:
    n=100000000
else:
    n=None

n=comm.bcast(n,root=0)

mypi=compute_pi(n,myrank,nprocs)

pi=comm.reduce(mypi,op=MPI.SUM,root=0)

if myrank==0:
    error=abs(pi-math.pi)
    print "pi is approx %0.16f, and error is %0.16f" %(pi,error)

    print time.time()-first

