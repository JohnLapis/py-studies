import time
from pygame import mixer
from pygame.mixer import music

def time_converter(delay):
    if delay[len(delay) - 1] == 's':
        return int(delay[:-1])
    elif delay[len(delay) - 1] == 'n':
        return int(delay[:-3])
                   
def alarm(delay, times, song):
    mixer.init()
    if song == None: song = '/usr/share/cinnamon/sounds/bell.ogg'
    if times == 0:
        while True:
            time.sleep(time_converter(delay))
            music.load(song)
            music.play(0)
    else:
        for i in range(times):
            time.sleep(time_converter(delay))
            music.load(song)
            music.play(0)
             
def main():
    print('How many times would you like the alarm the repeat? 0 for indefinitely')
    times = int(input())
    print("Enter the interval either in seconds (Xs) or minutes (Xmin):")
    interval = input()
    user_response = input("Would you like  want a specific song playing [Y/N]?")
    song = None
    if user_response .upper() == 'Y':
         song = input("Specify path to the file: ")
    alarm(interval, times, song)

if __name__ == '__main__':
    main()
