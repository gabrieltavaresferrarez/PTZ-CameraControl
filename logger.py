import time
import codecs
from datetime import datetime

 

listString_topicBullets= ['* ', '- ', '+ ', '¢ ', '* ', '- ', '+ ', '¢ ']

 

class Logger:

    def __init__(self, log_file_name : str = 'log.log'):
        self.string_logFileName = log_file_name
        with codecs.open(self.string_logFileName, "w", encoding='utf-8') as file_log:
            string_timestamp = self.get_timestamp()
            file_log.write(string_timestamp)
            file_log.write('########################### START LOG ###########################')
            file_log.write('\n')
       

    def topic(self, text, sub_level = 0, break_line = True):
        #escreve topico com time stamp
        #subtopicos tem identação
        with codecs.open(self.string_logFileName, "a", encoding='utf-8') as file_log:
            string_timestamp = self.get_timestamp()
            file_log.write(string_timestamp)

            file_log.write('\t\t'*sub_level)
            string_topicBullet = listString_topicBullets[sub_level]
            file_log.write(string_topicBullet)
 
            file_log.write(text)

            if break_line:
                file_log.write('\n')

           

    def write(self, text : str, breakline : bool = False, timestamp : bool = False): # apenas apenda a linha atual do log sem timestamp
        with codecs.open(self.string_logFileName, "a") as file_log:
            if timestamp:
                string_timestamp = self.get_timestamp()
                file_log.write(string_timestamp)

            file_log.write(text)

            if breakline:
                file_log.write('\n')

 
    def erro(self, text, sub_level = 0, breakline : bool = True, timestamp : bool = True):
        with codecs.open(self.string_logFileName, "a") as file_log:
            if timestamp:
                string_timestamp = self.get_timestamp()
                file_log.write(string_timestamp)

            # level
            file_log.write('\t\t'*sub_level)
            string_topicBullet = listString_topicBullets[sub_level]
            file_log.write(string_topicBullet)

            file_log.write('[ERRO] : ')
            file_log.write(text)
         
            if breakline:
                file_log.write('\n')
 
    def breakline(self):
        with codecs.open(self.string_logFileName, "a") as file_log:
            file_log.write('\n')
 

    def get_timestamp(self):
        date_now = datetime.now()
        string_timestamp = f'{date_now.year:02d}/{date_now.month:02d}/{date_now.day:02d}-{date_now.hour:02d}:{date_now.minute:02d}:{date_now.second:02d} | '
        return string_timestamp