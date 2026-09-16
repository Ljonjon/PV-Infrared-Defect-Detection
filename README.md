# PV Infrared Defect Detection

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.x-EE4C2C?logo=pytorch&logoColor=white)](https://pytorch.org/)
[![License](https://img.shields.io/badge/License-GPLv3-blue.svg)](LICENSE)
![Status](https://img.shields.io/badge/Status-Inference%20Ready-brightgreen)

面向光伏电站红外巡检的 **GBH-YOLOv5** 缺陷检测推理包。模型针对红外图像中的小目标和细长目标进行优化，可识别划痕、热点、破损、黑边和不发电五类缺陷。

> 测试数据集和训练好的 `best.pt` 模型不包含在本仓库中。如需获取，请发送邮件至 **ljonjon540122@gmail.com**，主题建议使用：`[PV Defect] Request test dataset and inference model`。

## Verified Metrics

原目录中的 `runs/` 文件夹为空，没有 `results.csv` 或独立验证日志。以下指标从 `weights/best.pt` 内嵌的 150 轮训练记录中提取，并以训练过程中用于选择最佳权重的 fitness 行为准。

| 指标 | 结果 |
|---|---:|
| Best epoch | 149 |
| Precision | 82.71% |
| Recall | 76.91% |
| mAP@0.5 | 80.60% |
| mAP@0.5:0.95 | 50.59% |
| Validation box loss | 0.03714 |
| Validation objectness loss | 0.02145 |
| Validation class loss | 0.00149 |

说明：

- 验证记录使用 960 × 960 输入分辨率。
- 这些指标来自模型 checkpoint 内嵌的训练验证记录，不等同于新的独立测试集复评。
- 原目录没有找到可用的训练日志、混淆矩阵或独立 held-out test 结果。

## 检测类别

| ID | 类别 | 中文说明 |
|---:|---|---|
| 0 | `scratch` | 划痕 |
| 1 | `hot_spot` | 局部热点 |
| 2 | `broken` | 破碎／物理损伤 |
| 3 | `black_border` | 黑边／边缘异常 |
| 4 | `no_electricity` | 不发电／组串异常 |

## 文件结构

```text
.
├── detect.py
├── data/
│   ├── convert_pv.py
│   ├── pv_thermal.yaml
│   └── README.md
├── models/
│   ├── common.py
│   ├── experimental.py
│   ├── export.py
│   ├── yolo.py
│   └── yolov5s_pv.yaml
├── utils/
├── test_images/JPEGImages/README.md
├── weights/README.md
├── requirements.txt
├── THIRD_PARTY_NOTICES.md
└── LICENSE
```

## 环境与快速开始

```bash
pip install -r requirements.txt
python detect.py
```

显式指定输入和模型：

```bash
python detect.py --weights weights/best.pt --source test_images/JPEGImages --img-size 960 --conf-thres 0.25 --device 0
```

CPU 推理：

```bash
python detect.py --weights weights/best.pt --source test_images/JPEGImages --device cpu
```

结果默认保存到 `runs/detect/exp/`。使用 `--save-txt` 可以同时保存 YOLO 格式标签。

## 数据转换

将原始 VOC XML 数据放到：

```text
data/images/PV-Multi-Defect/
├── Annotations/
└── JPEGImages/
```

执行：

```bash
python data/convert_pv.py
```

转换脚本会生成 `datasets/pv_data/` 下的 YOLO 格式训练和验证目录。

## 模型与数据获取

- 测试图片和训练权重可通过邮件申请获取。
- 训练权重约 54.56 MB。
- 原始数据集来自 CCNUZFW 的 `PV-Multi-Defect` 数据集，学术使用时请引用 GBH-YOLOv5 论文和原始数据来源。
- 代码基于 Ultralytics YOLOv5 v5.0 修改，按 GPL-3.0 发布；第三方说明见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。

## License

本仓库代码按 GNU General Public License v3.0 发布。数据集和模型权重可能适用单独的授权条款，未随仓库分发。
