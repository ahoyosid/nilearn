"""
Basic nilearn example
=====================

A simple example showing how to load an existing Nifti file and use
basic nilearn functionalities.
"""

# Import the os module, for file manipulation
import os

#########################################################################
# Let us use an in-memory Nifti file that is shipped with nilearn
from nilearn.datasets import data

anat_filename = os.path.join(os.path.dirname(data.__file__),
                             'avg152T1_brain.nii.gz')
print('anat_filename: %s' % anat_filename)

#########################################################################
# Using simple function from nilearn for image manipulation
from nilearn import image

# functions containing 'img' can take either a filename or an image as input.
# Inputs here are given as: image filename and smoothing value in mm
smooth_anat_img = image.smooth_img(anat_filename, 3)

# While we are giving a file name as input, the object that is returned
# is a 'nibabel' object. It has data, and an affine stored in object.
anat_data = smooth_anat_img.get_data()
print('anat_data has shape: %s' % str(anat_data.shape))
anat_affine = smooth_anat_img.get_affine()
print('anat_affine has affine:\n%s' % anat_affine)

# Finally, object can also be passed to nilearn function
# First input now is a image/object with same smoothing value
smooth_anat_img = image.smooth_img(smooth_anat_img, 3)

#########################################################################
# Visualization using plotting tool `plot_anat` from nilearn
from nilearn import plotting

# positioning of the image coordinates given as a list [x, y, z]
cut_coords = [0, 0, 0]

# Like all functions in nilearn, plotting can be given filenames
plotting.plot_anat(anat_filename, cut_coords=cut_coords,
                   title='Anatomy image')

# Or nibabel objects
plotting.plot_anat(smooth_anat_img,
                   cut_coords=cut_coords,
                   title='Smoothed anatomy image')

#########################################################################
# Saving smoothed image to file
smooth_anat_img.to_filename('smooth_anat_img.nii.gz')

#########################################################################
# Finally, showing plots when used inside a terminal
plotting.show()
