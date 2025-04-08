
from skimage.metrics import structural_similarity
import cv2
from PIL import Image
from skimage.transform import resize
#Works well with images of different dimensions
def orb_sim(img1, img2):
  # SIFT is no longer available in cv2 so using ORB
  orb = cv2.ORB_create()

  # detect keypoints and descriptors
  kp_a, desc_a = orb.detectAndCompute(img1, None)
  kp_b, desc_b = orb.detectAndCompute(img2, None)

  # define the bruteforce matcher object
  bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    
  #perform matches. 
  matches = bf.match(desc_a, desc_b)
  #Look for similar regions with distance < 50. Goes from 0 to 100 so pick a number between.
  similar_regions = [i for i in matches if i.distance < 50]  
  if len(matches) == 0:
    return 0
  return len(similar_regions) / len(matches)


#Needs images to be same dimensions
def structural_sim(img1, img2):

  sim, diff = structural_similarity(img1, img2, full=True)
  return sim

img00 = cv2.imread('elven_Chorus.jpg', 0)
img01 = cv2.imread('elven_Chorus_clear.jpg', 0)

#img1 = cv2.imread('images/BSE.jpg', 0)  # 714 x 901 pixels
#img2 = cv2.imread('images/BSE_noisy.jpg', 0)  # 714 x 901 pixels
img3 = cv2.imread('shelly2.png', 0)  # 203 x 256 pixels
img4 = cv2.imread('gale.jpg', 0)  # 203 x 256 pixels

orb_similarity1 = orb_sim(img00, img01)  #1.0 means identical. Lower = not similar
orb_similarity2= orb_sim(img00,img3)
orb_similarity3 = orb_sim(img00, img4)
#ssim1= structural_sim(img00,img01)
#ssim2= structural_sim(img00,img4)
print("Similarity using ORB is: ", orb_similarity1)
print("Similarity using ORB is: ", orb_similarity2)
print("Similarity using ORB is: ", orb_similarity3)
#print("Similarity using SSIM is: ", ssim2)
'''
#Resize for SSIM

img5 = resize(img3, (img01.shape[0], img01.shape[1]), anti_aliasing=True, preserve_range=True)

ssim = structural_sim(img01, img5) #1.0 means identical. Lower = not similar
print("Similarity using SSIM is: ", ssim)'''

import requests

img_data = requests.get('https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=368980&type=card').content
with open('image_name.jpg', 'wb') as handler:
    handler.write(img_data)


def imageMatch(img1,img2):
  img1 = cv2.resize(img1,(672,936))
  color_coverted1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
  cv2.imshow("OpenCV Image", img1)
  cv2.waitKey(0) 
  img1 = Image.fromarray(color_coverted1) 
  img1.show()
  width, height = img1.size
  left =0
  top=0
  right=width
  bottom=height/3
  img1TitleCrop= img1.crop((left,top,right,bottom))
  img1TitleCrop.show()

imageMatch(img00,img01)
