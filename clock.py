try:
    from time import sleep
    import random
    import playsound
    from datetime import datetime
finally:
    import os
    os.system('python -3 -m pip install playsound')
    os.system('python -3 -m pip install datetime')

alarm_sounds= ['beat1.wav']
print('Enter time in (HH:MM) format')
wake_up_time = input('What time would you like to wake up?\n')
curr_time = datetime.now().strftime("%H:%M")
while 1:
    if wake_up_time == curr_time:
        print('Time to wake up!')
        print('It\'s {0}'.format(curr_time))
        playsound.playsound(alarm_sounds)
        break
    else:
        print('You still have enough time go to sleep again.')
        print('Current time is {0}'.format(curr_time))
        sleep(10)
