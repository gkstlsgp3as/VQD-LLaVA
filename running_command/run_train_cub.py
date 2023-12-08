import os

string = "python train.py --name cub200_train --output ./OUTPUT/short_text2 --config_file configs/cub200.yaml --num_node 1 --tensorboard --caption_type short_text --gpu 3"#--load_path OUTPUT/pretrained_model/CC_pretrained.pth"

os.system(string)

