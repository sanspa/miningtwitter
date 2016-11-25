import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import time
import csv
import sys

class MyTweetListener(StreamListener):
    
    #inisialisasi
    def __init__(self,api = None):
        #That sets the api
        self.api = api
        #membuat file "data" dan waktu sekarang
        self.filename = 'data'+'_'+time.strftime('%Y%m%d-%H%M%S')+'.csv'
        csvFile = open(self.filename,'w')
        
        #membuat csv writer
        csvwriter = csv.writer(csvFile)
        
        csvwriter.writerow(['created_at',
                            'user.id',
                            'user.name',
                            'user.description',                            
                            'user.location',
                            'text',
                            'retweet_count',
                            'scrap_time'])
    def on_status(self, status):
        
        #Open the csv file
        csvFile = open(self.filename,'a')
        
        #Create csv writer
        csvWriter = csv.writer(csvFile)
        
        #only original tweet, not retweet_count
        if not 'RT @' in status.text:
            try:
                #Write to csv
                csvWriter.writerow([status.created_at,
                                    status.user.id,
                                    status.user.name,
                                    status.user.description,
                                    status.user.location,
                                    status.text,
                                    status.retweet_count,
                                    time.strftime('%Y%m%d-%H%M%S')])
            except Exception as e:
                #Print the error
                print(e)
                pass
            
        #close the file
        csvFile.close()
        
        return
    
    #Error Handler
    def on_error(self, status_code):
        #Print the status_code
        print("Encounter Error with the status code: ", status_code)
        
        if status_code == 401:
            return False
        
    def on_delete(self, status_id, user_id):
        #print message
        print("Delete notice")
        
        return
    
    def on_limit(self, track):
        #print rate limiting error
        print("rate limited, continuing")
        
        return True
    
    def on_timeout(self):
        print(sys,stderr,"Timeout....")
        
        time.sleep(10)
        
        return
    
def start_mining():
        '''
        Inputs lists of strings. Return tweets containing those strings.
        '''
        
        #Credential
        consumer_key="Oz1OZPH0UghyelRf4cuZKTUPs"       
        consumer_secret="3LImwWGn5Fmm8AGZWBQceVJSEuYvuRHwiNkwZn2Gt3ss5hYLXu"
        access_token="2880055838-ycrARoTBwdjREC3qnMI204lHMc9veI7sClcFjgk"
        access_token_secret="J7fD1BpKA4h6NsgNM4vIrwkF9DztPoS63MEPy6GuYgrp5"
        
        myListener = MyTweetListener()
        
        #OAuth process, using the keys and tokens
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        
        #Create a Stream object with listener and authorization
        stream = Stream(auth,myListener)
        
        while True:
        try:
            stream.filter(track=sys.argv[2:])
        except:
            continue
        
if __name__= '__main__':
    start_mining()
    
    

        
        
