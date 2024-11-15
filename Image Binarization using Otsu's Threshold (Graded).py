# -*- coding: utf-8 -*-
"""Assignment6.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1o73Q2wtVHjVXh1ZRiPujQzMB-vXg1Eid
"""

mean = float(input("Enter mean: "))
var = float(input("Enter variance: "))
std = var ** 0.5

def noiseimg(img):
    noise = np.random.normal(mean, std, img.shape)
    finalnoiseimg = np.clip(img + noise, 0, 255).astype(np.uint8)
    return finalnoiseimg

"""Bookpage 1"""

import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('/content/bookpage_1.jpeg', 0)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(gray_img)
plt.title('gray image')
plt.axis('off')
plt.show()


# Noise
noisyimg = noiseimg(img)
noisyrgbimg = cv2.cvtColor(noisyimg, cv2.COLOR_BGR2RGB)
plt.imshow(noisyrgbimg)
plt.title('Noisy image')
plt.axis('off')
plt.show()

histo = cv2.calcHist([gray_img], [0], None, [255], [0,255])

# Split histogram into two parts iteratively and calculate within-class variance
ans = []
for i in range(len(histo)):
    x, y = np.split(histo, [i])
    xmean = np.sum(x) / (img.shape[0] * img.shape[1])
    xvariance = np.sum([p*q for p, q in enumerate(x)]) / np.sum(x)
    x3 = np.sum([(p-xvariance)**2 * q for p,q in enumerate(x)]) / np.sum(x)
    x3 = np.nan_to_num(x3)

    ymean = np.sum(y) / (img.shape[0] * img.shape[1])
    yvariance = np.sum([p*q for p, q in enumerate(y)]) / np.sum(y)
    y3 = np.sum([(p-yvariance)**2 * q for p,q in enumerate(y)]) / np.sum(y)
    ans.append(xmean * x3 + ymean * y3)

# index corresponding to the minimum within-class variance
m = np.argmin(ans)
print(m)

# Threshold the image using the calculated threshold value
(threshvalue, binary) = cv2.threshold(gray_img, m, 255, cv2.THRESH_BINARY)

def thresholdvalue(img_title, normalized):
    image = cv2.imread(img_title, 0)
    return threshvalue


def main():
    thresholdvalue("/content/bookpage_1.jpeg",0)


if __name__ == "__main__":
    main()

import cv2
from matplotlib.ticker import FuncFormatter
from matplotlib import pyplot as plt



def call_otsu_threshold(img_title):
    image = cv2.imread(img_title, 0)

    # # Apply GaussianBlur to reduce image noise if it is required
    # if noise:
    #     image = cv2.GaussianBlur(image, (5, 5), 0)

    # initial image histogram
    plt.hist(image.ravel(), 256)
    plt.xlabel('Colour intensity')
    plt.ylabel('Number of pixels')
    plt.show()
    plt.close()

    otsu_threshold, image_result = cv2.threshold(
        image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU,
    )
    print("Obtained threshold: ", otsu_threshold)

    #resulting image histogram
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.hist(image_result.ravel(), 256)
    ax.set_xlabel('Colour intensity')
    ax.set_ylabel('Number of pixels')
    # Get rid of 1e7
    ax.yaxis.set_major_formatter(FuncFormatter(lambda x, pos: ('%1.1fM') % (x*1e-6)))
    plt.show()
    plt.close()

    # after applying otsu method
    plt.imshow(image_result, cmap='gray')
    plt.title("Otsu's thresholding result")
    plt.axis('off')
    plt.show()


def main():
    call_otsu_threshold("/content/bookpage_1.jpeg")
    thresholdvalue("/content/bookpage_1.jpeg",0)


if __name__ == "__main__":
    main()

"""Panther"""

import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('/content/panther.jpeg', 0)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(gray_img)
plt.title('gray image')
plt.axis('off')
plt.show()

# Noise
noisyimg = noiseimg(img)
noisyrgbimg = cv2.cvtColor(noisyimg, cv2.COLOR_BGR2RGB)
plt.imshow(noisyrgbimg)
plt.title('Noisy image')
plt.axis('off')
plt.show()


histo = cv2.calcHist([gray_img], [0], None, [255], [0,255])


# calculating within-class variance
ans = []
for i in range(len(histo)):
    x, y = np.split(histo, [i])
    xmean = np.sum(x) / (img.shape[0] * img.shape[1])
    xvariance = np.sum([p*q for p, q in enumerate(x)]) / np.sum(x)
    x3 = np.sum([(p-xvariance)**2 * q for p,q in enumerate(x)]) / np.sum(x)
    x3 = np.nan_to_num(x3)

    ymean = np.sum(y) / (img.shape[0] * img.shape[1])
    yvariance = np.sum([p*q for p, q in enumerate(y)]) / np.sum(y)
    y3 = np.sum([(p-yvariance)**2 * q for p,q in enumerate(y)]) / np.sum(y)
    ans.append(xmean * x3 + ymean * y3)

# index corresponding to the minimum within-class variance
m = np.argmin(ans)
print(m)

# Threshold the image using the calculated threshold value
(threshvalue, binary) = cv2.threshold(gray_img, m, 255, cv2.THRESH_BINARY)

def thresholdvalue(img_title, normalized):
    image = cv2.imread(img_title, 0)
    return threshvalue


def main():
    thresholdvalue("/content/panther.jpeg",0)


if __name__ == "__main__":
    main()


import cv2
from matplotlib.ticker import FuncFormatter
from matplotlib import pyplot as plt



def call_otsu_threshold(img_title):
    image = cv2.imread(img_title, 0)

    # # Apply GaussianBlur to reduce image noise if it is required
    # if noise:
    #     image = cv2.GaussianBlur(image, (5, 5), 0)

    # View initial image histogram
    plt.hist(image.ravel(), 256)
    plt.xlabel('Colour intensity')
    plt.ylabel('Number of pixels')
    plt.show()
    plt.close()

    otsu_threshold, image_result = cv2.threshold(
        image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU,
    )
    print("Obtained threshold: ", otsu_threshold)

    # View the resulting image histogram
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.hist(image_result.ravel(), 256)
    ax.set_xlabel('Colour intensity')
    ax.set_ylabel('Number of pixels')
    # Get rid of 1e7
    ax.yaxis.set_major_formatter(FuncFormatter(lambda x, pos: ('%1.1fM') % (x*1e-6)))
    plt.show()
    plt.close()

    # after applying otsu method
    plt.imshow(image_result, cmap='gray')
    plt.title("Otsu's thresholding result")
    plt.axis('off')
    plt.show()


def main():
    call_otsu_threshold("/content/panther.jpeg")
    thresholdvalue("/content/panther.jpeg",0)


if __name__ == "__main__":
    main()

"""Tom"""

import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('/content/tom.jpeg', 0)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(gray_img)
plt.title('gray image')
plt.axis('off')
plt.show()

# Noise
noisyimg = noiseimg(img)
noisyrgbimg = cv2.cvtColor(noisyimg, cv2.COLOR_BGR2RGB)
plt.imshow(noisyrgbimg)
plt.title('Noisy image')
plt.axis('off')
plt.show()


histo = cv2.calcHist([gray_img], [0], None, [255], [0,255])


# Split histogram into two parts iteratively and calculate within-class variance
ans = []
for i in range(len(histo)):
    x, y = np.split(histo, [i])
    xmean = np.sum(x) / (img.shape[0] * img.shape[1])
    xvariance = np.sum([p*q for p, q in enumerate(x)]) / np.sum(x)
    x3 = np.sum([(p-xvariance)**2 * q for p,q in enumerate(x)]) / np.sum(x)
    x3 = np.nan_to_num(x3)

    ymean = np.sum(y) / (img.shape[0] * img.shape[1])
    yvariance = np.sum([p*q for p, q in enumerate(y)]) / np.sum(y)
    y3 = np.sum([(p-yvariance)**2 * q for p,q in enumerate(y)]) / np.sum(y)
    ans.append(xmean * x3 + ymean * y3)

# index corresponding to the minimum within-class variance
m = np.argmin(ans)
print(m)

# Threshold the image using the calculated threshold value
(threshvalue, binary) = cv2.threshold(gray_img, m, 255, cv2.THRESH_BINARY)

def thresholdvalue(img_title, normalized):
    image = cv2.imread(img_title, 0)
    return threshvalue


def main():
    thresholdvalue("/content/tom.jpeg",0)


if __name__ == "__main__":
    main()


import cv2
from matplotlib.ticker import FuncFormatter
from matplotlib import pyplot as plt



def call_otsu_threshold(img_title):
    image = cv2.imread(img_title, 0)

    # # Apply GaussianBlur to reduce image noise if it is required
    # if noise:
    #     image = cv2.GaussianBlur(image, (5, 5), 0)

    # View initial image histogram
    plt.hist(image.ravel(), 256)
    plt.xlabel('Colour intensity')
    plt.ylabel('Number of pixels')
    plt.show()
    plt.close()

    otsu_threshold, image_result = cv2.threshold(
        image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU,
    )
    print("Obtained threshold: ", otsu_threshold)

    # View the resulting image histogram
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.hist(image_result.ravel(), 256)
    ax.set_xlabel('Colour intensity')
    ax.set_ylabel('Number of pixels')
    # Get rid of 1e7
    ax.yaxis.set_major_formatter(FuncFormatter(lambda x, pos: ('%1.1fM') % (x*1e-6)))
    plt.show()
    plt.close()

    # after applying otsu method
    plt.imshow(image_result, cmap='gray')
    plt.title("Otsu's thresholding result")
    plt.axis('off')
    plt.show()


def main():
    call_otsu_threshold("/content/tom.jpeg")
    thresholdvalue("/content/tom.jpeg",0)


if __name__ == "__main__":
    main()

import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('/content/bookpage_2.jpeg', 0)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(gray_img)
plt.title('gray image')
plt.axis('off')
plt.show()

# Noise
noisyimg = noiseimg(img)
noisyrgbimg = cv2.cvtColor(noisyimg, cv2.COLOR_BGR2RGB)
plt.imshow(noisyrgbimg)
plt.title('Noisy image')
plt.axis('off')
plt.show()


histo = cv2.calcHist([gray_img], [0], None, [255], [0,255])


# Split histogram into two parts iteratively and calculate within-class variance
ans = []
for i in range(len(histo)):
    x, y = np.split(histo, [i])
    xmean = np.sum(x) / (img.shape[0] * img.shape[1])
    xvariance = np.sum([p*q for p, q in enumerate(x)]) / np.sum(x)
    x3 = np.sum([(p-xvariance)**2 * q for p,q in enumerate(x)]) / np.sum(x)
    x3 = np.nan_to_num(x3)

    ymean = np.sum(y) / (img.shape[0] * img.shape[1])
    yvariance = np.sum([p*q for p, q in enumerate(y)]) / np.sum(y)
    y3 = np.sum([(p-yvariance)**2 * q for p,q in enumerate(y)]) / np.sum(y)
    ans.append(xmean * x3 + ymean * y3)

# index corresponding to the minimum within-class variance
m = np.argmin(ans)
print(m)

# Threshold the image using the calculated threshold value
(threshvalue, binary) = cv2.threshold(gray_img, m, 255, cv2.THRESH_BINARY)

def thresholdvalue(img_title, normalized):
    image = cv2.imread(img_title, 0)
    return threshvalue


def main():
    thresholdvalue("/content/bookpage_2.jpeg",0)


if __name__ == "__main__":
    main()


import cv2
from matplotlib.ticker import FuncFormatter
from matplotlib import pyplot as plt



def call_otsu_threshold(img_title):
    image = cv2.imread(img_title, 0)

    # # Apply GaussianBlur to reduce image noise if it is required
    # if noise:
    #     image = cv2.GaussianBlur(image, (5, 5), 0)

    # View initial image histogram
    plt.hist(image.ravel(), 256)
    plt.xlabel('Colour intensity')
    plt.ylabel('Number of pixels')
    plt.show()
    plt.close()

    otsu_threshold, image_result = cv2.threshold(
        image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU,
    )
    print("Obtained threshold: ", otsu_threshold)

    # View the resulting image histogram
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.hist(image_result.ravel(), 256)
    ax.set_xlabel('Colour intensity')
    ax.set_ylabel('Number of pixels')
    # Get rid of 1e7
    ax.yaxis.set_major_formatter(FuncFormatter(lambda x, pos: ('%1.1fM') % (x*1e-6)))
    plt.show()
    plt.close()

    # after applying otsu method
    plt.imshow(image_result, cmap='gray')
    plt.title("Otsu's thresholding result")
    plt.axis('off')
    plt.show()


def main():
    call_otsu_threshold("/content/bookpage_2.jpeg")
    thresholdvalue("/content/bookpage_2.jpeg",0)


if __name__ == "__main__":
    main()