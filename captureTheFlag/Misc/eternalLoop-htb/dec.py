import os

workdir = os.getcwd()
curdir = workdir
gooddir=workdir
go = True
while (go):
    go=False
    print("going down the rabbit hole")
    files = os.popen("cd " + curdir + "; ls").read()
    files = files.split("\n")
    for file in files:
        if ".zip" in file:
            print(file)
            infile = os.popen("cd " + curdir + "; unzip -l " + file + "|grep '.zip'").read().split(" ")[-1].split(".")[
                0]
            print(infile)
            status = os.popen("cd " + curdir + "; unzip -P " + infile + " -d " + infile + " " + file).read()
            print(status)
            if infile:
                gooddir=curdir
                curdir = os.path.join(curdir, infile)
                go=True
            infile=None
        else:
            # go=False
            break
print("loop finished completely")
os.system("nautilus "+gooddir)

