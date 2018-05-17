from crawl import *
import os,time
starturl='http://wugengji.feiwan.net/manhua/'

header={
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'first_h=1521771041940; count_h=1; first_m=1521771041942; count_m=1; __music_index__=1; Hm_lvt_7c51fff13c243b5d978c5336d034017b=1521769952; UM_distinctid=162508eb4343c2-01c7be9b6ee1d-336c7b05-13c680-162508eb435a8; CNZZDATA1272893301=1067576345-1521767256-%7C1521767256; __cfduid=d764725da9c413774cc691da97a62cc631521769955; Hm_lpvt_7c51fff13c243b5d978c5336d034017b=1521771043',
    'Host':'wugengji.feiwan.net',
    'User-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_5_8) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.801.0 Safari/535.1'
}


Get_contents(starturl,header=header)
with open('content.txt','r')as f:
    for line in f.readlines():
        chapter,url=line.rstrip().split('\t')
        logging.info('Gengnerate Download List:%s'%chapter)
        os.makedirs(chapter,exist_ok=True)
        Get_Img(url,chapter)
        time.sleep(2)