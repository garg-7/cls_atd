from numpy import dot
from numpy.linalg import norm
import json
import numpy as np

sim = dict()    # dictionary that stores:
                # {
                #   test_face1:[(ref_face1, similarity_with_it),(ref_face2, similarity_with_it)...],
                #   test_face2:[(ref_face1, similarity_with_it),(ref_face2, similarity_with_it)...] 
                # }
test_faces = list()  # list of all the test faces

test_data_list = open('list.txt','r') # open the file that has the list of test images

for test_img_name in test_data_list:
    test_img_name = test_img_name.replace('.jpg\n', '.feat')    # the feature file would have a different extension so change it
    
    test_faces.append(test_img_name.replace('.feat','')) # append the filename of the test face

    temp = list()       #   temporary list to store the various (ref_face, similarity) pairs for each test_face

    test_feat_file = open('save_path/' + test_img_name, 'rb')   # opening the feature file of the test face
    
    test_feat = np.fromfile(test_feat_file, dtype = '<f', count = -1) #loading the features of the test img
    
    maxsim = 0      # storing the maximum similarity
    maxsim_name = 'NULL'    # the reference img with which max similarity occurs
    
    ref_faces_list = open('liststd.txt','r')
    for ref_img_name in ref_faces_list:

        ref_img_name = ref_img_name.replace('.jpg\n','.feat') # the feature file would have a different extension so change it
        
        ref_feat_file = open('save_path/standard_features/'+ ref_img_name,'rb') # opening the feature file of the ref face
        
        ref_feat = np.fromfile(ref_feat_file, dtype = '<f', count = -1)  # loading the features of the ref img
        
        cos_sim = abs(dot(test_feat, ref_feat) / (norm(test_feat) * norm(ref_feat)))
        
        temp.append((ref_img_name.replace('.feat',''),float(cos_sim)))
        
        if cos_sim > maxsim:
            maxsim = cos_sim
            maxsim_name = ref_img_name
    
    ref_faces_list.close()
    
    sim[test_img_name.replace('.feat','')] = temp
    print(test_img_name.replace('.feat','')+" - " + maxsim_name.replace('f.feat','') + "| Score :", maxsim)
    with open('scores.json', 'w') as handle:
        json.dump(sim, handle)

# print("\n\n----Normal execution ended----\n\n")


# x = input("Do you want the dictionary values?(y/n)")
# if x=='y':
#     for test_face in sim:
#         print(test_face+":")
#         sim[test_face].sort(key=lambda x: x[1],reverse = True)
#         for val in sim[test_face]:
#             print(val)
#         print()
# else :
#     print("Program ended.")
