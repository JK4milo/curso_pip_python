import matplotlib.pyplot as plt


#generate bar chart

def generate_bar_chart(name,labels,values):
  fig,ax = plt.subplots()
  ax.bar(labels,values)
  plt.savefig(f'./imgs/{name}.png')
  plt.close()


#generate pie chart
def generate_pie_chart(name,labels,values):
  fig,ax = plt.subplots()
  ax.pie(values, labels= labels)
  ax.axis('equal')
  plt.savefig(f'./imgs/{name}.png')


if __name__ =='__main__':
  labels = ['a','b','c']
  values = [100,2000,400]
  name =[]
  generate_bar_chart(labels,values)
  generate_pie_chart(name,labels,values)
  