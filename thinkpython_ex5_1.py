import time

def epoch():
    days = ((time.time() / 60) / 60) / 24
    hours = (float(days) - int(days)) * 24
    min = (float(hours) - int(hours)) * 60
    sec = (float(min) - int(min)) * 60
    # print(int(hours),':', int(min),':', int(sec),',', int(days))
    print(f'{int(hours)}:{int(min)}:{int(sec)},{int(days)}')
    
epoch()