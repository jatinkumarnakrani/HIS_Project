import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def change(data):
    if data=="<31":
        return 31
    else :
        return int(data)

montrealBikeLane = pd.read_csv("datasets/MontrealBikeLane.csv")
weatherInfo = pd.read_csv("datasets/WeatherInfo.csv")

montrealBikeLane.rename(columns = {'Date':'date_time'}, inplace = True)
weatherInfo.rename(columns = {'Date/Time':'date_time'}, inplace = True)

sns.heatmap(montrealBikeLane.isnull())

montrealBikeLane['date_time'] = pd.to_datetime(montrealBikeLane['date_time'], format='%d/%m/%Y').dt.strftime('%d-%m-%Y')
weatherInfo['date_time'] = pd.to_datetime(weatherInfo['date_time'], format='%Y/%m/%d').dt.strftime('%d-%m-%Y')

montrealBikeLane.fillna(0, inplace=True)
output1 = pd.merge(montrealBikeLane, weatherInfo, on='date_time', how='inner')


columns_to_remove = ['Max Temp Flag', 'Min Temp Flag', 'Mean Temp Flag', 'Heat Deg Days Flag','Cool Deg Days Flag','Total Rain Flag','Snow on Grnd Flag','Time', 'Data Quality', 'Dir of Max Gust Flag', 'Spd of Max Gust Flag', 'Year','Month', 'Day','Heat Deg Days (°C)', 'Cool Deg Days (°C)', 'Total Snow Flag','Total Precip Flag','Max Temp (°C)', 'Min Temp (°C)','Dir of Max Gust (10s deg)']

output1.drop(columns_to_remove, inplace=True, axis=1)



columns_to_fill = ['Total Rain (mm)', 'Total Snow (cm)','Total Precip (mm)', 'Snow on Grnd (cm)']
output1['Total Rain (mm)'].fillna(0, inplace=True)
output1['Total Snow (cm)'].fillna(0, inplace=True)
output1['Total Precip (mm)'].fillna(0, inplace=True)
output1['Snow on Grnd (cm)'].fillna(0, inplace=True)
output1['Spd of Max Gust (km/h)'].fillna(31, inplace=True)

output1["Spd of Max Gust (km/h)"]=output1["Spd of Max Gust (km/h)"].apply(change)

columns_with_blank = output1.columns[output1.isnull().any()].tolist()
print(columns_with_blank)
print(output1)
# x1 = np.array(montrealBikeLane['Berri1'])
# y1 = np.array(montrealBikeLane['Boyer'])
# x2 = np.array(montrealBikeLane['Brébeuf'])
# y2 = np.array(montrealBikeLane['CSC (Côte Sainte-Catherine)'])

# plt.plot(x1, y1, x2, y2)
# plt.show()
output1.to_csv('filled_dataset.csv', index=False)

