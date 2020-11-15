""" 
    Python code to convert .xml to .csv    
    Developed by: Ashish Kumar @ Ranchi, Jharkhand
    Instruction : Please read README.md before using this file
"""

# Import libraries
import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET
import argparse

# Function
def main(path, name):
    path = path + name
    """ .xml to .csv converter """
    xml_list = []
    for xml_file in glob.glob(path + "/*.xml"):
        tree, root = ET.parse(xml_file), tree.getroot()
        for member in root.findall("object"):
            value = (
                root.find("filename").text,
                int(root.find("size")[0].text),
                int(root.find("size")[1].text),
                member[0].text,
                int(member[4][0].text),
                int(member[4][1].text),
                int(member[4][2].text),
                int(member[4][3].text),
            )
            xml_list.append(value)
    xml_df = pd.DataFrame(
        xml_list,
        columns=[
            "filename",
            "width",
            "height",
            "class",
            "xmin",
            "ymin",
            "xmax",
            "ymax",
        ],
    )
    xml_df.to_csv("test_labels.csv", index=None)
    print("Mission accomplished")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-p",
        "--path",
        type=str,
        help="Path of the folder with dataset",
        default=os.getcwd(),
    )
    parser.add_argument(
        "-n", "--name", type=str, help="Name of the folder", default="train"
    )
    args = parser.parse_args()
    main(path=args.path, name=args.name)
