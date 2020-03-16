import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    weather_data_path = "weather.csv"
    weather_year = 2020
    # read CSV file
    with open(weather_data_path,"r") as fin:

        df = pd.read_csv(fin,skiprows=18)

        weather_variables = [v for v in list(df.columns) if v not in ['Date', 'HH:MM', 'Datasource']]

        tdf = df['HH:MM'].str.split(':',expand=True)
        df['Hour']=(pd.to_numeric(tdf[0])-1)
        df['Minute']=pd.to_numeric(tdf[1])
        ddf = df['Date'].str.split('/',expand=True)
        df['Year'] = pd.to_numeric(ddf[0])
        df['Month'] = pd.to_numeric(ddf[1])
        df['Day'] = pd.to_numeric(ddf[2])

        # stitch data together
        df['Datetime'] = pd.to_datetime(str(weather_year) + '/' + df['Month'].astype(str) + '/' + df['Day'].astype(str) + ' ' + df['Hour'].astype(str) + ':' + df['Minute'].astype(str), format="%Y/%m/%d %H:%M")#.replace(year=2020).dt.strftime('%Y-%m-%dT%H:%M:00-05:00 Chicago')
        df = df.set_index('Datetime')
        
        plot_variable = 'Dry Bulb Temperature {C}'
        plt.plot(df[plot_variable])
        plt.title(plot_variable)
        plt.xlabel('Datetime')
        plt.ylabel(plot_variable)
        plt.show()