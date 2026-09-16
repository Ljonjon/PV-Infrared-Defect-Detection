# Model weights

`best.pt` is the trained PV infrared defect detector used by this delivery. It is intentionally not committed to Git because dataset-model transfer is handled separately.

To request the model, email **ljonjon540122@gmail.com**.

Please use this subject line:

```text
[PV Defect] Request test dataset and inference model
```

After receiving the file, place it at:

```text
weights/best.pt
```

Then run:

```bash
python detect.py --weights weights/best.pt --source test_images/JPEGImages
```
