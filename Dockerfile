FROM  tensorflow/tensorflow:1.14.0-gpu
MAINTAINER quip_cnn_segmentation

RUN 	apt-get -y update && \
	apt-get -y install git python-pip openslide-tools wget libsm6 && \
	pip install openslide-python scikit-image scipy numpy opencv-python==4.2.0.32 tqdm

WORKDIR /root

COPY    . /root/quip_cnn_segmentation/

RUN	cd /root/quip_cnn_segmentation/segmentation-of-nuclei/cnn_model && \
	tar -xzvf model_trained.tar.gz && rm -f model_trained.tar.gz 

ENV	BASE_DIR="/root/quip_cnn_segmentation/"
ENV	PATH="./":$PATH
WORKDIR /root/quip_cnn_segmentation/segmentation-of-nuclei

CMD ["/bin/bash"]
