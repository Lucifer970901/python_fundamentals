import logging

logging.basicConfig(filename="logging_implementation/Megha.txt",
                    filemode='a', #append mode
                    format = '%(asctime)s %(levelname)s-%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

for i in range(0,15):
    if (i%2==0):
        logging.warning('Log warning message')
    elif (i%3==0):
        logging.critical("Log critical message")
    else:
        logging.error("Log error message")

i=10
try:
    i = i/0
except:
    logging.error("division by zero")