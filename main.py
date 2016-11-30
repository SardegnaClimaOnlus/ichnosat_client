
import sys
import http.client


def request(hR):
    conn = http.client.HTTPConnection('localhost:5000')
    conn.connect()
    conn.request("GET", hR)
    response = conn.getresponse()
    data = response.read()
    print (data)
    conn.close()

def start_scientific_processor():
    print ("START scientific-processor command.\n")
    request("/start-scientific-processor")


def notify_scientific_processor():
    print ("START scientific-processor command.\n")
    request("/notify-scientific-processor")


def stop():
    print ("STOP command\n")

# map the inputs to the function blocks
options = {"start-scientific-processor" : start_scientific_processor,
           "notify-scientific-processor" : notify_scientific_processor,
           "stop" : stop
}


options[str(sys.argv[1])]()