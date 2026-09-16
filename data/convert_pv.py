import xml.etree.ElementTree as ET
import os
import random
import shutil
from tqdm import tqdm

# ================= 配置区 =================
# 1. 类别列表 (严格按照你扫出来的顺序)
classes = ['scratch', 'hot_spot', 'broken', 'black_border', 'no_electricity']

# 2. 原始数据路径 (根据你的截图)
raw_xml_dir = './data/images/PV-Multi-Defect/Annotations'
raw_img_dir = './data/images/PV-Multi-Defect/JPEGImages'

# 3. 目标保存路径
save_root = 'datasets/pv_data'
train_ratio = 0.8  # 80% 训练, 20% 验证
# ==========================================

def convert(size, box):
    """ 将坐标转换为 YOLO 归一化格式 """
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    return (x * dw, y * dh, w * dw, h * dh)

def setup_dirs():
    """ 创建 YOLO 目录结构 """
    for split in ['train', 'val']:
        os.makedirs(os.path.join(save_root, 'images', split), exist_ok=True)
        os.makedirs(os.path.join(save_root, 'labels', split), exist_ok=True)

def main():
    setup_dirs()

    # 获取所有图片文件
    img_files = [f for f in os.listdir(raw_img_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    random.seed(42)
    random.shuffle(img_files)

    split_idx = int(len(img_files) * train_ratio)
    train_list = img_files[:split_idx]
    val_list = img_files[split_idx:]

    datasets = {'train': train_list, 'val': val_list}

    for split, files in datasets.items():
        print(f"正在处理 {split} 数据集...")
        for img_name in tqdm(files):
            basename = os.path.splitext(img_name)[0]
            xml_file = os.path.join(raw_xml_dir, basename + '.xml')

            if not os.path.exists(xml_file):
                print(f"警告: 找不到对应的 XML 文件: {xml_file}")
                continue

            # 1. 复制图片到目标文件夹
            shutil.copy(os.path.join(raw_img_dir, img_name),
                        os.path.join(save_root, 'images', split, img_name))

            # 2. 解析 XML 并生成 TXT 标签
            tree = ET.parse(xml_file)
            root = tree.getroot()
            size = root.find('size')
            width = int(size.find('width').text)
            height = int(size.find('height').text)

            with open(os.path.join(save_root, 'labels', split, basename + '.txt'), 'w') as f:
                for obj in root.iter('object'):
                    cls_name = obj.find('name').text
                    if cls_name not in classes:
                        continue

                    cls_id = classes.index(cls_name)
                    xmlbox = obj.find('bndbox')
                    b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text),
                         float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
                    bb = convert((width, height), b)
                    f.write(f"{cls_id} {' '.join([f'{a:.6f}' for a in bb])}\n")

    # 3. 生成 YAML 配置文件
    yaml_content = f"""
# PV Infrared Defect Dataset
train: {save_root}/images/train
val: {save_root}/images/val

nc: {len(classes)}
names: {classes}
"""
    with open('data/pv_thermal.yaml', 'w') as f:
        f.write(yaml_content)

    print(f"\n转换完成！")
    print(f"数据集位于: {save_root}")
    print(f"配置文件已生成: data/pv_thermal.yaml")

if __name__ == '__main__':
    main()
