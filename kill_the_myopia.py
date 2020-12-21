import time

def main():
    nbLap = 0
    while True:
        time.sleep(1200) #1200 secondes -> 20 minutes
        pause()
        nbLap += 1
        print("You took", nbLap, "breaks")


def pause():
    pauseTime = 300 #300 secondes -> 5 minutes
    while pauseTime:
        min, sec = divmod(pauseTime, 60)
        printformat = '{:02d}:{:02d}'.format(min, sec)
        print(printformat, end='\r')
        time.sleep(1)
        pauseTime -= 1
    print("You can come back !")

if __name__ == "__main__":
    print("Welcome in Kill The Myopia !")
    main()
