from bs4 import BeautifulSoup
from bs4 import CData

markup = "<title><![CDATA[Pulp 2014 720p BluRay DTS x264-TRiPS]]></title>"
soup = BeautifulSoup(markup,'xml')
print soup.find('title').get_text()
