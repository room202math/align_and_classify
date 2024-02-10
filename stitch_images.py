'''Stitch overlapping images into a superimage with the high-level Stitcher class.

This primarily works for images taken with a camera that just rotated, like a panorama.

It succeeds for the "rotated_camera" test images, and fails for "rotated_and_translated_camera".

For the latter, you'll probably need a more involved approach.
'''

import cv2

# Load the images
image1 = cv2.imread('./test_images/rotated_camera/1.jpg')
image2 = cv2.imread('./test_images/rotated_camera/2.jpg')

# Create a Stitcher object
stitcher = cv2.Stitcher_create()

# Stitch the images
status, superimage = stitcher.stitch([image1, image2])

# Check if stitching was successful
if status == cv2.Stitcher_OK:
    # Save or display the result
    cv2.imwrite('superimage.jpg', superimage)
    cv2.imshow('Superimage', superimage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Stitching failed!")

