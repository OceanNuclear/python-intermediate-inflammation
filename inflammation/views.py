"""Module containing code for plotting inflammation data."""

from matplotlib import pyplot as plt
import numpy as np


def visualize(data_dict, title=None):
    """Display plots of basic statistical properties of the inflammation data.

    :param data_dict: Dictionary of name -> data to plot
    """
    # TODO(lesson-design) Extend to allow saving figure to file

    num_plots = len(data_dict)
    fig = plt.figure(figsize=(3.0, 3.0))
    axes = fig.add_subplot()

    for name, data in data_dict.items():
        axes.plot(data, label=name)
    axes.legend()
    if title:
        plt.title(title)
    fig.tight_layout()

    plt.show()
