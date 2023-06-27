import chart
import utils
import read

def run():
  data =read.read_csv('/home/runner/python1021/app/data.csv')
  data = list(filter(lambda item:item['Continent']=='South America',data))
  countries = list(map(lambda x:x['Country/Territory'],data))
  porcentage = list(map(lambda x:x['World Population Percentage'],data))

  chart.generate_pie_chart(countries,porcentage)

if __name__=='__main__':
  run()
