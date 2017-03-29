import glob
import re
import pandas as pd
from PIL import Image
from PIL import ImageStat
import cv2
from app.face_detect import *


def load_image(infilename):
    img = Image.open(infilename)
    return img


def image_extract_all(path):
    data_lst = list()
    for fname in glob.glob(path):

        # load image for PIL and OpenCV packages
        im = load_image(fname)
        cv_im = cv2.imread(fname)
        gray = cv2.cvtColor(cv_im, cv2.COLOR_BGR2GRAY)

        #

        if len(im.getbands()) == 3:
            image_dict = {
                'image_key': re.findall('\d+', fname)[0],
                'R_max': ImageStat.Stat(im).extrema[0][1],
                'G_max': ImageStat.Stat(im).extrema[1][1],
                'B_max': ImageStat.Stat(im).extrema[2][1],
                'image_width': im.size[0],
                'image_height': im.size[1],
                'R_sum': ImageStat.Stat(im).sum[0],
                'G_sum': ImageStat.Stat(im).sum[1],
                'B_sum': ImageStat.Stat(im).sum[2],
                'R_sum2': ImageStat.Stat(im).sum2[0],
                'G_sum2': ImageStat.Stat(im).sum2[1],
                'B_sum2': ImageStat.Stat(im).sum2[2],
                'R_mean': ImageStat.Stat(im).mean[0],
                'G_mean': ImageStat.Stat(im).mean[1],
                'B_mean': ImageStat.Stat(im).mean[2],
                'R_median': ImageStat.Stat(im).median[0],
                'G_median': ImageStat.Stat(im).median[1],
                'B_median': ImageStat.Stat(im).median[2],
                'R_rms': ImageStat.Stat(im).rms[0],
                'G_rms': ImageStat.Stat(im).rms[1],
                'B_rms': ImageStat.Stat(im).rms[2],
                'R_var': ImageStat.Stat(im).var[0],
                'G_var': ImageStat.Stat(im).var[1],
                'B_var': ImageStat.Stat(im).var[2],
                'R_stddev': ImageStat.Stat(im).stddev[0],
                'G_stddev': ImageStat.Stat(im).stddev[1],
                'B_stddev': ImageStat.Stat(im).stddev[2],
                'luminance': 0.299 * ImageStat.Stat(im).sum[0] + 0.587 * ImageStat.Stat(im).sum[1] + 0.114 * ImageStat.Stat(im).sum[2],
                'percieved_luminance': 0.299 * ImageStat.Stat(im).sum2[0] + 0.587 * ImageStat.Stat(im).sum2[1] + 0.114 * ImageStat.Stat(im).sum2[2],
                'blur': cv2.Laplacian(cv_im, cv2.CV_64F).var(),
                'num_faces': num_faces(gray)
            }
        else:
            pass

        data_lst.append(image_dict)
        # print(str(fname) + ' complete')

    image_df = pd.DataFrame(data_lst)

    return image_df


def image_extract(image):
    data_lst = list()
    # for fname in glob.glob(path):

    # load image for PIL and OpenCV packages
    im = load_image(image)
    cv_im = cv2.imread(image)
    gray = cv2.cvtColor(cv_im, cv2.COLOR_BGR2GRAY)

    #

    if len(im.getbands()) == 3:
        image_dict = {
            # 'image_key': re.findall('\d+', fname)[0],
            'R_max': ImageStat.Stat(im).extrema[0][1],
            'G_max': ImageStat.Stat(im).extrema[1][1],
            'B_max': ImageStat.Stat(im).extrema[2][1],
            'image_width': im.size[0],
            'image_height': im.size[1],
            'R_sum': ImageStat.Stat(im).sum[0],
            'G_sum': ImageStat.Stat(im).sum[1],
            'B_sum': ImageStat.Stat(im).sum[2],
            'R_sum2': ImageStat.Stat(im).sum2[0],
            'G_sum2': ImageStat.Stat(im).sum2[1],
            'B_sum2': ImageStat.Stat(im).sum2[2],
            'R_mean': ImageStat.Stat(im).mean[0],
            'G_mean': ImageStat.Stat(im).mean[1],
            'B_mean': ImageStat.Stat(im).mean[2],
            'R_median': ImageStat.Stat(im).median[0],
            'G_median': ImageStat.Stat(im).median[1],
            'B_median': ImageStat.Stat(im).median[2],
            'R_rms': ImageStat.Stat(im).rms[0],
            'G_rms': ImageStat.Stat(im).rms[1],
            'B_rms': ImageStat.Stat(im).rms[2],
            'R_var': ImageStat.Stat(im).var[0],
            'G_var': ImageStat.Stat(im).var[1],
            'B_var': ImageStat.Stat(im).var[2],
            'R_stddev': ImageStat.Stat(im).stddev[0],
            'G_stddev': ImageStat.Stat(im).stddev[1],
            'B_stddev': ImageStat.Stat(im).stddev[2],
            'luminance': 0.299 * ImageStat.Stat(im).sum[0] + 0.587 * ImageStat.Stat(im).sum[1] + 0.114 * ImageStat.Stat(im).sum[2],
            'percieved_luminance': 0.299 * ImageStat.Stat(im).sum2[0] + 0.587 * ImageStat.Stat(im).sum2[1] + 0.114 * ImageStat.Stat(im).sum2[2],
            'blur': cv2.Laplacian(cv_im, cv2.CV_64F).var(),
            'num_faces': num_faces(gray)
        }
    else:
        pass

    data_lst.append(image_dict)
    # print(str(fname) + ' complete')

    image_df = pd.DataFrame(data_lst)

    return image_df
