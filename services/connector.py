import requests
import xmltodict
import email.utils
import redis
from bs4 import BeautifulSoup

r = requests.get('https://hdts.ru/rss.php')
xml_data = xmltodict.parse(r.text)
last_build_time = email.utils.parsedate_tz(xml_data['rss']['channel']['lastBuildDate'])
last_build_tim_stamp = email.utils.mktime_tz(last_build_time)
redis_client = redis.StrictRedis(host="localhost",port=6379,db=0)
old_last_build_time_stamp = redis_client.get('LastBuildTime')

soup = BeautifulSoup(r.text,'xml')
items = soup.findAll('item')
for item in items:
    print item.title.string
    print item.description.string
if(old_last_build_time_stamp == None ) or (last_build_tim_stamp > old_last_build_time_stamp):
    redis_client.set("LastBuildTime",last_build_tim_stamp)
    print "Update DB"
else:
    print "Already newest"
