# Nuclear image synthesis and segmentation code

This repository contains source code for the following paper:  
Robust Histopathology Image Analysis: to Label or to Synthesize? Hou, Le and Agarwal, Ayush and Samaras, Dimitris and Kurc, Tahsin M and Gupta, Rajarsi R and Saltz, Joel H. Computer Vision and Pattern Recognition (CVPR), 2019

The codes have been used to generate the datasets published in the following paper: 

Le Hou, Rajarsi Gupta, John S. Van Arnam, Yuwei Zhang, Kaustubh Sivalenka, Dimitris Samaras, Tahsin M. Kurc, and Joel H. Saltz. Dataset of segmented nuclei in hematoxylin and eosin stained histopathology images of ten cancer types. Sci Data 7, 185 (2020). https://doi.org/10.1038/s41597-020-0528-1

You need the following python2 libraries to run this software:  
```
tensorflow  
scipy  
numpy  
json  
pickle
cv2 
```

If you want to obtain initial synthetic images with nuclear masks, please read training-data-synthesis/README.md  
If you want to train your nuclei segmentation model, or use our trained nuclei segmentation model, please read segmentation-of-nuclei/README.md 

This software uses several open source repositories, especially [this one](https://github.com/carpedm20/simulated-unsupervised-tensorflow)

## Trained model and released segmentation results

We also include:  
1. A Dockerfile with trained model [here](Dockerfile)  
2. Segmentation results we've already generated [here](https://stonybrookmedicine.app.box.com/s/7n9gdy3i6qmm638or7lbxrzzydb1iv9b) with [readme](https://stonybrookmedicine.app.box.com/notes/461635773066?s=7n9gdy3i6qmm638or7lbxrzzydb1iv9b).


## Docker

for Ubuntu, install Docker following these steps
```
sudo apt-get remove docker docker-engine docker.io containerd runc
```

```
 sudo apt-get update
 sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
```

```
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
```

```
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

```
 sudo apt-get update
 sudo apt-get install docker-ce docker-ce-cli containerd.io
```

# Verify docker engine is installed

```
sudo docker run hello-world
```
 
