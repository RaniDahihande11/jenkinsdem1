import pandas as pd

print('extract data from MySQL to database')


data = {
    'id': [1,2,3],
    'name':['Ram','Raju','Rahul'],
    'age':[10,20,30]


}

df = pd.DataFrame(data)
print(df)