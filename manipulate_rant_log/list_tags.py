#!/opt/local/bin/python
# rant log manipulation
# Ben Payne <ben.is.located@gmail.com>
# 

import re

file_name='rants.tex'
file = open(file_name,'r')# open the xml file for reading
data = file.read()# convert to string
file.close()# close file because we dont need it anymore
#print(data)

# tags exist in the form
# \begin{loggentry}{YYYYMMDD}{tag1|tag2}
# pull out the tags into a list