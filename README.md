# Setup

- Install [python](https://www.python.org/downloads/)
- Install [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- Clone this repository.  Navigate to where you want it to live in a shell and run `git clone git@github.com:room202math/align_and_classify.git`
- Intall the python dependencies listed in requirements.txt: `pip install -r requirements.txt`

The OpenCV library listed in requirements.txt is a powerful tool for computer vision.  It's worth just having a look through the docs to see what's possible.

Finally, ChatGPT is your friend.  It's really good at writing simple code if you point it in the write direction, like "Use python opencv to combine two overlapping images into a superimage".

# Techniques

I see your problem as twofold.

## Image Registration

One, align overlapping images of the seafloor taken from different camera positions.  This problem is called *image registration*.  You will find many examples in the OpenCV documentation.

Run stitch_images.py in this repo to see a simple approach which works for a camera that has only been rotated between images.

## Image Classification

Second, classify regions in the superimage as belonging to different categories (presumably "mud", "assembly of jellyfish", etc.).  There are three flavors of this kind of classification:

1. Classification: Classify an entire image as belonging to one category or another.  When this needs to be done for a large image with different regions, one breaks it into rectangular subimages and classifies each one.
2. Object Detection: Draw a box around objects in an image and classify them.
3. Segmentation: Classify objects and draw their actual boundary.

As you would expect, these techniques are listed in order of increasing complexity.  Bigger models mean you need more training data.  So probably you want to start with a simple classifier.

The most user friendly (and also very performant) ML models for all of these tasks are the [YOLO models](https://github.com/ultralytics/ultralytics).  Their documentation is solid.  You can follow it to use their public models as-are, or train them on your own training data.  Note that the existing models will only know about generic classes like "dog", "bike", etc.  However, their inner layers are good at detecting image features in general, so they can be quickly trained on datasets with a different list of classes - this is called *transfer learning*.

The most performant segmentation model I've seen is Facebook's [SAM - Segment Anything Model](https://segment-anything.com/).  The last time I set it up to run somewhere on my machine it was a bit involved, but they may have made it easier since then.