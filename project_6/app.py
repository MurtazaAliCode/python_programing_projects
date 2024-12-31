print("\t=========================={project of countdown timmer}=============================\n")

import time

def countdowntimer(Time):

    while Time:       
        minuts, seconds = divmod(Time, 60)
        timer = '{:02d}:{:02d}'.format(minuts, seconds)
        print(timer, end="\r")
        time.sleep(1)
        Time -= 1
       
    print('Timer completed!')

countdowntimer(5)
      