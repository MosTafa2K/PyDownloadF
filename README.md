# PyDownloadF

## <span style="color:#22b6e3">Intro


* #### PyDownloadF is a free open-source module that download files from url and that can show and get file size/name from url.

> Notic : This project is a simple project written in Python3 language and made for training and experimental purposes.<br><br>
The libraries used for this project include :<br>
**OS**<br>
**requests**<br>
**urllib**<br>
**tqdm**<br>
<br><span style=color:#22b6e3>Don't forget if you no have some libraries of above, first install thats.<hr></span>
# <span style="color:#22b6e3">How to use
Example to ' Download File '
```python
from DownloadF import DownloadFile
DownloadFile("url").download()
```

Example to ' Get FileName '
```python
from DownloadF import DownloadFile
DownloadFile("url").get_filename()
```

Example to ' Get FileSize '
```python
from DownloadF import DownloadFile
DownloadFile("url").get_filesize()
```
# Thanks For using...