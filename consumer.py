from confluent_kafka import Consumer, KafkaException, KafkaError
import json
import psycopg2

# Kafka Consumer Configuration
consumer_config = {
    'bootstrap.servers': 'pkc-p11xm.us-east-1.aws.confluent.cloud:9092',
    'security.protocol': 'SASL_SSL',
    'sasl.mechanism': 'PLAIN',
    'sasl.username': 'KFWWR6X3DXE5KGYE',
    'sasl.password': 'oZ9Lfj55x8QBRJacpvryymQYTFnfauzg0x3cyjT4rlo/a1G5zBqvum5KR572NJa7',
    'group.id': 'lkc-1y5rp3', #cluster_id
    'auto.offset.reset': 'earliest'
}

# Initialize Kafka Consumer
consumer = Consumer(**consumer_config)

# Subscribe to the 'users' topic
topic = 'topic_0'
consumer.subscribe([topic])

# PostgreSQL Connection Details
db_config = {
    'dbname': 'defaultdb',
    'user': 'avnadmin',
    'password': 'AVNS_0moofrzCLOUx5s4CUi8',
    'host': 'pg-4c0d3de-mugendijames341-7875.f.aivencloud.com',
    'port': 19572
}

# Connect to PostgreSQL Database
try:
    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()
    print("Connected to PostgreSQL database.")
except Exception as e:
    print(f"Failed to connect to PostgreSQL: {e}")
    exit(1)

# Create the table if it doesn't exist
create_table = """
CREATE TABLE IF NOT EXISTS tbl_messages (
    id SERIAL PRIMARY KEY,
    Open VARCHAR(255),
    High VARCHAR(255),
    Low VARCHAR(255),
    Close VARCHAR(255),
    Volume VARCHAR(255)
);
"""
cursor.execute(create_table)
conn.commit()

# Function to insert data into PostgreSQL
def insert_data(data):
    """Inserts stock data into the PostgreSQL database."""
    insert_query = """
    INSERT INTO tbl_messages (Open, High, Low, Close, Volume)
    VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(insert_query, (data['1. open'], data['2. high'], data['3. low'], data['4. close'], data['5. volume']))
    conn.commit()
    print("Data inserted successfully")

# Consumer Loop
try:
    while True:
        # Poll Kafka for messages
        msg = consumer.poll(timeout=1.0)
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                # End of partition event
                print('%% %s [%d] reached end at offset %d\n' % (msg.topic(), msg.partition(), msg.offset()))
            elif msg.error():
                raise KafkaException(msg.error())
        else:
            # Process received message
            print('Received message: key=%s value=%s' % (msg.key().decode('utf-8') if msg.key() else None, msg.value().decode('utf-8') if msg.value() else None))
            data = json.loads(msg.value().decode('utf-8'))
            
            # Insert data into PostgreSQL
            insert_data(data)

except KeyboardInterrupt:
    print("Consumer interrupted by user")

finally:
    # Close Kafka consumer and PostgreSQL connection
    consumer.close()
    cursor.close()
    conn.close()
