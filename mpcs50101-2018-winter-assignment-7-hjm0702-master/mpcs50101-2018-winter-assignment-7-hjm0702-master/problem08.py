# -*- coding: utf-8 -*-

import sys
import requests
import json
from datetime import datetime

reload(sys)
sys.setdefaultencoding('utf8')


def date(n):
    month = {"01": "January", "02": "January", "03": "January", "04": "January", "05": "January",
    "06": "January", "07": "January", "08": "January", "09": "January", "10": "January",
    "11": "January", "12": "January", }
    result = datetime.strptime(n, "%Y-%m-%dT%H:%M:%SZ")
    return month[result.strftime('%m')] + result.strftime('%d, %Y %H:%M')

def news():
    Again = True

    while Again:
        Again2 = True
        while Again2:
            prompt1 = raw_input('''Welcome to Command Line News! Please make a choice:
[1] Top headlines
[2] Search
>> ''')

            '''When Headlines selected'''
            if prompt1 == "1":
                Again3 = True
                while Again3:
                    prompt1_1 = raw_input('''Select which category would you like to headlines for:
[1] business
[2] entertainment
[3] general
[4] health
[5] science
[6] sports
[7] technology
>> ''')

                    if prompt1_1 in ["1", "2", "3", "4", "5", "6", "7"]:
                        dic = {"1": 'business', "2": 'entertainment', "3": 'general', "4": 'health',
                        "5": 'science', "6": 'sports', "7": 'technology'}

                        url = "https://newsapi.org/v2/top-headlines?q=" + dic[prompt1_1] + "&apiKey=81c0632777214ed4877214bea72f818e"
                        r = requests.get(url)
                        json_data = r.json()

                        status = json_data["status"]
                        total_results = json_data["totalResults"]
                        article = json_data["articles"]

                        try :
                            if int(total_results) <= 20:
                                for i in range(total_results):
                                    news = article[i]
                                    print "*", news["title"]
                                    print "  -", date(news['publishedAt'])
                                    print "  -", news['description']
                                    print ""
                            else:
                                for i in range(20):
                                    news = article[i]
                                    print "*", news["title"]
                                    print "  -", date(news['publishedAt'])
                                    print "  -", news['description']
                                    print ""
                        except:
                            print "There is some character unable to read."
                        Again3 = False

                    else:
                        print "Please input an interger from 1 to 7."
                Again2 = False


            elif prompt1 == "2":
                prompt2 = raw_input('''Enter your search term:
>>''' )

                url = "https://newsapi.org/v2/everything?q=" + prompt2 + "&apiKey=81c0632777214ed4877214bea72f818e"
                r = requests.get(url)
                json_data = r.json()

                status = json_data["status"]
                total_results = json_data["totalResults"]
                article = json_data["articles"]

                try :
                    if int(total_results) <= 20:
                        for i in range(total_results):
                            news = article[i]
                            print "*", news["title"]
                            print "  -", date(news['publishedAt'])
                            print "  -", news['description']
                            print ""
                    else:
                        for i in range(20):
                            news = article[i]
                            print "*", news["title"]
                            print "  -", date(news['publishedAt'])
                            print "  -", news['description']
                            print ""
                except:
                    print "There is some character unable to read."
                Again2 = False
            else:
                print "Please input 1 or 2."

        Again4 = True
        while Again4:
            prompt3 = raw_input('''Would you like to find more news articles?
[1] Yes
[2] No
>> ''')
            Again4 = False
            if prompt3 in ["2", "No", "no"] :
                Again = False
            elif prompt3 in ["1", "Yes", "yes"]:
                Again = True
            else:
                print "Please input 1 or 2!"
                Again4 = True


news()
