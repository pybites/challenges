#!python3
#An app to provide random troubleshooting steps. Probably right half the time!

import time
import random

STEPS_LIST = ('SHUFFLE THE DIMMS',
            'POWER DRAIN THE HOST',
            'STRESS TEST THE HOST',
            'RUN CPU AND MEMORY TESTS SEPARATELY',
            'RUN MEMTEST',
            'RTFM',
            'RETURN TO MINIMUM CONFIG',
            'REPLACE EVERY DIMM, EVERY CPU AND THE MOTHERBOARD',
            'CALL AN EXORCIST')


def intro_message():
    print('Team Awesome proudly presents...\n')
    time.sleep(2)

    print('THE TROUBLESHOOTING WHEEL OF MISFORTUNE'.center(80, '*') + '\n')
    time.sleep(2)

    print('Having trouble fixing a host?\n')
    time.sleep(2)

    print("With just one fantabulous spin of THE TROUBLESHOOTING WHEEL OF MISFORTUNE (tm), we'll have you on your way!")
    time.sleep(4)

def spin():
    input('\nGive the wheel a spin! (Hit Enter)')
    print('Spinning...')
    time.sleep(2)
    print('\n' + STEPS_LIST[random.randint(0, len(STEPS_LIST) -1)])
    print('\nNow get out there and fix that mofo!\n')

def main():
    intro_message()

    while True:
        spin()
        answer = input('Want another spin? (N to quit) ')
        if answer.upper() == 'N':
            break

if __name__ == "__main__":
    main()
