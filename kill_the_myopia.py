import time
import subprocess

def sendmessage(message):
    subprocess.Popen(['notify-send', "Kill The Myopia",message])
    return

def main():
    nbLap = 0
    while True:
        noPause()
        pause()
        nbLap += 1
        print("You took", nbLap, "breaks")

def noPause():
    t = 10 #1200 secondes -> 20 minutes
    while t:
        min, sec = divmod(t, 60)
        printformat = '{:02d}:{:02d}'.format(min, sec)
        print(printformat, end='\r')
        time.sleep(1)
        t -= 1

    print('\007')
    print("-----")
    print("Break time")
    print("-----")
    sendmessage("Break time")

def pause():
    pauseTime = 5 #300 secondes -> 5 minutes
    while pauseTime:
        min, sec = divmod(pauseTime, 60)
        printformat = '{:02d}:{:02d}'.format(min, sec)
        print(printformat, end='\r')
        time.sleep(1)
        pauseTime -= 1

    print('\007')
    print("-----")
    print("Screen time")
    print("-----")
    sendmessage("Screen time")

if __name__ == "__main__":
    print("Welcome in Kill The Myopia !")
    main()