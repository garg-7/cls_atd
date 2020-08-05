from numpy import dot, arccos, pi
from numpy.linalg import norm
import json
import numpy as np
import os

ans = []
info = {}

sim = dict()  # dictionary that stores:

test_faces = list()  # list of all the test faces

test_data_list = open('list.txt', 'r')  # open the file that has the list of test images

for test_img_name in test_data_list:
    test_img_name = test_img_name.replace('.jpg\n',
                                          '.feat')  # the feature file would have a different extension so change it

    test_faces.append(test_img_name.replace('.feat', ''))  # append the filename of the test face

    temp = list()  # temporary list to store the various (ref_face, similarity) pairs for each test_face

    test_feat_file = open('save_path/' + test_img_name, 'rb')  # opening the feature file of the test face

    test_feat = np.fromfile(test_feat_file, dtype='<f', count=-1)  # loading the features of the test img

    maxsim = 0  # storing the maximum similarity
    maxsim_name = 'NULL'  # the reference img with which max similarity occurs

    ref_faces_list = open('liststd.txt', 'r')
    for ref_img_name in ref_faces_list:

        ref_img_name = ref_img_name.replace('.jpg\n',
                                            '.feat')  # the feature file would have a different extension so change it

        ref_feat_file = open('save_path/standard_features/' + ref_img_name,
                             'rb')  # opening the feature file of the ref face

        ref_feat = np.fromfile(ref_feat_file, dtype='<f', count=-1)  # loading the features of the ref img

        cos_sim = 1 - arccos(dot(test_feat, ref_feat)/(norm(test_feat)*norm(ref_feat)))/pi

        temp.append((ref_img_name.replace('.feat', ''), float(cos_sim)))

        if cos_sim > maxsim:
            maxsim = cos_sim
            maxsim_name = ref_img_name

    ref_faces_list.close()

    sim[test_img_name.replace('.feat', '')] = temp
    print(test_img_name.replace('.feat', '') + " - " + maxsim_name.replace('f.feat', '') + "| Score :", maxsim)
    if float(maxsim) > 0.62:
        ans.append({
            "roll_no": maxsim_name.replace('f.feat', ''),
            "attendance": 'Present',
            "score": str(maxsim),
            "ref_img": 'http://localhost:8000/static/reference/{}.jpg'.format(maxsim_name.replace('f.feat', '')),
            "ext_img": 'http://localhost:8000/static/extracted/{}.jpg'.format(test_img_name.replace('.feat', ''))
        })

    info[test_img_name.replace('.feat', '')] = [maxsim_name.replace('f.feat', ''), float(maxsim)]
    with open('scores.json', 'w') as handle:
        json.dump(sim, handle)

with open('attendance.json', 'w', encoding='utf-8') as f:
    json.dump(ans, f, ensure_ascii=False, indent=4)


dir_path = os.path.dirname(os.path.realpath(__file__))
t = dir_path.rsplit('/', 1)[0]
os.chdir(t)
with open('info.json', 'w', encoding='utf-8') as f:
    json.dump(info, f, ensure_ascii=False, indent=4)

