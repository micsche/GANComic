# Comic strip generation using GAN (in progress)

In the sytle of CartoonGAN https://openaccess.thecvf.com/content_cvpr_2018/papers/Chen_CartoonGAN_Generative_Adversarial_CVPR_2018_paper.pdf, this is an attempt to create a GAN using comic strips generated from real-photography.

## Data
![Comic vs Film Pictures](https://github.com/micsche/GANComic/blob/main/images/film1.png)


Conveniently, a comic strip Corto Maltese (authored by Hugo Pratt) has been inspired by film His Majesty O'Keefe starring Burt Lancaster. This allows us to take snippets of comic and tag them to a film image, as show above. The GAN needs  film and cartoon data to be processed for its training. 

It will be very difficult to find the exact cartoon frame matching a film frame. Therefore, the aim is to match person image segment to the cartoon image segmenting. The two image segments will be fed together in the GAN.


## Pipeline
![Pipeline](https://github.com/micsche/GANComic/blob/main/pipeline.svg)

Much of the pre-processing will be performed using a workhorse algorith Mask-RCNN. A Tensorflow 2.1 adaptation has been used (https://github.com/akTwelve/Mask_RCNN). 
Preprocessing 
1. Frame Finding: Mask R-CNN and OpenCV are used to detect the individual frames within the cartoon strip.

3. Text Removal (optional): Another Mask R-CNN detects handwritten text in a segment removal algorithm. This could be helpful and possibly not necessary.
  i. The Mask R-CNN has been programmed using synthetic data. Drawings have been internet-scraped from bing.com. Bubble-text has been generated using random snippets from "Dubliners" by James Joyce. Handwriting was done using the emnist dataset (https://www.nist.gov/itl/products-and-services/emnist-dataset).

![Bubble Text](https://github.com/micsche/GANComic/blob/main/images/bubbletext.png)
  
  ii. Training the Mask-RCNN, most of the text was being detected, with very little False Positives. However, there were parts of text not being detected. To aim for better training, we reused the True Positives captured in the training. Suspect is that the handwriting font used is particular to that cartoon segment.
  
![Bubble Text](https://github.com/micsche/GANComic/blob/main/images/bubbletext2.png)

Notice the more regular handwriting, than one use
  
3. Production of cartoon image segments and film image segments(todo). Human figure recognition by image segmentation is a stock label of Mask R-CNN. Trials have already been performed on the cartoon to be adequate. The same cannot be said for the film part of image segmentation, due to the low resolution/quality of the film. Some film processing might be required. The process will produce images, that are equivalent from film style to comic style. Testing is under way.

4. GAN (todo). A suitable GAN will be selected to perform transfer learning. CycleGAN and CartoonGAN are the first candidates. Two GANs will be trained to produce the relevant pictures (film vs cartoon). More on this further on.



