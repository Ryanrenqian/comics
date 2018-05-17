import requests
import io
from PIL import Image

class Download:
    def __init__(self,url,output):
        self.url=url
        self.output=output
    def downChecker(self,data):
        pass
    def save(self):
        pass
    def run(self,check=True,restart=True):
        pass

class ImagDowner(Download):
    def downChecker(self,data):
        bValue=True
        try:
            Image.open(io.BytesIO(data)).verify()
        except:
            bValue=False
        return bValue

    def save(self):
        with open(self.output,'wb')as f:
            f.write(self.data)

    def run(self,params=None,check=True,timeout=10,**kwargs):
        res = requests.get(self.url, stream=True,timeout=timeout,**kwargs)
        with open(self.output, 'wb') as of:
            for chunk in res.iter_content(chunk_size=1024):
                if chunk:
                    of.write(chunk)
                    of.flush()
        return self.output

ImagDowner(url='http://img.feiwan.net/wugengji/manhua/2b59/10.jpg',output='test.jpg').run()