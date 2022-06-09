# FER-SCN-FER2013
## Usage
**Step 1. Install libraries**
```
conda env create -f environment.yml
```
**Step 2. Download all processed fer2013 files from this link**
```
https://1drv.ms/u/s!AmeTT2EpSz40kx2V9egbfDXJhGb3?e=ymCADi
```
**The original dataset can be found from this link**
```
https://www.kaggle.com/competitions/challenges-in-representation-learning-facial-expression-recognition-challenge/data
```
**Step 3. Put the processed all fer2013 files in the main folder**

**Step 4. Download pre-trained models from this link**
```
https://1drv.ms/u/s!AmeTT2EpSz40hFdT1nRCWPBzQQ-x?e=zHZITm
```
**Step 5. Put the pre-trained models in the following folder**
```
model_save
```
**To train the model from scratch, run the following**
```
bash train.sh
```
**After training the new model will be saved at the model_save folder and the results will be saved at the results folder**

**For evaluation, edit the test.sh file to use the model you want and run the following**
```
bash test.sh
```
**After running the above, the results will be saved at the main folder**

**In order to check the accuracy and the confusion matrix open the following jupyter notebook**
```
data_comparison.ipynb
```
**You may need to edit one line of code on the in the above notebook that is mark by a comment**
