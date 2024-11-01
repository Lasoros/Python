import time #gives timestamp

#print(time.time()) #gives floating point number since the "beginning of time"; this varies by OS Linux=01/01/1970

def send_emails():
    for i in range(10000):
        pass

start = time.time()
send_emails()
end = time.time()

duration = end - start

print(duration)