import numpy
from numpy import *
import time
n=array([],dtype=float64)
while True:
    try:
        #time.sleep(0.02)
        a=numpy.loadtxt("1.txt",dtype='str')
        print 'pos_x: ',a[0]
	print 'pos_y: ',a[1]
	print 'pos_z: ',a[2]
	print 'yaw: ',a[3]
	print 'altittude: ',a[4]

	time.sleep(1) 
    except KeyboardInterrupt:
	break        
	time.sleep(0.01) 
