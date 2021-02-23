import time
import os
import subprocess
import multiprocessing
from playsound import playsound

def sendmessage(message):
    subprocess.Popen(['notify-send', "Kill The Myopia",message])
    return

def main():
    nbLap = 0
    while True:
        noPause()
        pause()
        nbLap += 1
        if nbLap == 1:
        	print("You took", nbLap, "break")
        else:
        	print("You took", nbLap, "breaks")

def noPause():
    t = 1200 #1200 secondes -> 20 minutes
    while t:
        min, sec = divmod(t, 60)
        printformat = '{:02d}:{:02d}'.format(min, sec)
        print(printformat, end='\r')
        time.sleep(1)
        t -= 1

    if os.path.exists('./soundalarm.mp3'):
    	p = multiprocessing.Process(target=playsound, args=("soundalarm.mp3",))
    	p.start()
    	input("press ENTER to continue")
    	p.terminate()
    	p.kill()
    else:
    	print('\007')
    	input("press ENTER to continue")
    print("-----")
    print("Break time")
    print("-----")
    sendmessage("Break time")

def pause():
    pauseTime = 300 #300 secondes -> 5 minutes
    while pauseTime:
        min, sec = divmod(pauseTime, 60)
        printformat = '{:02d}:{:02d}'.format(min, sec)
        print(printformat, end='\r')
        time.sleep(1)
        pauseTime -= 1

    if os.path.exists('./soundalarm.mp3'):
    	p = multiprocessing.Process(target=playsound, args=("soundalarm.mp3",))
    	p.start()
    	input("press ENTER to continue")
    	p.terminate()
    	p.kill()
    else:
    	print('\007')
    	input("press ENTER to continue")
    print("-----")
    print("Screen time")
    print("-----")
    sendmessage("Screen time")

if __name__ == "__main__":
    print("Welcome to Kill The Myopia !")
    try:
    	main()
    except KeyboardInterrupt:
    	print('')
    	print('Thanks for using Kill The Myopia ! See you soon :)')
    	os._exit(0)
