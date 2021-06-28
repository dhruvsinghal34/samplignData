import csv 
import statistics as s 
import pandas as pd
import random 
import plotly.figure_factory as ff 
import plotly.graph_objects as go

df = pd.read_csv("medium_data.csv")
data = df["id"].tolist()
figure = ff.create_distplot([data],["id"],show_hist = False)
figure.show()

def random_set_of_mean(counter):
    dataTemp = []
    for i in range(0,counter):
        temp_index = random.randint(0,len(data)-1)
        value = data[temp_index]
        dataTemp.append(value)
    
    mean = s.mean( dataTemp)
    return mean

def show_fig(mean_list):
    df = mean_list
    mean = s.mean(df)
    fig = ff.create_distplot([df],["id"],show_hist = False)
    fig.show()

def setup():
    mean_list = []
    for i in range(0,1000):
        set_of_mean = random_set_of_mean(100)
        mean_list.append(set_of_mean)
    
    show_fig(mean_list)
    mean = s.mean(mean_list)
    print("mean of sampling distrubution of Temperature is = " , mean)

setup()

# code to find mean of raw data(temperature data)

temperature_mean = s.mean(data)
print(" the temperature mean is = " , temperature_mean)


def standard_deviation ():
    mean_list = []
    for i in range (0,1000):
        set_of_mean = random_set_of_mean(100)
        mean_list.append(set_of_mean)
    
    standard_deviation = s.stdev(mean_list)
    print("the standard deviation of sampling distrubution is =" , standard_deviation)

standard_deviation()

              