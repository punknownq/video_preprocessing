import cv2
import os
from os.path import basename


filepath = "pic-10"
pathDir = os.listdir(filepath)
total_num = len(pathDir)
print(total_num)
i = 0
for item in pathDir:
    if item.endswith('.png'):
        src = os.path.join(filepath, item)
        dst = os.path.join(filepath, "TSD-Signal-00232-"+str(i).zfill(5)+".png")
        print(item,i)
        try:
            os.rename(src, dst)
            print ("converting %s to %s ..." % (src, dst))
            i = i + 1
        except:
            continue
print ("total %d to rename & converted %d jpgs" % (total_num, i))
