import os
import sys
import xml.etree.ElementTree as ET
import glob

def xml_to_txt(indir,outdir):

    os.chdir(indir)
    if not os.path.exists(outdir):
        os.mkdir(outdir)

    annotations = os.listdir('.')
    print(annotations)
    for i, file in enumerate(annotations):

        file_save = file.split('.')[0]+'.txt'
        file_txt=os.path.join(outdir,file_save)
        picname=annotations[i].split('.')[0]

        f_w = open(file_txt,'w')

        # actual parsing
        in_file = open(file)
        tree=ET.parse(in_file)
        root = tree.getroot()

        for obj in root.iter('object'):
                current = list()
                name = obj.find('name').text

                xmlbox = obj.find('bndbox')
                xn = xmlbox.find('xmin').text
                xx = xmlbox.find('xmax').text
                yn = xmlbox.find('ymin').text
                yx = xmlbox.find('ymax').text
                print (name)
                f_w.write(picname+'.png'+' '+name+' '+xn+' '+yn+' '+xx+' '+yx+' ')
                f_w.write('\n')


file = os.path.basename(__file__)
print(file)
indir='pic-15-label'   #xml目录
outdir='xml2txt'  #indir下txt目录
print(indir)
xml_to_txt(indir,outdir)
