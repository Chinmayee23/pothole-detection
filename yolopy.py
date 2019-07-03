#!python3
# import required packages

import subprocess

fp = "pothole/imgd/Fotolia_80750547_Subscription_Monthly_XL.jpg"
command = "${PWD}/darknet detector test -dont_show  pothole/pothole.data pothole/pothole.cfg pothole/backup/pothole_4000.weights -ext_output %s" % fp
proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
output = proc.stdout.read()

# Now we take out the output into python variable from C
print(output)

