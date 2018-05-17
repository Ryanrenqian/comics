import os,time
from crawl import *
from Download import  ImagDowner
alltime=103
logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')
proxy={'HTTP':"http://120.78.78.141:8888"}

def getjobs():
    jobs = []
    for root,dirs,files in os.walk('.'):
        for file in files:
            if file=='download.txt':
                with open(os.path.join(root,file),'r')as f:
                    for line in f.readlines():
                        try:
                            i,url,o=line.rstrip().split('\t')
                        except:
                            logging.debug('error %s in %s' % (line, os.path.join(root, file)))
                        if not os.path.exists(os.path.join(root,o)):
                            jobs.append((url,os.path.join(root,o)))
    return jobs
timeout=100
jobs=getjobs()
while len(jobs)!=0:
    for i in sorted(jobs):
        try:
            logging.info('Downloading %s' % i[1])
            sttime = time.time()
            ImagDowner(*i).run(proxies=proxy,timeout=timeout)
            endtime = time.time()
            sleeptime = alltime - endtime + sttime
            time.sleep(sleeptime)
        except:
            time.sleep(1)
            continue
    jobs=getjobs()
    timeout+=50
    alltime+=50
    logging.info('%d jobs left'%len(jobs))
