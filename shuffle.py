import os
import shutil
import random
def shuffle(from_images,from_labels,to_images,to_labels):
    files=os.listdir(from_images)
    random.shuffle(files)
    i=1
    for file_name in files:
        normal_name= file_name[:-4]
        
        image_from_path=os.path.join(from_images,file_name)
        label_name= normal_name+".txt"
        label_from_path=os.path.join(from_labels,label_name)
        
        
        new_image_name=str(i)+".jpg"
        new_label_name=str(i)+".txt"
        
        image_to_path=os.path.join(to_images,new_image_name)
        label_to_path=os.path.join(to_labels,new_label_name)
        print(f" the file {image_from_path} to {image_to_path}")
        print(f" the file {label_from_path} to {label_to_path}")
        
        shutil.copyfile(image_from_path,image_to_path)
        shutil.copyfile(label_from_path,label_to_path)
        i+=1
    


from_labels="templabel"

from_images="tempimage"


to_labels="labels"


to_images="images"


shuffle(from_images,from_labels,to_images,to_labels)

