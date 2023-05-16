import time

def pomodoro_timer(minutes):
    """
    A simple Pomodoro timer that takes a specified number of minutes as input

    and counts down to zero, displaying how much time is left every second.
    """
    seconds = minutes * 60

    while seconds > 0:
        m, s = divmod(seconds, 60)
        time_left = f'{m:02d}:{s:02d}'
        print(f'Time left: {time_left}', end='\r')
        time.sleep(1)
        seconds -= 1

    print('Time is up!')
if __name__ == '__main__':
    pomodoro_timer(25) # 25 minute Pomodoro session
