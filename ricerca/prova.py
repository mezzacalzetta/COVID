import sys
import re
import string
import os
import glob
import os, fnmatch
REGIONI="REG"
PROOVINCE=""	
files=glob.glob("*.log")
files=   glob.glob("../../../")
files=fnmatch.filter(os.listdir('../../../COVID-19/GRPH/'), 'REGION*')
for file in files :
	REGIONI=REGIONI+","+ file
print (REGIONI)


