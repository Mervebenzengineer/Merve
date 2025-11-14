import time

while True:
    now=time.localtime()
    clock=time.strftime("%d.%m.%Y.-%H.%M.%S",now)

    print("Current time:",clock)
    
    time.sleep(10)



