# Problem 10

# Download data from the following url and print out the value
# for the key "message".

# https://gist.githubusercontent.com/tabinks/027f56704b1556e51470599cc53536f7/raw/fc10e5ee8d3effe74c67104480e8577a8d2caf95/secret_message.json
#
# You can choose to write a program in Python or use command line
# tools.  Include the code or command used and the message.

Answer : Congratulations on finishing your first computer science course!

import sys
import requests
import json

reload(sys)
sys.setdefaultencoding('utf8')

url = 'https://gist.githubusercontent.com/tabinks/027f56704b1556e51470599cc53536f7/raw/fc10e5ee8d3effe74c67104480e8577a8d2caf95/secret_message.json'
r = requests.get(url)
json_data = r.json()
print json_data["message"]

