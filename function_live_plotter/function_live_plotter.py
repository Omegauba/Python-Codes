# -*- coding: utf-8 -*-
"""
Created on Fri Jan 4 10:57:47 2019

@author: OmegaUba

Small code to plot live graph of functions

"""
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

sns.set()

#define your function
def function(x):
    return (np.sin(x) + np.sin(3*x)/3 + np.sin(5*x)/5 + np.sin(7*x)/7)*np.cos(x/11)

x_axis = np.arange(0, 1000, 1)/1e2
y_axis = np.zeros((1000, ))

figure = plt.figure(1)
graph = figure.add_subplot(111)
graph.grid(True)
graph.set_title("Realtime Random Numbers")
graph.set_xlabel("Frequency")
graph.set_ylabel("Amplitude")

#define axis boundaries
graph.axis([0, 1000, -1.5, 1.5])

#plot just a straight line for reference
line = graph.plot(x_axis, y_axis, '-')

manager = plt.get_current_fig_manager()

values = y_axis

#the strategy is to use one array to store the values, the array gets bigger and bigger and only the last 1000 elements are plotted
def Random_Generator(arg):
  global values
  values = np.append(values, values.max() + 0.01)

# modify the x,y dataset and replot
def Live_Plotter(arg):
  global values
  x_axis_temp = values[-1000:]
  y_axis_temp = function(x_axis_temp)
  graph.axis([x_axis_temp.min(), x_axis_temp.max(), -1.5, 1.5])
  line[0].set_data(x_axis_temp, y_axis_temp)
  manager.canvas.draw()

#two timers, must be synchronized, each will call back the function, interval is in ms
timer_1 = figure.canvas.new_timer(interval = 1)
timer_1.add_callback(Live_Plotter, ())

timer_2 = figure.canvas.new_timer(interval = 1)
timer_2.add_callback(Random_Generator, ())

timer_1.start()
timer_2.start()

plt.show()

#to stop the plot
def Stop_Plot():
    timer_1.stop()
    timer_2.stop()
