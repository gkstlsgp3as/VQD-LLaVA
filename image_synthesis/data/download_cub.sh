#!/usr/bin/env bash
wget https://data.caltech.edu/records/65de6-vp158/files/CUB_200_2011.tgz
tar -zxvf CUB_200_2011.tgz
rm CUB_200_2011.tgz && rm attributes.txt

python download_CUB_captions.py
unzip birds.zip 
unzip ./birds/text.zip
mv ./text/ ../../DATA/CUB-200/text
mv CUB_200_2011/images/ ../../DATA/CUB-200/
mv ./birds/train ../../DATA/CUB-200
mv ./birds/test ../../DATA/CUB-200

#python split_CUB.py
rm -r CUB_200_2011 birds
rm birds.zip

#move the pth file
mv ViT-B-32.pt ../../OUTPUT/pretrained_model
mv taming_f8_8192_openimages_last.pth ../../OUTPUT/pretrained_model/taming_dvae