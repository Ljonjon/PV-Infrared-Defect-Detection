# Third-party notices

## Ultralytics YOLOv5

This repository contains a modified copy of Ultralytics YOLOv5 v5.0 code (`f5b8f7d54c9fa69210da0177fec7ac2d9e4a627c`) used for inference and deployment.

- Upstream project: https://github.com/ultralytics/yolov5
- License: GNU General Public License v3.0
- Local modifications include:
  - `torch.load(..., weights_only=False)` compatibility for modern PyTorch checkpoints.
  - NumPy compatibility fixes for deprecated integer types.
  - PV-specific inference defaults and model configuration.
  - Removal of unused experimental modules and unrelated sample configuration files.

The full GPL-3.0 license text is included in `LICENSE`.

## GBH-YOLOv5

The detector configuration is based on the GBH-YOLOv5 architecture: Ghost convolution, BottleneckCSP blocks, and an additional tiny-target prediction head.

Citation:

```bibtex
@article{Li2023GBHYOLOv5,
  title   = {GBH-YOLOv5: Ghost Convolution with BottleneckCSP and Tiny Target Prediction Head Incorporating YOLOv5 for PV Panel Defect Detection},
  author  = {Li, Longlong and Wang, Zhifeng and Zhang, Tingting},
  journal = {Electronics},
  volume  = {12},
  number  = {3},
  pages   = {561},
  year    = {2023},
  doi     = {10.3390/electronics12030561}
}
```

## PV-Multi-Defect dataset

The original dataset is maintained by the CCNUZFW research group:

- Repository: https://github.com/CCNUZFW/PV-Multi-Defect
- Paper DOI: https://doi.org/10.3390/electronics12030561
- Classes: `scratch`, `hot_spot`, `broken`, `black_border`, `no_electricity`

The dataset is not included in this repository. The exact test package used for this delivery is available by email request and may be subject to separate research-use terms.
