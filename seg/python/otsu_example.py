import matplotlib.pyplot as plt
import skimage.io
import skimage.filters
import os

# Get path to current script
folder = os.path.dirname(os.path.realpath(__file__))

imr4 = skimage.io.imread('{0}/../static/images/renen4.png'.format(folder), as_grey = True)
im88 = skimage.io.imread('{0}/../static/images/rene88.png'.format(folder), as_grey = True)

imr4 = skimage.filters.gaussian_filter(imr4.astype('float'), 2.0)
im88 = skimage.filters.gaussian_filter(im88.astype('float'), 2.0)

tr4 = skimage.filters.threshold_otsu(bimr4)
t88 = skimage.filters.threshold_otsu(bim88)

plt.figure(figsize = (6,4))
plt.imshow(imr4, cmap = plt.cm.gray, interpolation = 'None')
plt.tight_layout()
plt.savefig('{0}/../static/images/renen4plot.png'.format(folder), format='png', dpi = 150)
#plt.show()

plt.figure(figsize = (6,4))
plt.imshow(im88, cmap = plt.cm.gray, interpolation = 'None')
plt.tight_layout()
plt.savefig('{0}/../static/images/rene88plot.png'.format(folder), format='png', dpi = 150)

#Show
plt.figure(figsize = (6,4))
plt.imshow(imr4 > tr4, cmap = plt.cm.gray, interpolation = 'None')
plt.tight_layout()
plt.savefig('{0}/../static/images/renen4otsu.png'.format(folder), format='png', dpi = 150)
#plt.show()

plt.figure(figsize = (6,4))
plt.imshow(im88 > t88, cmap = plt.cm.gray, interpolation = 'None')
plt.tight_layout()
plt.savefig('{0}/../static/images/rene88otsu.png'.format(folder), format='png', dpi = 150)
#plt.show()


#tr4 = skimage.filters.threshold_otsu(imr4)
#t88 = skimage.filters.threshold_otsu(im88)
#Write thresholded versions
