import os

string = "python train.py --name cub200_train --output ./OUTPUT/long_text3 --config_file configs/cub200.yaml --num_node 1 --tensorboard --caption_type long_text --gpu 2 --load_path ./OUTPUT/long_text3/cub200_train/checkpoint/last.pth"

os.system(string)

