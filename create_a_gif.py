# had to install imageio and python and now importing
import imageio.v3 as iio

# here you include the .png files for your gif
filenames = ['image1.png', 'image2.png', 'image3.png']
# where the image files go
images = []

for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite('animated_from_images.gif', images, duration = 500, loop = 0)
