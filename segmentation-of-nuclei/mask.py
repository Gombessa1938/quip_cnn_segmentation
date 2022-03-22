from extract_patch_segmentation_mask import extract_segmentation_mask
import matplotlib.pyplot as plt
import numpy as np
from tqdm import trange
from PIL import Image


HE_image = np.array(Image.open('/home/pictorlambdanode3/Desktop/seg_folder/svs/crop_1.png'))



def color_bin(bin_labl):
    """
    Colors bin image so that nuclei come out nicer.
    """
    dim = bin_labl.shape
    x, y = dim[0], dim[1]
    res = np.zeros(shape=(x, y, 3))
    for i in trange(1, bin_labl.max() + 1):
        rgb = np.random.normal(loc = 125, scale=100, size=3)
        rgb[rgb < 0 ] = 0
        rgb[rgb > 255] = 255
        rgb = rgb.astype(np.uint8)
        res[bin_labl == i] = rgb
    return res.astype(np.uint8)


segmentation_polygon_folder = '/home/pictorlambdanode3/Desktop/seg_folder/seg_tiles/TU_Liver8.svs'
x = 16001
y = 28001
patch_width=4000
mask = extract_segmentation_mask(segmentation_polygon_folder, x, y, patch_width, scale_to_40X=False)
mask = color_bin(mask)
plt.imshow(HE_image)
plt.imshow(mask,alpha=0.5)
plt.savefig('result.png',dpi=600)

#plt.show()
