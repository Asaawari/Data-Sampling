import csv
import plotly.figure_factory as ff
import statistics
import random
import pandas as pd

data = pd.read_csv("medium_data.csv")
final_data = data["reading_time"].tolist()

fig = ff.create_distplot([data],["reading_time"], show_hist=False)
fig.show()

print("Population Mean = ",statistics.mean(final_data))

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(final_data))
        value = final_data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    final_data = mean_list
    fig = ff.create_distplot([final_data],["reading_time"], show_hist=False)
    fig.show()

def setup():
    mean_list = []
    for i in range(0,100):
        set_of_means= random_set_of_mean(10)
        mean_list.append(set_of_means)
    show_fig(mean_list)
    print("Sampling Mean:- ", statistics.mean(mean_list))

setup()