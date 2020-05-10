# Using ArcFace PyTorch Implementation
Following 3 steps are involved:

## 1. Listing files
- Make sure the faces to be tested are present in the ./data/ directory.
- Run get_list.py, which will create a list.txt in the current directory.
- This file will contain just the names of all the .jpg files present in the data folder.

## 2. Extracting features
- Run get_features.py.
- It will create .json files containing facial emebdding of all the .jpg files listed in list.txt.
- These .json files will be stored in the ./save_path/ directory.

## 3. Obtaining scores
(Assuming the reference images' feature (.json) files are already present in ./save_path/standard_features/ directory)
- Run get_scores.py.
- It reads any feature files present in the save_path/ dir. and compares it with all the feature files in the save_path/standard_features/ dir.
- It stores the results in a score.json file in the current directory.
- Scores.json contains a dictionary, which has values in the form of :
{
  test_1 : [roll_no1, scorewithrollno1], [rolln_no2, scorewithrollno2] ...
  test_2 : ...
  .
  .
}

The scores listed above will be in descending order i.e. the Roll No. that matches the most against a test file is listed first.
