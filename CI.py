import subprocess
import datetime
import unittest
from test import NombresRomainsTest

branch = "dev"

# Pull dev
print("----------------------------------------------------------------------")
subprocess.run(f"git pull origin {branch}", shell=True)
print("----------------------------------------------------------------------")

# Test
tests = unittest.TestLoader().loadTestsFromTestCase(NombresRomainsTest.MyTestCase)
tests_result = unittest.TextTestRunner(verbosity=2).run(tests)
print("----------------------------------------------------------------------")


# Si OK, Rebase + Fast Forward le commit testé sur "main"
if tests_result.wasSuccessful() == True:
   date = datetime.datetime.now().strftime("%d-%m-%Y")
   print(date)
   subprocess.run("git rebase main", shell=True)
   subprocess.run("git checkout main",shell=True)
   subprocess.run("git merge dev",shell=True)
   
# Sinon, exlure le commit de "dev" et le déplacer sur une branche "failure/<horodatage>"
else:
   date = datetime.datetime.now().strftime("%Y-%m-%d")   
   
   subprocess.run(f"git checkout -b failure/{date}",shell=True)  
   subprocess.run("git reset HEAD", shell=True)   
   subprocess.run(f"git checkout failure/{date}",shell=True)
   subprocess.run("git cherry-pick HEAD", shell=True) 

print("fin.")