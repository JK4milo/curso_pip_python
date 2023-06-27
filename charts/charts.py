import matplotlib.pyplot as plt


def piechart():
    labels = ['A','B','C']
    values = [40,30,10]
    

    fig,ax = plt.subplots()
    ax.pie(values, labels = labels)
    plt.savefig('pie.png')
    plt.close()