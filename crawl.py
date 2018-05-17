
import requests,logging,re
from bs4 import BeautifulSoup as bs
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')

url = 'http://wugengji.feiwan.net/manhua/'
def Get_contents(url,header=None,proxy=None):
    res=requests.get(url,header,proxies=proxy)
    #if res.raise_for_status!=200:
    #    logging.debug(res.raise_for_status())
    soup=bs(res.text,'lxml')
    type=re.search('text/html; charset=(\w+)',soup.find('meta').get('content')).group(1)
    res.encoding=type
    bsobj=bs(res.text,'lxml')
    o=open('content.txt','w')
    for i in bsobj.select('#show_div_1 > ul > li > a'):
        logging.info(i.get('title'))
        o.write('%s\t%s\n'%(i.get('title'),i.get('href')))
url='http://wugengji.feiwan.net/201703/124235.html'

def Get_Img(url,output):
    res=requests.get(url)
    soup=bs(res.text,'lxml')
    type=re.search('text/html; charset=(\w+)',soup.find('meta').get('content')).group(1)
    res.encoding=type
    bsobj=bs(res.text,'lxml')
    a=bsobj.find_all(lambda x: x.name=='script' and not x.has_attr('src') and not x.has_attr('language'))[-1]
    f= open(output+'/download.txt','w')
    for page,jpg in re.findall("narImg\[(\d+)\] = \'(\S+)\'",a.string):
        filename=jpg.split('/')[-1]
        f.write('%s\t%s\t%s\n'%(page,jpg,filename))
proxy={"http":'116.237.151.156:9000'}
header={
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host':'wugengji.feiwan.net',
    'User-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_5_8) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.801.0 Safari/535.1'
}

def Download(url,output):
    res=requests.get(url,timeout=2)
    if res.raise_for_status() !=404:
        with open(output,'wb')as f:
            f.write(res.content)


