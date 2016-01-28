#%%
import matplotlib.pyplot as plt
import skimage.io
import skimage.filters
import os
import mahotas
import numpy

# Get path to current script
#folder = '/home/bbales2/web/seg/python/'
os.path.dirname(os.path.realpath(__file__))

imr4 = skimage.io.imread('{0}/../static/images/renen4.png'.format(folder), as_grey = True)
im88 = skimage.io.imread('{0}/../static/images/rene88.png'.format(folder), as_grey = True)

plt.figure(figsize = (6,4))
plt.imshow(imr4, cmap = plt.cm.gray, interpolation = 'None')
plt.tight_layout()
plt.savefig('{0}/../static/images/renen4plot.png'.format(folder), format='png', dpi = 150)
#plt.show()

plt.figure(figsize = (6,4))
plt.imshow(im88, cmap = plt.cm.gray, interpolation = 'None')
plt.tight_layout()
plt.savefig('{0}/../static/images/rene88plot.png'.format(folder), format='png', dpi = 150)


fimr4 = skimage.filters.gaussian_filter(imr4.astype('float'), 2.0)
fim88 = skimage.filters.gaussian_filter(im88.astype('float'), 2.0)

tr4 = skimage.filters.threshold_otsu(fimr4)
t88 = skimage.filters.threshold_otsu(fim88)

plt.figure(figsize = (6,4))
plt.imshow(fimr4, cmap = plt.cm.gray, interpolation = 'None')
plt.tight_layout()
plt.savefig('{0}/../static/images/renen4blur.png'.format(folder), format='png', dpi = 150)
#plt.show()

plt.figure(figsize = (6,4))
plt.imshow(fim88, cmap = plt.cm.gray, interpolation = 'None')
plt.tight_layout()
plt.savefig('{0}/../static/images/rene88blur.png'.format(folder), format='png', dpi = 150)

#Show
plt.figure(figsize = (6,4))
plt.imshow(fimr4 > tr4, cmap = plt.cm.gray, interpolation = 'None')
plt.tight_layout()
plt.savefig('{0}/../static/images/renen4otsu.png'.format(folder), format='png', dpi = 150)
#plt.show()

plt.figure(figsize = (6,4))
plt.imshow(fim88 > t88, cmap = plt.cm.gray, interpolation = 'None')
plt.tight_layout()
plt.savefig('{0}/../static/images/rene88otsu.png'.format(folder), format='png', dpi = 150)
#plt.show()
#%%
mark = mahotas.labeled.borders((fimr4 >= tr4))
plt.figure(figsize = (6,4))
plt.imshow(imr4, interpolation = 'None', cmap = plt.cm.gray)
plt.imshow(numpy.ma.masked_where(mark < 0.1, mark), interpolation = 'None')
plt.tight_layout()
plt.savefig('{0}/../static/images/renen4otsuBorders.png'.format(folder), format='png', dpi = 150)

#%%
print numpy.mean(imr4[:, :imr4.shape[1] / 2])
print numpy.mean(imr4[:, imr4.shape[1] / 2:])
print tr4

#tr4 = skimage.filters.threshold_otsu(imr4)
#t88 = skimage.filters.threshold_otsu(im88)
#Write thresholded versions
