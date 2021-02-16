import os
import requests
import urllib.request
from tqdm import tqdm
from urllib.parse import urlparse

class DownloadFile:

    def __init__(self, url):
        self.url = url

    def get_filename(self):
        ffile = urlparse(self.url)
        self.ffile = ffile
        self.ffile = os.path.basename(self.ffile.path)
        return self.ffile
    
    def get_filesize(self):
        fsize = urllib.request.urlopen(self.url)
        fsiz = fsize.length
        return '{:.2f} MB'.format(int(fsiz) / float(1 << 20))

    def download(self):
        req = requests.get(self.url, stream=True)
        buffer = 1024
        total_size = int(req.headers.get('content-length', 0))
        prog = tqdm(req.iter_content(buffer), total=total_size,
                    unit='KB', unit_scale=True)
        with open(DownloadFile.get_filename(self), 'wb') as f:
            for data in prog:
                prog.update(len(data))
                f.write(data)