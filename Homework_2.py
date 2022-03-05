sek = int (input('Enter the time in seconds: '))
hour = sek // 3600
n = sek - hour * 3600
minute = n // 60
sek_1 = n - minute * 60
print('Time in hour, min, sec:', hour, minute, sek_1)
