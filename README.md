# kitti2coco
convert kitti 2D object detection dataset to coco format



I can't find the code to convert kitti 2D detection dataset to coco format.So I code it myself.There are 3 files in this repository:

- `modify_annotations_txt.py` : merge the similar class in kitti.'Van', 'Truck', 'Tram' is merged into 'Car'.'Person_sitting' is merged into 'Pedestrian'. 'Misc' and 'Dontcare' are ignored.
- `split_datasets.py` : split dataset into train set and val set according to a certain proportion.(default 9 : 1)
- `kitti2coco.py` : read the label in kitti and reorgnize them in coco format and save as a  json file.



**First step : we should origanize files into the following structure. Then execute `modify_annotations_txt.py`, the file can merge some similar class.**

```
data_dir
├── kitti
│   ├── image_2
│   │   ├── 000000.png
│   │   ├── 000001.png
│   │   ├── 000002.png
│   │   ├── 000003.png
│   │   ├── 000004.png
│   │   └── 000005.png
│   └── label_2
│       ├── 000000.txt
│       ├── 000001.txt
│       ├── 000002.txt
│       ├── 000003.txt
│       ├── 000004.txt
│       └── 000005.txt
```

**Second step : execute `split_datasets.py`. Then we can obtain the structure as follow:**

```
dest_dir
├── annotations
├── labels
│   ├── train_labels
│   └── val_labels
├── train2017
└── val2017
```

**Third step : execute `kitti2coco.py`.And the process is completed.We can get the kitti dataset of coco format.**

```
kitti_coco
├── annotations
│   ├── instances_train2017.json
│   └── instances_val2017.json
├── labels
│   ├── train_labels
│   │   ├── 000000.txt
│   │   ├── 000001.txt
│   │   ├── 000002.txt
│   │   ├── 000004.txt
│   │   └── 000005.txt
│   └── val_labels
│       └── 000003.txt
├── train2017
│   ├── 000000.png
│   ├── 000001.png
│   ├── 000002.png
│   ├── 000004.png
│   └── 000005.png
└── val2017
    └── 000003.png
```

