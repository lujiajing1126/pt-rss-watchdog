import requests
from requests.exceptions import ConnectionError,Timeout
import xmltodict
import email.utils
import redis
import logging
from bs4 import BeautifulSoup
import sys

def scarpy(debug=False):
	logger = logging.getLogger("ptfd_rss_service")
	try:
		r = requests.get('https://hdts.ru/rss.php')
		xml_data = xmltodict.parse(r.text)
	except ConnectionError:
		logger.warning("ConnectionError Occur.")
		sys.exit(1)
	except Timeout:
		logger.warning("Connect or Read Timeout.")
		sys.exit(1)

	last_build_time = email.utils.parsedate_tz(xml_data['rss']['channel']['lastBuildDate'])
	last_build_tim_stamp = email.utils.mktime_tz(last_build_time)
	redis_client = redis.StrictRedis(host="localhost",port=6379,db=0)
	old_last_build_time_stamp = redis_client.get('LastBuildTime')

	if(old_last_build_time_stamp == None ) or (last_build_tim_stamp > old_last_build_time_stamp) or debug:
	    redis_client.set("LastBuildTime",last_build_tim_stamp)
	    soup = BeautifulSoup(r.text,'xml')
	    items = soup.findAll('item')
	    for item in items:
			title = item.title.string
			description = item.description.string
			link = item.link.string
			guid = item.guid.string
			enclosure = item.enclosure['url']
			pub_date = email.utils.mktime_tz(email.utils.parsedate_tz(item.pubDate.string))
			payload = {'title':title,'description':description,'link':link,'guid':guid,'enclosure':enclosure,'pub_date':pub_date}
			req = requests.post('http://localhost:3000/api/v1/torrents/',data = payload)
			logger.info(req.text)
	    logger.info("Request for Api")
	else:
	    logger.info("Already newest")