import os
import json
import argparse
import cv2


def kitti2coco(label_dir, img_dir, output_dir, suffix):
    # Create COCO annotation structure
    coco = {}
    coco['images'] = []
    coco['annotations'] = []
    coco['categories'] = []

    # Add categories
    categories = [
        {'id': 1, 'name': 'Car'},
        {'id': 2, 'name': 'Pedestrian'},
        {'id': 3, 'name': 'Cyclist'}
    ]
    coco['categories'] = categories

    # Add images and annotations
    image_id = 0
    annotation_id = 0

    for file in os.listdir(label_dir):
        if file.endswith('.txt'):
            image_path = os.path.join(img_dir, file[:-4] + '.png')
            
            # 读取图片的高宽
            img_file = cv2.imread(image_path)
            img_height, img_width = img_file.shape[0],img_file.shape[1]
            
            image = {
                'id': image_id,
                'file_name': file[:-4] + '.png',
                'height': img_height, # KITTI image height
                'width': img_width # KITTI image width
            }
            coco['images'].append(image)

            with open(os.path.join(label_dir, file), 'r') as f:
                lines = f.readlines()
                for line in lines:
                    line = line.strip().split(' ')
                    category_id = 1 if line[0] == 'Car' else 2 if line[0] == 'Pedestrian' else 3
                    bbox = [float(coord) for coord in line[4:8]]

                    x1, y1, x2, y2 = bbox
                    bbox_width = x2 - x1
                    bbox_height = y2 - y1


                    annotation = {
                        'id': annotation_id,
                        'image_id': image_id,
                        'category_id': category_id,
                        'bbox': [x1, y1, bbox_width,bbox_height],
                        'area': bbox_height*bbox_width,
                        'iscrowd': 0
                    }
                    coco['annotations'].append(annotation)
                    annotation_id += 1

            image_id += 1

    # Write COCO annotation to file
    with open(os.path.join(output_dir, 'instances_'+ suffix + '2017' +'.json'), 'w') as f:
        json.dump(coco, f)

if __name__ == '__main__':

    '''

    目录结构：
    data_root
    ├── annotations
    ├── labels
    │   ├── train_labels
    │   └── val_labels
    ├── train2017
    └── val2017

    '''
    data_root = '/data2/2022/kyb/datasets/kitti2cocotest/kitti_coco/'

    # 输出路径
    outputs_path = os.path.join(data_root, 'annotations')
    os.makedirs(outputs_path, exist_ok=True)

    
    train_img_dir = os.path.join(data_root, 'train2017')    # 训练集图片的路径
    train_label_dir = os.path.join(data_root, 'labels/train_labels')    # 训练集label的路径
    kitti2coco(train_label_dir, train_img_dir, outputs_path, 'train')   # 转换训练集标注格式

    val_img_dir = os.path.join(data_root, 'val2017')    # 验证集图片的路径
    val_label_dir = os.path.join(data_root, 'labels/val_labels')    # 验证集label的路径
    kitti2coco(val_label_dir, val_img_dir, outputs_path, 'val') # 转换验证集标注格式

    print('格式转换完成！')
