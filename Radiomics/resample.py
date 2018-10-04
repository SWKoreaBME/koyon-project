from data_utils import *
import os
'''
    resample.py

    resample nifti file to voxel size you want and save as .nii file

    18 / 10 / 4
        binary error solved
'''

raw_path='path/to/data'
save_path='path/to/save'

voxel_size=(1, 1, 1)

for subject in os.listdir(raw_path):
    images=[img for img in os.listdir(os.path.join(raw_path, subject)) if 'nii' in img]
    for im in images:
        data=os.path.join(raw_path, subject, im)

        im_file_resampled, im_voxel = resample(data, voxel_size)
        if 'mask' in im:
            im_file_resampled = mask2binary(im_file_resampled)
        
        new_name=im.split('.nii')[0]
        save_file(new_name, im_file_resampled, save_path, im_voxel)
        print(im_file_resampled.shape)
        print(data, '-- Done')