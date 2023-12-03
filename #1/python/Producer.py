#install 
#pip install confluent_kafka

# Producer
import pandas as pd
import csv
import mysql.connector
from getpass import getpass 
from confluent_kafka import Producer
import time
p = Producer({'bootstrap.servers':'localhost:8096'})

def acked(err, msg):
    if err is not None:
        print("Failed to deliver message: %s: %s" % (str(msg), str(err)))
    else:
        print("Message produced: %s" % (msg.value().decode()))

#p.produce('randomTopic', key="key", value="value", callback=acked)

# Wait up to 1 second for events. Callbacks will be invoked during
# this method call if the message is acknowledged.
#p.poll(1)

#p.produce('randomTopic', key="name", value="Thiti", callback=acked)
#p.poll(1)

user = input('Username: ')
pwd = getpass('Password: ')

my_db = mysql.connector.connect( host='localhost',
                                                       user=user,
                                                       password=pwd,
                                                       database='classicmodels' )
print('Successfully connected to the database.')
sql_command = f'''select * from customers;'''
df = pd.read_sql(sql_command, my_db)
new_df = df[['customerNumber']].copy()
new_df['value'] = df[['customerName', 'contactFirstName', 'contactLastName', 'phone', 'addressLine1', 'addressLine2', 'city', 'state', 'postalCode', 'country', 'salesRepEmployeeNumber', 'creditLimit']].values.tolist()

for i in range(new_df.shape[0]):
    p.produce('randomTopic2', key=new_df.loc[i,'customerNumber'], value=str(new_df.loc[i,'value']), callback=acked)
    time.sleep(1)
    print()