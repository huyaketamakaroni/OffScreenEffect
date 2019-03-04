#!/usr/bin/python
import cgi
import sys
import urlparse
import json 
import serial 
import csv
import socket
import datetime

#host = "192.168.6.105"
#port = 6789
#client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#client.connect((host, port))
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from datetime import datetime as dt

num = ""
listData = []
lastDirc = "1000"
lastnum = "1192"

ser = serial.Serial('COM3',9600,timeout=1)

PORT_NUMBER = 80

tdatetime = dt.now()
fname = tdatetime.strftime('data/%Y%m%d-%H%M%S.csv')
print "---------------------------------------------"
print fname
f = open(fname, 'ab') 
csvWriter = csv.writer(f)
listData = []
listData.append("#num")
listData.append("mode")
listData.append("pattern")
listData.append("answer")
listData.append("duration")
csvWriter.writerow(listData)

#httpd = HTTPServer(('', 8001), MyHandler)
#httpd.serve_forever()

#This class will handles any incoming request from
#the browser
class myHandler(BaseHTTPRequestHandler):
        #turn off log_message
        def log_message(self, format, *args):
            return
        
        def do_GET(self):
            global num
            body = '<script>setTimeout("location.reload()",200);</script><p style="font-size:500px;text-align:center;"> ' + num + '</p>'
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            #self.send_header('Content-length', len(body))
            self.end_headers()
            self.wfile.write(body.encode('utf-8'))
            
        def do_POST(self):            
                #with serial.Serial('COM3',9600,timeout=1) as ser:
                global num           
                global lastDirc
                global lastnum
                
                #if(lastnum != num):
                    #client.send(num)
                    #client.send("end")
                    #lastnum = num
                
                #print("post!")
                content_len = int(self.headers.get('content-length'))
                requestBody = self.rfile.read(content_len).decode('UTF-8')
                
                
                data = json.loads(requestBody)
                
                if(data["numFlag"] != "False"):
                        num = data["num"]
                else:
                        num = ""
                
                if(data["enter"] == "True"):
                    global f
                    f.close()
                    tdatetime = dt.now()
                    fname = tdatetime.strftime('data/%Y%m%d-%H%M%S.csv')
                    print "\n---------------------------------------------"
                    sys.stdout.write("\n" + fname + "\n")
                    f = open(fname, 'ab')
                    global csvWriter
                    csvWriter = csv.writer(f)
                    global listData
                    listData = []
                    listData.append("#num")
                    listData.append("mode")
                    listData.append("pattern")
                    listData.append("answer")
                    listData.append("duration")
                    csvWriter.writerow(listData)

                if(data["durationFlag"] != "False"):
                    listData = []
                    listData.append(data["num"])
                    listData.append(data["mode"])
                    listData.append(data["pattern"])
                    listData.append(data["answer"])
                    listData.append(data["duration"])
                    csvWriter.writerow(listData)          
                    #f.close()
                    print("\nnum: " + data["num"] + ", mode: " + data["mode"] + ", answer: " + data["answer"] + ", duration: " + data["duration"])
              
            
                direction = data["direction"]
                flag = ""
                sys.stdout.write("\r[%s] mode: %s, pat: %s, phase: %s, debug: %s, dir: %s(%s), num: %s\t\t\t" % (data["trial"], data["mode"], data["pattern"], data["phase"], data["debug"], direction, data["directionFlag"], num,))
                if(data["directionFlag"] != "False"):
                    #print(direction+'\r\n'.rstrip('\n'))
                    if(direction == "right"):
                        flag = "r"
                    elif(direction == "upperRight"):
                        flag = "U"
                    elif(direction == "up"):
                        flag = "u"
                    elif(direction == "upperLeft"):
                        flag = "L"
                    elif(direction == "left"):
                        flag = "l"
                    elif(direction == "downerLeft"):
                        flag = "D"
                    elif(direction == "down"):
                        flag = "d"
                    elif(direction == "downerRight"):
                        flag = "R"
                    elif(direction == "TurnLeft"):
                        flag = "C"
                    elif(direction == "TurnRight"):
                        flag = "c"
                    else:
                        flag = "N"
                else:
                        flag = "N"
                    
                #print(flag)
                if(lastDirc != flag):
                    #change LED power
                    ####################
                    #num = "1"
                    #ser.write(num)
                    ####################
                    ser.write(flag)
                    #ser.write((flag+":"+ num +"*").encode())
                    #print((flag+":"+ num +"*").encode())
                    lastDirc = flag
                    #print(flag)
                

            
try:
	#Create a web server and define the handler to manage the
	#incoming request
	server = HTTPServer(('', PORT_NUMBER), myHandler)
	print 'Started httpserver on ', socket.gethostbyname(socket.gethostname()) ,' port ' , PORT_NUMBER
	
	#Wait forever for incoming htto requests
	server.serve_forever()

except KeyboardInterrupt:
	print '^C received, shutting down the web server'
	server.socket.close()
    
    
        #f = open('Data.csv', 'ab') 

        #csvWriter = csv.writer(f)
        
        #listData.append("1")                      
        #listData.append("2")
        
        #print(listData)
        #for listdata in listData:
        #    csvWriter.writerow(listdata)          

        #f.close()    
    


    
