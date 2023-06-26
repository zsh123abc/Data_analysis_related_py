import cv2
import os

def cap_img(video_path, img_dirpath):
    vidcap = cv2.VideoCapture(video_path)
    success,image = vidcap.read()
    count = 0
    success = True
    if not os.path.exists(img_dirpath):
        os.makedirs(img_dirpath)
    while success:
        success,image = vidcap.read()
        if count%10==0:
            # print(count)
            video_name = video_path.split('\\')[-1]
            # image_path=(img_dirpath + '\\' + ("%s_frame_%s.jpg" % (video_name, str(count).zfill(3))))
            image_path = (img_dirpath + '\\' + ("%s_%04d.jpg" % (video_name.split('.')[0], count)))
            try:
                cv2.imwrite(image_path, image)     # save frame as JPEG file
                print('image_path:::', image_path)
            except Exception as e:
                print('Error:', e)
                print(video_path)
            # if cv2.waitKey(10) == 27:
            #     break
        count += 1
        # cv2.waitKey(0)

if __name__ == "__main__":
    root_dir = r'C:\Users\cwj\Documents\WXWork\1688856502407527\Cache\Video\2023-06\625'

    for filename in os.listdir(root_dir):

            video_path = os.path.join(root_dir, filename)
            # img_dirpath = os.path.join(root_dir,video_path[:-4])
            # img_dir_path = r'F:/tmp/data/data/4/images'
            img_dirpath = root_dir+"/img"
            cap_img(video_path, img_dirpath)