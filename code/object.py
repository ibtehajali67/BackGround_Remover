import cv2
import numpy as np
import os
import glob
from u2net_test import main
import argparse
parser = argparse.ArgumentParser(description="Process some integer.")
parser.add_argument('-m','--mask_dir',type=str,default="/home/ibtehaj/Documents/ibtehaj/art/back_ground_change/nft/generated_mask/" , help="path of mask of image")
parser.add_argument('-bg','--background_dir',type=str ,default="/home/ibtehaj/Documents/ibtehaj/art/back_ground_change/nft/background/*", help="path of mask of image")
parser.add_argument('-inn','--image_dir',type=str ,default="/home/ibtehaj/Documents/ibtehaj/art/back_ground_change/nft/Input", help="path of image")
parser.add_argument('-o','--out_dir',type=str , default="/home/ibtehaj/Documents/ibtehaj/art/back_ground_change/nft/output/", help="path of mask of image")
args=parser.parse_args()
main(args.image_dir,args.mask_dir)
mask=args.mask_dir+"/*.png"
images=args.image_dir+"/*"
def object_style(n,f,b,img,forg,bkg,out):
  img=cv2.imread(img) #input image mask
  forg=cv2.imread(forg) #forground_styled result image
  bkg=cv2.imread(bkg) #background_styled result image 
  h,w,_=forg.shape
  img=cv2.resize(img,(w,h))
  bkg=cv2.resize(bkg,(w,h))
  y,x =np.where(np.all(img > [0,0,0], axis=-1))
#  forg[y,x]=bkg[y,x]
  bkg[y,x]=forg[y,x]
  cv2.imwrite(out+f+"_"+b+".png",bkg)
def main():
    for x in glob.glob(mask):
      name=os.path.basename(x)
      name=name.split(".")[0]# mask name
      for forg in glob.glob(images):
        s=os.path.basename(forg)
        fr=s.split(".")[0]
        if fr==name:
            print(s)
            f=forg
            for back in glob.glob(args.background_dir):
                s=os.path.basename(back)
                bg=s.split(".")[0]# bg name
                b=back
                object_style(name,fr,bg,x,f,b,args.out_dir)
    print("done")
if __name__ == "__main__":
    main()
    
