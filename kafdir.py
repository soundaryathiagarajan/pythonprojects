import sys
from kafka import SimpleProducer, SimpleClient
import os
import logging
import simplejson
logging.basicConfig(level=logging.INFO)
log = logging.getLogger("LogManager")

client = SimpleClient('localhost:9092')
producer = SimpleProducer(client, async=False)   

def process_file(f): 
	with open(f, 'r') as f:   
		for line in f:	
			if "Trace log : {\"request\":{\"http\"" in line: 
				out = 'Trace log' + line.split('Trace log')[-1]
				producer.send_messages('tes't, out)
            			# print line   


# def some_function(file):	
#     print(file)	
    # inputDir = sys.argv[1]
    # if not os.path.exists(sys.argv[1]):
    #     log.info("Input file does not exists")
    #     sys.exit(0)
    #f = open('/home/soundaryat/Downloads/datafile.txt','r')
    
#     #--- your original script, transformed into a some_function

# client = SimpleClient('localhost:9092')
# producer = SimpleProducer(client, async=False)   

if __name__ == "__main__":
	f = sys.argv[1]	
	s = os.listdir(f)
	# process_file(f)
	for each in s:
		f1 = f + each
		# print f1
		process_file(f1)


# dr = sys.argv[1]

# lda = os.listdir(dr)

# for f in lda: 
#  	producer.send_messages('testab',f)
# 	some_function(dr+"/"+f)
	        # producer.send_messages('testa',line)

    # with open(sys.argv[1], 'r') as f:   
    #     for line in f:   
    #         producer.send_messages('test', line)

    # #REFERENCE
# #--- your original script, transformed into a function
# def some_function(file):
#     print(file)
# #---

# # The directory with your .csv files
# dr = sys.argv[1]

# for f in os.listdir(dr):
#     file = dr+"/"+f
#     some_function(file)