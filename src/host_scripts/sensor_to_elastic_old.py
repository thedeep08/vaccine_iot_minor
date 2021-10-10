import sys
import Adafruit_DHT #DHT library
import pandas as pd    # dataframe library
from elasticsearch import Elasticsearch   # python client for elasticsearch
from elasticsearch import helpers
import datetime 
import time

def get_sensor_data(list_of_data, start_time, end_time, time_interval):
    for time_now in range(int(start_time), int(end_time), time_interval):
	    humidity, temperature = Adafruit_DHT.read_retry(11, 4)
            print(humidity)
            dict_temp = {'temp': temperature, 'humid': humidity, 'time': time_now }
	    #dict_temp['temp'] = temperature
	    #dict_temp['humid'] = humidity
	    #dict_temp['time'] = time_now
            list_of_data.append(dict_temp)
	    time.sleep(5)
            print(list_of_data)
    df = pd.DataFrame(list_of_data)
    return df
    #df.set_index('time', inplace=True)
        #for proc in psutil.process_iter():
        #    # Get process detail as dictionary
        #    process_dict = proc.as_dict(attrs=['pid', 'name', 'cpu_percent', 'memory_percent'])
        #    # p_time = proc.create_time()
        #    # p_time_h = datetime.datetime.fromtimestamp(p_time).strftime("%Y-%m-%d %H:%M:%S")
        #    process_dict['time'] = time_now
        ## Append dict of process detail in list
        #    listOfProcessNames.append(process_dict)

#
#while True:
#
#    humidity, temperature = Adafruit_DHT.read_retry(11, 4)
#
#    print 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity)



use_these_keys = ['temp', 'humid', 'time']
#
## filtering of pandas data frame
def filterKeys(document):
    return {key: document[key] for key in use_these_keys }


# to send data to elastic client by creating elastic document
def doc_generator(df):
    df_iter = df.iterrows()
    for index, document in df_iter:
        yield { "_index": 'pitemp',
                "_id" : index,
                "_source": filterKeys(document),
            }

if __name__ == "__main__":
    es_client = Elasticsearch(['http://192.168.1.104:9200'],http_compress=True)
    list_of_data = list()
    start_time = 0
    end_time  = 60
    time_interval = 5


    # listOfProcessNames = get_process_pid(list_of_Process, start_time, end_time, time_interval)
    # print(listOfProcessNames)

    # creating pandas dataframe
    dataFrame = get_sensor_data(list_of_data, start_time, end_time, time_interval)
    #dataFrame = dataFrame.rename_axis('pid').reset_index()

    dataFrame_iter = dataFrame.iterrows()
    index, document = next(dataFrame_iter)

    # loading data to es using es.bulk api
    helpers.bulk(es_client, doc_generator(dataFrame))



