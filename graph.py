import matplotlib.pyplot as plt

def plot_graph(dates, values):
    plt.plot(dates,values)
    plt.title('Graph')
    plt.xlabel('Dates')
    plt.ylabel('Values')
    plt.show()