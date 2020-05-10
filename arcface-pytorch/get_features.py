import numpy as np
import torch
import cv2
from config.config import Config
from models.resnet import *
from torch.nn import DataParallel
import json


def get_features(model, test_list, batch_size=10):
    images = None
    features = None
    cnt = 0
    for i, img_path in enumerate(test_list):
        image = load_image(img_path)
        if image is None:
            print('read {} error'.format(img_path))

        if images is None:
            images = image
        else:
            images = np.concatenate((images, image), axis=0)

        if images.shape[0] % batch_size == 0 or i == len(test_list) - 1:
            cnt += 1

            data = torch.from_numpy(images)
            data = data.to(torch.device("cuda"))
            output = model(data)
            output = output.data.cpu().numpy()

            fe_1 = output[::2]
            fe_2 = output[1::2]
            feature = np.hstack((fe_1, fe_2))
            # print(feature.shape)

            if features is None:
                features = feature
            else:
                features = np.vstack((features, feature))

            images = None
            f1 = open('save_path/{}'.format(img_path.replace('data/','').replace('.jpg','.json')),'w')
            json.dump(feature.tolist(),f1)
    return features, cnt

def load_image(img_path):
    image = cv2.imread(img_path, 0)
    if image is None:
        return None
    image = cv2.resize(image, (128, 128))
    image = np.dstack((image, np.fliplr(image)))
    image = image.transpose((2, 0, 1))
    image = image[:, np.newaxis, :, :]
    image = image.astype(np.float32, copy=False)
    image -= 127.5
    image /= 127.5
    return image

def get_path_list(imgs_path):
    img_list = list()
    f = open(imgs_path, 'r')
    for names in f:
        img_list.append('data/'+names.replace("\n",''))
    return img_list


if __name__=='__main__':
    opt = Config()
    if opt.backbone == 'resnet18':
        model = resnet_face18(opt.use_se)
    elif opt.backbone == 'resnet34':
        model = resnet34()
    elif opt.backbone == 'resnet50':
        model = resnet50()
    model = DataParallel(model)
    # load_model(model, opt.test_model_path)
    model.load_state_dict(torch.load(opt.test_model_path))
    model.to(torch.device("cuda"))
    model.eval()
    img_list = get_path_list('list.txt')
    # print(img_list)
    feat, count = get_features(model, img_list, opt.test_batch_size)
    print("The count is",count)