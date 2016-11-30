
import sys
import http.client

# define the function blocks
def start():
    print ("START command.\n")
    hR = "/"
    print("1")
    conn = http.client.HTTPConnection('localhost:5000')
    print("2")
    conn.connect()
    print("3")
    conn.request("GET",hR)
    print("4")
    response = conn.getresponse()
    print("5")
    data = response.read()
    print("6")
    print (data)
    print("7")
    conn.close()

def stop():
    print ("STOP command\n")

# map the inputs to the function blocks
options = {"start" : start,
           "stop" : stop
}


options[str(sys.argv[1])]()