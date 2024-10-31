# Better Image Captioning EnhancesText-to-Image Generation Performance![image](https://github.com/user-attachments/assets/58403a0c-e112-436e-8001-37337f742412)

[Shinhye Han](https://gkstlsgp3as.github.io/), [Sehyun Kwon](https://github.com/sehyunkwon), Jaeksuk Kim

---
Text-to-Image generation models like Stable Diffusion and Midjourney are demonstrating remarkable performance. Training these models requires a substantial number of image and text pair data. However, creating such datasets manually involves significant costs and often leads to the generation of noisy data. In this paper, we experimentally confirm that Vision Language Models can replace humans in creating these datasets. We also discuss what constitutes good data for training Text-to-Image generation models.

![1_model_arch](https://github.com/user-attachments/assets/e696447d-07c3-4c6d-b97b-6e6536eaec1e)
(sourced from original VQ-Diffusion paper: *arXiv:2111.14822*)

## Requirements
* Python 3.10.13, Pytorch 2.1.0+cu121

### :point_right: Results
https://github.com/user-attachments/assets/c8e791b5-eea6-4c63-93f2-42f7bdd82100


### :airplane: Training
#### Data Preparation - CUB-200
```
│CUB-200/
├──images/
│  ├── 001.Black_footed_Albatross/
│  ├── 002.Laysan_Albatross
│  ├── ......
├──text/
│  ├── text/
│  │   ├── 001.Black_footed_Albatross/
│  │   ├── 002.Laysan_Albatross
│  │   ├── ......
├──train/
│  ├── filenames.pickle
├──test/
│  ├── filenames.pickle
```

```
sh ./image_synthesis/data/bash download_cub.sh
```

#### label preparation - noisy, long, short text for CUB-200
You can download each text caption in below links:

org: https://drive.google.com/file/d/1DtE4IcGmLacDtdJ7hLiowkqDIdhSi7IV/view?usp=sharing

long: https://drive.google.com/file/d/1mdgylOkD8py0pDRxa4iXv2euM8ewbgJh/view?usp=sharing

short: https://drive.google.com/file/d/1B7gHZ0LnQ9SfzKhaDlI_Sbx6bYkUI_9f/view?usp=sharing

noisy: https://drive.google.com/file/d/1E2bdaX-nGPwKw7uv8hPmh4Zq2h0MtNuM/view?usp=sharing


#### Training
Train Text2Image generation on CUB200 dataset:
```
python running_command/run_train_cub.py

### directly 
python train.py --name cub200_train --config_file configs/cub200.yaml --num_node 1 --tensorboard --gpu 2
```

### :rocket: Inference 
To generate image from given text on MSCOCO/CUB/CC datasets:
```
from inference_VQ_Diffusion import VQ_Diffusion
VQ_Diffusion_model = VQ_Diffusion(config='OUTPUT/pretrained_model/config_text.yaml', path='OUTPUT/pretrained_model/cub_learnable.pth')

# Inference VQ-Diffusion
VQ_Diffusion_model.inference_generate_sample_with_condition("A group of elephants walking in muddy water", truncation_rate=0.86, save_root="RESULT", batch_size=4)

# Inference Improved VQ-Diffusion with learnable classifier-free sampling
VQ_Diffusion_model.inference_generate_sample_with_condition("A group of elephants walking in muddy water", truncation_rate=1.0, save_root="RESULT", batch_size=4, guidance_scale=3.0)
```

### 📞: Contact
If you have any questions, please feel free to contact me via `sienna.shhan@gmail.com`.


