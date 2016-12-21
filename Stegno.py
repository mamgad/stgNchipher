print"         __        _   __     _       __\n   _____/ /_____ _/ | / /____(_)___  / /_  ___  _____\n  / ___/ __/ __ `/  |/ / ___/ / __ \/ __ \/ _ \/ ___/\n (__  ) /_/ /_/ / /|  / /__/ / /_/ / / / /  __/ /\n/____/\__/\__, /_/ |_/\___/_/ .___/_/ /_/\___/_/\n         /____/            /_/\n                       "




file_loc=raw_input("file name:\n");
message=raw_input("message");
print "Opening file %s" % file_loc
fileRead = open(file_loc, 'r')
content = bytearray(fileRead.read())
fileRead.close()
print bytearray(content);
fileWrite = open("R"+file_loc,'w')
msg_pointer=0;
i=0

while (i<len(content)and msg_pointer<len(message)):
    print (str(content[i+2000])+",")
    if content[i+2000]>64:
        print message[msg_pointer]+"HEREE"
        content[i+2000]=(ord(message[msg_pointer])+content[i+2000])%255


        msg_pointer+=1

    i+=1

print content;
print "\n\n\n\n.."
fileWrite.write(content);
fileWrite.close()
