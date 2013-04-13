#	Created by Caleb Coffie
#	Used to expendite the process of testing and
#	and debugging on the XO

os.system("git pull")

os.system("sudo python setup.py build")
os.system("sudo python setup.py dist_xo")

os.system("sugar-install-bundle OpenVideoChat-1.xo")

os.system("echo \"---------------\" >> ErrorLog.txt")
os.system("date >> ErrorLog.txt")
os.system("echo \"---------------\" >> ErrorLog.txt")


os.system("sugar-launch org.laptop.OpenVideoChat &>> ErrorLog.txt")

os.system("git add ErrorLog.txt")
os.system("git commit -m\"Updating Error Log.\"")

os.system("git push")
