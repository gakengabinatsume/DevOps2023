#import os
#path = '/app/CV.pdf'
#os.system(path)
import subprocess
path = '/app/CV.pdf'
subprocess.Popen([path], shell=True)
