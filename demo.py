"""
Author: Ali Hajimirza (ali@alihm.net)
Copyright Ali Hajimirza, free for use under MIT license.
"""
import csv
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
from algorithm import 


def line_plot(data_arrays, xlabel, ylabel, labels, title, f):
    """
    Plots a scatter chart.
    Parameters
    ----------
    data_arrays: 2d numpy array
        Data to be plotted. This array consists of matrices of real values to be plotted.
        Each row of this matrix will be plotted as a line on the graph.
    xlabel: list of string
        The list of categories on for the x axis labels. The length of this list should be equal to the
        columns of the data_arrays.
    ylabel: string
        The label on the y axis.
    labels: list of string
        The labels for each category.
    title: string
        The title of the graph. Will be used as the name of the graph file.
    dest: string, optional
        Path to the directory to save the image
    Returns
    -------
    None:
        Saves the plot to the disk.
    """
    plt.suptitle(title, fontsize=14)
    plots = []
    for data in data_arrays:
        plot, = plt.plot(data)
        plots.append(plot)
    plt.legend(plots, labels, loc=2)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig(f, format="png")
    plt.clf()


if __name__ == '__main__':
    # reading the file
    with open('hw7.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile)
        input_list = np.array(map(lambda line: np.array(map(lambda i: float(i), line)), reader))

    x_list = input_list[:,0]
    e_matrix = input_list[:,1:]
    mean_matrix = sumilate_E_M(x_list, e_matrix, 100)
    line_plot(mean_matrix, 'step', 'mean', ['Distribution 1','Distribution 2','Distribution 3'], 'E-M Learning' ,'part-c.png' )
