import random
import pandas as pd
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go
import csv



df = pd.read_csv('School2.csv') 
data = df['Math_score'].tolist()

def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

mean_list = []
for i in range(0,1000):
    set_of_means = random_set_of_mean(100)
    mean_list.append(set_of_means)

st_deviation = statistics.stdev(mean_list)
mean = statistics.mean(mean_list)
print(mean, st_deviation)

first_deviation_start, first_deviation_end = mean - st_deviation, mean+st_deviation
second_deviation_start, second_deviation_end = mean -(2*st_deviation), mean+(2*st_deviation)
third_deviation_start, third_deviation_end = mean - (3*st_deviation), mean+(3*st_deviation)


df = pd.read_csv('School_1_Sample.csv')
data1 = df['Math_score'].tolist()

mean_of_Sample1 = statistics.mean(data1)
print(mean_of_Sample1)

fig = ff.create_distplot([mean_list],['Student Marks'],show_hist = False)
fig.add_trace(go.Scatter(x = [mean, mean],y = [0, 0.17],mode = 'lines', name = 'MEAN'))
fig.add_trace(go.Scatter(x = [mean_of_Sample1, mean_of_Sample1],y = [0, 0.17],mode = 'lines', name = 'MEAN OF STUDENTS WHO HAD MATH LABS'))
fig.add_trace(go.Scatter(x = [first_deviation_start, first_deviation_end],y = [0, 0.17],mode = 'lines', name = 'STANDARD DEVIATION 1'))
fig.add_trace(go.Scatter(x = [second_deviation_start, second_deviation_end],y = [0, 0.17],mode = 'lines', name = 'STANDARD DEVIATION 2'))
fig.add_trace(go.Scatter(x = [third_deviation_start, third_deviation_end],y = [0, 0.17],mode = 'lines', name = 'STANDARD DEVIATION 3'))
fig.show()

df = pd.read_csv('School_2_Sample.csv')
data1 = df['Math_score'].tolist()

mean_of_Sample1 = statistics.mean(data1)
print(mean_of_Sample1)

fig = ff.create_distplot([mean_list],['Student Marks'],show_hist = False)
fig.add_trace(go.Scatter(x = [mean, mean],y = [0, 0.17],mode = 'lines', name = 'MEAN'))
fig.add_trace(go.Scatter(x = [mean_of_Sample1, mean_of_Sample1],y = [0, 0.17],mode = 'lines', name = 'MEAN OF STUDENTS WHO USE MATH APPLICCATION'))
fig.add_trace(go.Scatter(x = [first_deviation_start, first_deviation_end],y = [0, 0.17],mode = 'lines', name = 'STANDARD DEVIATION 1'))
fig.add_trace(go.Scatter(x = [second_deviation_start, second_deviation_end],y = [0, 0.17],mode = 'lines', name = 'STANDARD DEVIATION 2'))
fig.add_trace(go.Scatter(x = [third_deviation_start, third_deviation_end],y = [0, 0.17],mode = 'lines', name = 'STANDARD DEVIATION 3'))
fig.show()


df = pd.read_csv('School_3_Sample.csv')
data1 = df['Math_score'].tolist()

mean_of_Sample1 = statistics.mean(data1)
print(mean_of_Sample1)

fig = ff.create_distplot([mean_list],['Student Marks'],show_hist = False)
fig.add_trace(go.Scatter(x = [mean, mean],y = [0, 0.17],mode = 'lines', name = 'MEAN'))
fig.add_trace(go.Scatter(x = [mean_of_Sample1, mean_of_Sample1],y = [0, 0.17],mode = 'lines', name = 'MEAN OF STUDENTS WHO PRACTICE MORE'))
fig.add_trace(go.Scatter(x = [first_deviation_start, first_deviation_end],y = [0, 0.17],mode = 'lines', name = 'STANDARD DEVIATION 1'))
fig.add_trace(go.Scatter(x = [second_deviation_start, second_deviation_end],y = [0, 0.17],mode = 'lines', name = 'STANDARD DEVIATION 2'))
fig.add_trace(go.Scatter(x = [third_deviation_start, third_deviation_end],y = [0, 0.17],mode = 'lines', name = 'STANDARD DEVIATION 3'))
fig.show()


z_score = (mean-mean_of_Sample1)/st_deviation
print(z_score)