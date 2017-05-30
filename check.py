import os
import re

lst = os.listdir()

for filename in lst : 
    if (os.path.isdir(filename) != True) and  (re.search("\.mis", filename) != None) and (re.search("100", filename) != None) : 

        filein = filename   
        fileout1 = filename[0 : len(filename) - 4] + "_ewls.out"
        fileout2 = filename[0 : len(filename) - 4] + "_ewcc.out"
        ti = str(1000)
        print("test ewls for " + filein)
        os.system("ewls " + filein + " " + fileout1 + " " + ti)

        print("test ewcc for " + filein)
        os.system("ewls " + filein + " " + fileout2 + " " + ti)

    


