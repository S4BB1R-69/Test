#coding=utf-8
import os, sys, platform
os.system('rm -rf MEO.so')
 
try:
    if sys.argv[1]=='update':
        os.system('rm -rf MEO.so')
except:
    pass
 
 
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('MEO.so'):
        os.system('curl -L https://github.com/S4BB1R-69/Random/blob/main/MEO.cpython-311.so?raw=true -o MEO.so') 
        print("\1b[1;92mWELCOME TO MY NEW TOOLS ")
        import MEO
    else:
        import MEO
        
 
elif bit == '32bit':
    print(" SORRY 32 BIT NOT WORKING ")

