
from  subprocess import call
call(['python', 'hackathon.py'])
f = open('output.txt', 'r')
output = ""
for line in f:
        output = output + line
print output
