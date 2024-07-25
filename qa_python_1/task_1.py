time = '1h 45m,360s,25m,30m 120s,2h 60s'
time_list = time.split(',')

total_minutes = 0

for m in time_list:
    minutes = 0
    
    if 'h' in m:
        hours = int(m.split('h')[0])
        minutes += hours * 60
        m = m.replace(f'{hours}h', '')
    
    if 'm' in m:
        mins = int(m.split('m')[0])
        minutes += mins
        m = m.replace(f'{mins}m', '')
    
    if 's' in m:
        seconds = int(m.split('s')[0])
        minutes += seconds // 60
    
    total_minutes += minutes

print(total_minutes)
