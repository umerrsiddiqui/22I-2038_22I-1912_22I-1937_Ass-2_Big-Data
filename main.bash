

#Function to start Zookeeper
  start_zookeeper ()
{
  
echo "Starting Zookeeper..." 
\

#Replace <zookeeper-path> with the actual path to your Zookeeper installation
	<zookeeper - path > /bin / zookeeper - server - start.sh <
	zookeeper - path > /config / zookeeper.properties > /dev / null 2 >
	&1 & 
sleep 5


echo "Zookeeper started." 
}


 
#Function to start Kafka Server
  start_kafka_server ()
{
  
echo "Starting Kafka Server..." 
#Command to start Kafka Server


	<kafka - path > /bin / kafka - server - start.sh < kafka - path >
	/config / server.properties > /dev / null 2 > &1 & 
sleep 10
#Wait for Kafka Server to start
echo "Kafka Server started." 
}


 
#Function to start Kafka Producer
  start_producer ()
{
  
echo "Starting Kafka Producer..." 
#Command to start Kafka Producer


	python < producer - path > /producer.py > /dev / null 2 > &1 & 
sleep 5

#Wait for Kafka Producer to start
echo "Kafka Producer started." 
}


 
#Function to start Kafka Consumers
  start_consumers ()
{
  
echo "Starting Kafka Consumers..." 
#Command to start Kafka Consumers

	python < consumer - path > /consumer1.py > /dev / null 2 > &1 & 
python <
	consumer - path > /consumer2.py > /dev / null 2 > &1 & 
python <
	consumer - path > /consumer3.py > /dev / null 2 > &1 & 
sleep 5
#Wait for Kafka Consumers to start
echo "Kafka Consumers started." 
}


 
#Function to stop Kafka Server and Zookeeper
  stop_kafka ()
{
  
echo "Stopping Kafka Server..." 
#Command to stop Kafka Server

	<kafka - path > /bin / kafka - server - stop.sh > /dev / null 2 > &1 
	echo "Kafka Server stopped." 
 
echo "Stopping Zookeeper..." 
#Command to stop Zookeeper

<zookeeper - path > /bin / zookeeper - server - stop.sh > /dev / null 2 >
	&1 
 echo "Zookeeper stopped." 
}

 
#Main function
  main ()
{
  
#Start Zookeeper
	start_zookeeper 
 
#Start Kafka Server
	start_kafka_server 
 
#Start Kafka Producer
	start_producer 
 
#Start Kafka Consumers
start_consumers 
}


 
#Call the main function
  main 
