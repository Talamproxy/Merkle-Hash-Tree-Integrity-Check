import os
from datetime import datetime

startTime = datetime.now()

for x in range(1,5001):
    updater = open('commit-py.txt', 'w')
    updater.write("auto-commit "+str(x)+"\n")
    updater.close()
    
    os.system("git add --all")
    os.system('git commit -am "auto-commit '+str(x)+'"')

runTime = datetime.now()-startTime
print(runTime)
updater = open('commit-py.txt', 'w')
updater.write("auto-commit.py\n5000 commits in 0"+str(runTime)+"\n")
updater.close()

os.system("git add --all")
os.system('git commit -am "auto-commit.py time"')
