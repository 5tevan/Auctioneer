import time
import os
import sys

if __name__ == "__main__":
	try:
        	pid = os.fork()
        	if pid > 0:
                	sys.exit(0)
     	except OSError, e:
        	sys.stderr.write("fork #1 failed: %d (%s)\n" % (e.errno, e.strerror))
        	sys.exit(1)
	
	# add code here
