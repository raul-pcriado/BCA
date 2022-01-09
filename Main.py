# import libraries
import pandas
import numpy
import matplotlib

# import data
path = 'E:\Descargas\Work\Altran\welcome_pack_2021_v2\crimes_dataset.csv'
data = pandas.read_csv(path, sep=";")
data

sorted(data['YEAR'].unique())
sorted(data['MONTH'].unique())
sorted(data['DAY_OF_WEEK'].unique())
sorted(data['HOUR'].unique())
sorted(data['Location'].unique())

data['Location' != ]
