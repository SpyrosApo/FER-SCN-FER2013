python -u test.py --gpu_ids 0 --test_image_path ./test_images.txt --test_path ./test_ \
       --model_path ./model_save/my_resnet18.pth \
       2>&1 |tee ./log.txt
