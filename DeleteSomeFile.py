import os
import re

root =  r"C:\Users\liuyu\Desktop\BussinessCard\Cards"
pattern = "pic_thumb"

#Delete some files with particular prefix
for i in os.listdir(root):
    if re.search(pattern,i,flags=0):
        os.remove(os.path.join(root,i))
        print("Already remove {}".format(i))

#Rename all the files
count = 1
for i in os.listdir(root):
    os.rename(os.path.join(root,i),os.path.join(root,"{}.jpg".format(count)))
    count+=1

print("Finish All!")
