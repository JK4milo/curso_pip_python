import utils
import read
import chart
def run():
  data = read.read_csv('D:/Users/user/Desktop/proyecto-pip-python/app/data.csv')
  country = input("Digite el pais: ").title()
  result = utils.population_by_country(data, country)
  
  
  if len(result)>0:
    country= result[0]
    labels, values = utils.get_population(country)
    chart.generate_bar_chart(country['Country/Territory'],labels,values)
  
  
  print(result)

if __name__ == '__main__':
  run()