from Application_Functions import buildTree
from cryptocurrency import crypto_dict, questions
import json
import os

cryptoTree = buildTree(crypto_dict, questions)

os.chdir("../json_files")

# save the tree to a json file
with open('crypto_tree.json', 'w') as outfile:
    json.dump(cryptoTree, outfile)
    # print the tree
    print(json.dumps(cryptoTree, indent=4))