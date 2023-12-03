# Use Kafka to sent data

## Objective
วัตถุประสงค์ของโปรเจ็คนี้คือการส่งข้อมูลจากที่หนึ่งไปยังอีกที่หนึ่งด้วย Kafka

โดยได้จัดทำทั้งหมด 2 รูปแบบ นั่นคือ
1. Send data row by row with a 1-second delay from the “customers” table in the “classicmodels” database using Python (producer) to Python (consumer) through five kafka brokers (partition = 3, replication-factor = 5) (Use the “customerNumber” as the key, the other features as the value.)
2. Transfer data from MySQL (source) to Hadoop (sink)
