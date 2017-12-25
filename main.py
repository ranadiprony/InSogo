import json
import requests
import os
from os import path

appid = None
appkey = None

def getConfig():

    try:
        configfile = path.join(os.getcwd(), "config.json")
        conf = json.load(open(configfile))
        global appid
        global appkey
        appid = conf["config"]["appid"]
        appkey = conf["config"]["appkey"]
    except Exception as ex:
        print(ex.message)
        print("Kindly use the configtemplate.json with appropriate values and rename as config.json")
        exit()


def init():
    print("Welcome")
    response = requests.get(
        'http://techpaisa.com/api/chart/VOLTAS/fibonacci-retracement/?app_id={}&app_key={}'.format(appid,appkey))
    if response.status_code == 200:
        print(response.json()['text_analysis'])
    else:
        print("Connection Failure")

getConfig()
init()

