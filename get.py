import os
import shutil

def move(path,to):
    for filename in os.listdir(path):
        filepath=os.path.join(path,filename)
        topath=os.path.join(to,filename)
        shutil.move(filepath, topath)

path1="train/labels"
path2="valid/labels"
path3="test/labels"

to="labels"
move(path1,to)
move(path2,to)
move(path3,to)
