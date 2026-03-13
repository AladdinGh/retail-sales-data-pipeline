Checkpoint Question 1
What is the main difference between ETL and ELT in this mini-project?
==> ELT we extracted data from different sources, then we loaded it in the Postgre Database and then in the data base itself we transformeded it (apply filter, changes, null handling ...) . 
In ETL we did the transformation on the data frames level not on the databese level, which means in the first case we used SQl to clean, in the latter we used python.


Checkpoint Question 2
Why does the ETL version transform data in Python before loading it into PostgreSQL?
==> Because we need to deliver clean data to the database tables "silver data"

Checkpoint Question 3
Why does the ELT version load raw data into PostgreSQL first before transforming it?
==> In this case we do not want to transform the data before loading it. this can be a good use case where we have no time/or computational power to preprocess data before loading, so we just load it and leave the heavy lifting for SQL.

Checkpoint Question 4
What are the three raw source files in this project, and what does each one represent in the business scenario?
==> JSON : represents the "lightest" format of data which is encapsulated in key:value pairs, easy, readable and light. json files can be responses from webpages for example. XML : exchange format , can be also be response from webpages 
CSV : comma seperated values, very used in data science and very well accepted in the python dev environment  

Checkpoint Question 5
Why is this project useful as a portfolio project for future job interviews?
==> hives hands on experience on ETL vs ELT concepts.