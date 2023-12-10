#### Load Libraries ####
from Application_Functions import play, isAnswer, playAnswer, financialAnalysis, loadData, changePeriod, plotPriceSeries, plotReturnSeries, plotNetworkStatSeries, buildTree
import os
import subprocess
import json

# read the tree from a json file
with open('../json_files/crypto_tree.json') as json_file:
    cryptoTree = json.load(json_file)

#### Create Main Function ####
def main():
    if len(os.listdir("../json_files")) != 0:

        reload = input("Do you want to run the Data_Collector.py script to generate the JSON files? (Type 'R' to Reload or press 'Enter')")

        if reload == "R":
            print("Running Data_Collector.py script...")
            print("\n")
            print("NORun the Data_Collector.py script to generate the JSON files.")
            print("Running Data_Collector.py script...")
            subprocess.run(["python", "Data_Collector.py"])
        elif reload == "":
            print("Proceeding to the next step...")
    else:
        print("\n")
        print("JSON files are present in the directory. Proceeding to the next step.")
    print("----------------------------------------------------------")
    print("Welcome to the Crypto Recomenndation App")
    print("Let's Find a Cryptocurrency for you to analyze!")
    play(cryptoTree)

if __name__ == '__main__':
    main()
