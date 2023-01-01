
coun_file=open('countries.txt','r')
#print(coun_file.readable())
for files in coun_file.readlines():
    print(files)
coun_file.close()
