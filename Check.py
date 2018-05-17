import os
from PIL import Image
#import logging

#logging.basicConfig(level=logging.info,format='%(asctime)s - %(levelname)s - %(message)s')

def ImaginCheck(file):
    bValid=True
    try:
        Image.open(file).verify()
    except:
        bValid = False
    return bValid
for root,dirs,files in os.walk('.'):
    for file in files:
        if file.endswith('.jpg'):
            file=os.path.join(root,file)
            if not ImaginCheck(file):
                print('file %s removed!'%file)
                os.remove(file)