import os


img_dir = r'C:\Users\cwj\Documents\WXWork\1688856502407527\Cache\File\2023-06\625_snd_court_img\img'
xml_dir = r'C:\Users\cwj\Documents\WXWork\1688856502407527\Cache\File\2023-06\625_snd_court_img\json'


allusedxmls = []
file_imgs = os.listdir(img_dir)
file_xmls = os.listdir(xml_dir)
for file_name in file_imgs:

    file_name = file_name[:-4] + '.json'
    # print(file_name)
    allusedxmls.append(file_name)

for file_name in file_xmls:
    print(file_name)
    # if file_name not in allusedxmls:
    if file_name not in allusedxmls:
        path = xml_dir +'/'+ file_name
        os.remove(path) 