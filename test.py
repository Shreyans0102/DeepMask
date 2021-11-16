import torch
import sys
import cv2
import numpy as np
import copy
import os
sys.path.append(r'C:\Users\shrey\hackUmass\FaceMaskDetection\models')

model_path = r"C:\Users\shrey\hackUmass\FaceMaskDetection\models\model360.pth"
img_path = r"C:\Users\shrey\hackUmass\imgs\WIN_20211106_17_01_17_Pro.jpg"

model = torch.load(model_path)
model.eval()

for i in os.listdir(r"C:\Users\shrey\Downloads\Compressed\data\images"):
    img_path = os.path.join(r"C:\Users\shrey\Downloads\Compressed\data\images", i)
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    height, width, _ = img.shape
    image_resized = cv2.resize(img, (360,360))
    image_np = image_resized / 255.0  # 归一化到0~1
    image_exp = np.expand_dims(image_np, axis=0)
    image_transposed = image_exp.transpose((0, 3, 1, 2))
    input_img = torch.tensor(image_transposed).float()
    a,b = model.forward(input_img)
    a = a.detach()
    b = b.detach()
    print(a.shape)
    print('____________________')
    print(b.shape)
    print('____________________')


