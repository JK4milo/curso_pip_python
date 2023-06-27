import csv

def read_csv(path):
  with open(path, 'r') as csvfile:
    reader =csv.reader(csvfile,delimiter=',')
    #esto muestra la primera linea que es el titulo de la columna, lo cual nos interesa por que necesitamos crear un diccionario.
    header = next(reader)
    data = []
    for row in reader:
      iterable = zip(header, row)
      country_dict = {key:value for key, value in iterable}
      data.append(country_dict)
    return data
    
      
    
    





if __name__ =='__main__':
  data = read_csv('/home/runner/python1021/app/data.csv')  
  print(data)
  
  
    