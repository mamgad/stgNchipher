print '         __        _   __     _       __             \n   _____/ /_____ _/ | / /____(_)___  / /_  ___  _____\n  / ___/ __/ __ `/  |/ / ___/ / __ \/ __ \/ _ \/ ___/\n (__  ) /_/ /_/ / /|  / /__/ / /_/ / / / /  __/ /    \n/____/\__/\__, /_/ |_/\___/_/ .___/_/ /_/\___/_/     \n         /____/            /_/                       '


fileA = open('b.mp3', 'r')
fileB= open ('Rb.mp3','r')
A = fileA.read()
B = fileB.read()
counter=0
message=''
for i in range(0,10000) :
   if ord(B[i])-ord(A[i])!=0:
       char= ord(B[i])-ord(A[i])
       if char < 0:
           char = char +255

       print "ok"
       #print char
       message=message+chr(char)
print "done"
print "Decipthered message is :"
print message