import datetime
import time

st = input('Insert time to count down (h:m:s) ')

if len(st) == 8:
    if int(st.split(':')[0]) > 23:
        raise Exception("Hour is too large. ENTER AN HOUR LESS THAN 24!!!")

    h, m, s = 0, 0, 0
    date_time_obj = datetime.datetime.strptime(st, '%H:%M:%S')

    while True:
        if s > 59:
            s = 0
            m = m + 1
        if m > 59:
            m = 0
            h = h + 1
        l = datetime.datetime.strptime('{}:{}:{}'.format(h, m, s), '%H:%M:%S')
        if date_time_obj >= l:
            s += 1
            x = date_time_obj - l
            remaining_time = '{:02d}:{:02d}:{:02d}'.format(x.seconds//3600, (x.seconds//60)%60, x.seconds%60)
            print(remaining_time, end='\r')
            time.sleep(1)
        else:
            print('Time is over !')
            break
else:
    print('please write input with correct format (00:00:00)')
