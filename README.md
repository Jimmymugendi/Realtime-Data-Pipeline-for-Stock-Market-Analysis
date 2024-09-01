# Real-time Data Pipeline for Stock Market Analysis
### Overview
This project demonstrates the development of a real-time data pipeline designed to ingest, process, and analyze stock market data. Using cutting-edge tools like Apache Kafka, PostgreSQL, and Python, the pipeline captures stock data in real-time and stores it in a robust data architecture, enabling timely analysis and insights.

### Project Highlights
* Data Ingestion: Real-time stock data is fetched using APIs from Alpha Vantage and ingested into the pipeline.
* Stream Processing: Apache Kafka, deployed on Confluent Cloud, acts as the streaming platform to handle data flow between producers and consumers.
* Data Storage: Aiven's integration with PostgreSQL allows for seamless data storage, enabling efficient query execution and data retrieval.
* Real-time Analysis: The pipeline is designed to process data on-the-fly, providing up-to-the-minute insights into stock performance.
### Technologies Used
* Python: Scripting for producer and consumer operations.
* Apache Kafka: Streaming platform for real-time data handling.
* APIs (Alpha Vantage): Data source for stock market data.
* Aiven: Managed service to connect Kafka with PostgreSQL.
* PostgreSQL: Database for storing and analyzing the ingested data.
### Architecture Overview
1. Producer Script: Written in Python, the producer script connects to the Alpha Vantage API to fetch live stock data and sends it to Kafka.
![Screenshot (851)](https://github.com/user-attachments/assets/a899c165-2f84-4809-9f50-7c04b6fa5a93)
3. Kafka Streams: Apache Kafka serves as the streaming backbone, receiving data from the producer and forwarding it to a PostgreSQL database.
![Screenshot (840)](https://github.com/user-attachments/assets/4d0fe560-8536-40e3-ac4e-bb3a7dca0bf5)

5. Consumer Script: Another Python script reads data from Kafka topics and loads it into PostgreSQL for analysis and visualization.
![Screenshot (850)](https://github.com/user-attachments/assets/39d358a4-c58c-4320-8d53-01571723c621)
7. Data Analysis: SQL queries and aggregations on the PostgreSQL database allow for insightful analysis of real-time stock data.
![Screenshot (845)](https://github.com/user-attachments/assets/fa0f1344-5577-4778-8d00-0c472e3ce2a2)
### Learning Outcomes
* Stream Processing with Kafka: Developed skills in handling real-time data using Apache Kafka, setting up topics, and managing data streams.
* ETL Workflow: Gained experience in ETL (Extract, Transform, Load) processes, integrating APIs, streaming platforms, and databases.
* Data Integration: Successfully connected various technologies to build a cohesive data pipeline, demonstrating the ability to work with cloud services and real-time data.
### Getting Started
#### Prerequisites
* Python 3.x
* Apache Kafka (via Confluent Cloud)
* PostgreSQL (via Aiven)
* API key for Alpha Vantage
### Installation
1. Clone the repository:

bash

`git clone https://github.com/yourusername/stock-market-pipeline.git`

2. Install the required Python packages:

bash

`pip install -r requirements.txt`

3. Set up Kafka topics and configure the PostgreSQL connection as per the instructions in the config.yaml file.

### Running the Project
1. Run the producer script to start streaming data to Kafka:

bash

`python producer.py`

2. Run the consumer script to store data in PostgreSQL:

bash

`python consumer.py`

### Future Work
Visualization: Integrate with Tableau or Power BI for dynamic data visualization.
Scalability: Expand the pipeline to handle multiple data sources and enhance fault tolerance.
### About Me
I am a data scientist passionate about building real-time data solutions that drive business insights. This project showcases my skills in data engineering, particularly in stream processing, ETL workflows, and integrating modern data technologies.
