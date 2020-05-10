import os
import json
import numpy as np

def get_list(epath):
#f1 = open(os.path.join(epath,'list.txt'),'w')
    file_dict = dict()
    for root, dirs, files in os.walk(epath):
        for filename in files:
            ftmp = open(os.path.join(epath,filename),'r')
            val = json.load(ftmp)
            file_dict[filename.replace('.json','')]=np.array(val[0])
            #f1.write(filename+os.linesep)
    return file_dict


def get_scores(stdpath, testpath):
    std_dict = get_list(os.path.join(os.path.abspath(os.path.dirname(__file__)),stdpath))
    test_dict = get_list(os.path.join(os.path.abspath(os.path.dirname(__file__)),testpath))
    results = dict()
    for test in test_dict:
        x1 = test_dict[test]
        temp = list()
        maxsim = 0
        maxname = 'NONE'
        for std in std_dict:
            x2 = std_dict[std]
            cosine = abs(np.dot(x1, x2)/ (np.linalg.norm(x1) * np.linalg.norm(x2)))
            temp.append((std,float(cosine)))
            if cosine > maxsim:
                maxsim = cosine
                maxname = std
        temp = sorted(temp,key = lambda x: x[1],reverse=True)
        results[test] = temp
    
    with open('scores.json', 'w') as handle:
        json.dump(results, handle)
      


if __name__ == "__main__":
    stdpath = 'save_path/standard_features/'
    testpath = 'save_path/'
    get_scores(stdpath, testpath)