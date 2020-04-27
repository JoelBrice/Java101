import socket

port = 1234

def getSocketConnection():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try: ### Try to connect to the network
        s.connect((socket.gethostname(), port))
    except e: ## Any error?
        e.connectionError() ## Show the error here

    s.listen(80)

full_msg = " "

def getMessage(message):
    message = full_msg
    while getSocketConnection():
        msg = s.recv(8)
        if len(msg) <=0:
            break
        message += msg.decode("utf-8")
    return message
    

def printMessage():
    getSocketConnection()
    getMessage(full_msg)
    print(full_msg)


printMessage()
