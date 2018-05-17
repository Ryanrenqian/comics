from concurrent import futures
import tqdm
import requests
from Download import ImagDowner
import logging,os
import collections
logging.disable(level=logging.DEBUG)
jobs=[]
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
def down_many(jobs):
    counter=collections.Counter()
    with futures.ThreadPoolExecutor(max_workers=5) as executor:
        to_do_map = {}
        for job in sorted(jobs):
            down=ImagDowner(*job)
            future=executor.submit(down.run,timeout=300)
            to_do_map[future]=job
        done_iter=futures.as_completed(to_do_map)
        done_iter=tqdm.tqdm(done_iter,total=len(jobs))
        for future in done_iter:
            try:
                res=future.result()
            except requests.exceptions.HTTPError as exc:
                error_msg='HTTP {res.status_code} - {res.reason}'
                error_msg=error_msg.format(res=exc.response)
            except requests.exceptions.ConnectionError as exc:
                error_msg='Connection error'
            except requests.exceptions.ReadTimeout as exc:
                error_msg = 'Time out'
            else:
                error_msg=''
            if error_msg:
                job=to_do_map[future]
                print('*** Error for{}:{}'.format(job,error_msg))

down_many(jobs)