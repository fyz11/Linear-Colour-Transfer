# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 23:00:49 2018

@author: felix
"""

if __name__=="__main__":
    
    from color_transform import *
    import pylab as plt 
    import numpy as np 
    
    src_file = 'test_images/van_gogh.jpg'
    target_file = 'test_images/hist_2.jpg'
    
#    src_file = 'soma_bw.jpg'
#    target_file = 'soma_rgb.jpg'
    
    # read the images.
    src_img = read_rgb(src_file)
    target_img = read_rgb(target_file)


# =============================================================================
#   Example 0: Image Statistics Transfer Baseline. 
# =============================================================================
    print('============')
    print('Baseline Example : Recolor by matching means' )
    print('============')
    recolor_img_stats = color_transfer_stats(src_img, target_img)

    plt.figure(figsize=(15,5))
    plt.subplot(131)
    plt.title('Source image')
    plt.imshow(src_img)
    plt.subplot(132)
    plt.title('Target image')
    plt.imshow(target_img)
    plt.subplot(133)
    plt.title('Recolored image')
    plt.imshow(recolor_img_stats)
    plt.savefig('results/baseline.png', pad_inches=None, bbox_inches='tight')
    plt.show()


# =============================================================================
#   Example 1: Direct Transfer  
# =============================================================================
    print('============')
    print('Example 1: Recolor by linear transform' )
    print('============')
    # recolor based on the source image colors
    recolor_img = match_color(src_img, target_img, mode='sym', eps=1e-8, source_mask=None, target_mask=None)    
    
    plt.figure(figsize=(15,5))
    plt.subplot(131)
    plt.title('Source image')
    plt.imshow(src_img)
    plt.subplot(132)
    plt.title('Target image')
    plt.imshow(target_img)
    plt.subplot(133)
    plt.title('Recolored image')
    plt.imshow(recolor_img)
    plt.savefig('results/example1.png', pad_inches=None, bbox_inches='tight')
    plt.show()
    
    
# =============================================================================
#   Example 2: Masked Transfer  
# =============================================================================
    print('============')
    print('Example 2: Selective recoloring by linear transform using an image mask' )
    print('============')
    target_mask = np.ones(target_img.shape[:-1]); 
    target_mask[target_img.shape[0]//2-100:target_img.shape[0]//2+100, target_img.shape[1]//2-100:target_img.shape[1]//2+100] = 0
    recolor_img_mask = match_color(src_img, target_img, mode='sym', eps=1e-8, source_mask=None, target_mask=target_mask)    
    
    plt.figure(figsize=(15,5))
    plt.subplot(131)
    plt.title('Source image')
    plt.imshow(src_img)
    plt.subplot(132)
    plt.title('Target image')
    plt.imshow(target_img)
    plt.subplot(133)
    plt.title('Recolored image')
    plt.imshow(recolor_img_mask)
    plt.savefig('results/example2.png', pad_inches=None, bbox_inches='tight')
    plt.show()
    
    
    
# =============================================================================
#   Example 3: Selective Masked Transfer  
# =============================================================================
    print('============')
    print('Example 3: Selective color sampling and colouring by linear transform using image masks' )
    print('============')
    
    source_mask = np.zeros(src_img.shape[:-1]); 
    source_mask[50:250, 1000:1300] = 1
    target_mask = np.ones(target_img.shape[:-1]); 
    target_mask[target_img.shape[0]//2-100:target_img.shape[0]//2+100, target_img.shape[1]//2-100:target_img.shape[1]//2+100] = 0
    
    recolor_img_mask = match_color(src_img, target_img, mode='sym', eps=1e-8, source_mask=source_mask, target_mask=target_mask)    
    
    plt.figure(figsize=(15,5))
    plt.subplot(131)
    plt.title('Source image')
    plt.imshow(src_img)
    plt.imshow(source_mask*255, cmap='gray', alpha=0.5)
    plt.subplot(132)
    plt.title('Target image')
    plt.imshow(target_img)
    plt.subplot(133)
    plt.title('Recolored image')
    plt.imshow(recolor_img_mask)
    plt.savefig('results/example3.png', pad_inches=None, bbox_inches='tight')
    plt.show()
    
    