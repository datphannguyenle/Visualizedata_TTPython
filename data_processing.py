import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Ho Chi Minh.csv')
time = []
month = ''
for c in df['datetime']:
    if str(c)[5:7] != month:
        time.append(str(c)[-5:])
        month = str(c)[5:7]
    else:
        time.append(str(c)[-2:])

print(time)
plt.plot(time, df['temp'], 'r', label='Temp')
plt.plot(time, df['humidity'], 'b', label='Humidity')
plt.plot(time, df['windspeed'], 'g', label='Wind speed')
plt.plot(time, df['uvindex'], 'y', label='UV index')
plt.title("Weather index in Ho Chi Minh city for 14 days")
plt.legend(loc='best')
plt.xlabel("Time")
plt.ylabel("Index")
plt.show()
#https://www.youtube.com/watch?v=doQ77RCgpxA&t=156s