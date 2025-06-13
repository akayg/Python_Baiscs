import os 
os.mkdir("osmodule")
with open("osmodule/file.txt","w") as f:
    f.write("Module 11 content")


os.remove("osmodule/file.txt")
os.rename("osmodule","renamed")
os.rmdir("renamed")