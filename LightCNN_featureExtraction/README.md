## Implementing the LightCNN function::

1. Make sure the individual faces are in a folder called data.
2. Run the get_list.py script. It will create a list.txt file that is needed.
3. Run the extract_features.py file (without any arguments). It will store the .feat files according to the faces in the save_path folder.

## Cosine Similarity::

1. Just run the cossim.py script. It will dump a dictionary of scores into a scores.pickle file.
(The dictionary contains the comparison value with respect to each class.)
