#user will choose afile and 
#and search how many line start with 
#specific name but this code if the file not exciste
#then the code with not blow up

fname =input("enter the name of the file")
try:
    fhand =open(fname)
except:
    print ("can not open this: ",fname)
    quit()
count = 0
for line in fhand:
    if line.startswith("x")
    count =count+1
    print("there were",count,"subject lines in",fname)
