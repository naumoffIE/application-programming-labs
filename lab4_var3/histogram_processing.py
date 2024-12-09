import matplotlib.pyplot as plt
import pandas as pd


def plot_column_distribution(column: pd.Series, x_label_title: str) -> None:
    """
    Plot a histogram for a specified DataFrame column.

    :param: column: Series object containing the data to plot.
    :param: x_label_title: Label for the x-axis of the histogram.
    """
    plt.figure(figsize=(9, 6))
    plt.hist(column, bins=30, color='salmon', edgecolor='black')
    plt.title('Distribution of Image Areas')
    plt.xlabel(x_label_title)
    plt.ylabel('Number of Images')
    plt.show()
