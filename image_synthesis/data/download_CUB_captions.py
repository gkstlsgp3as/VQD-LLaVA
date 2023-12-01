import gdown
import os
from urllib import request

## download birds.zip from google drive
url = 'https://drive.google.com/uc?id=1O_LtUP9sch09QH3s_EBAgLEctBQ5JBSJ'
fname = 'birds.zip'
gdown.download(url, fname, quiet=False)

os.mkdirs('../../DATA/CUB-200/text', exist_ok=True)

## download pretrained files 
url = 'https://facevcstandard.blob.core.windows.net/t-shuygu/release_model/VQ-Diffusion/pretrained_model/ViT-B-32.pt?sv=2021-10-04&st=2023-05-30T06%3A44%3A27Z&se=2030-05-31T06%3A44%3A00Z&sr=b&sp=r&sig=7y5lmD6yhIZUJsDPN80XtMcs5ip%2FtPR0OrX1MrLCalY%3D'
savename = 'ViT-B-32.pt'
request.urlretrieve(url, savename)
url = 'https://facevcstandard.blob.core.windows.net/t-shuygu/release_model/VQ-Diffusion/pretrained_model/taming_dvae/taming_f8_8192_openimages_last.pth?sv=2021-10-04&st=2023-05-30T06%3A45%3A45Z&se=2030-05-31T06%3A45%3A00Z&sr=b&sp=r&sig=PSQU46nW9ulhMSC7bzgoMrVMxtuw7bDnuBz0c%2FDlS5A%3D'
savename = 'taming_f8_8192_openimages_last.pth'
request.urlretrieve(url, savename)