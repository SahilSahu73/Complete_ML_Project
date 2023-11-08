# Logging
'''
Logger can help to develop a better understanding of the flow of a program and 
discover scenarios that we might not have even thought of while developing.
It constantly looks at the flow that the application is going through.
They can store information, like which user or IP accessed the application. 
If an error occurs, then they can provide more insights than a stack trace 
by telling you what the state of the program was before it arrived at the line
of code where the error occurred.
'''

# By using logger we can log messages that we want to see.
'''
There are 5 standard levels indicating the severity of events.
Each has a corresponding method that can be used to log events at that level of severity.
The defined levels, in increasing order of severity are:
1. DEBUG
2. INFO
3. WARNING
4. ERROR
5. CRITICAL

NOTE : by default, the logging module logs the messages with a severity level
       of WARNING or above.


basicConfig(**kwargs) method :
Commonly used parameters are :
1. level - to set the specified severity level
eg: logging.basicConfig(level=logging.DEBUG)

2. filename - to get teh logging details in a file instead of the console
eg : logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

3. filemode - if filename given, then open the file in the specified mode. Default is a i.e. append
4. format - this is the format of the log message.

'''

import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(),"logs_",LOG_FILE)
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# if __name__ == "__main__":
#     logging.info("Logging has started.")