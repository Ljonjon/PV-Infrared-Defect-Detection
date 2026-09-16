# Data preparation

The original PV-Multi-Defect dataset is maintained by the CCNUZFW research group and is not redistributed in this repository. The test image package and the trained model used by this delivery are available by email request.

To prepare a local training/validation layout, place the received raw dataset as:

```text
data/images/PV-Multi-Defect/
├── Annotations/
└── JPEGImages/
```

Then run:

```bash
python data/convert_pv.py
```

The converter writes a YOLO-format dataset to `datasets/pv_data/` and updates `data/pv_thermal.yaml`.

Expected class order:

1. `scratch`
2. `hot_spot`
3. `broken`
4. `black_border`
5. `no_electricity`
