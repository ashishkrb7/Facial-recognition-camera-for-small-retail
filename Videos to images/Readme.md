# Python package to extract the images from the videos

## Directory architecture
```
C:.
│   License
│   Readme.md
│   requirements.txt
│   Videos2Images.py
│
└───SourceDump

```
- SourceDump        : Put your videos here
- requirements.txt  : Requirements for python module
## Command to run 
*For help use*
```
python Videos2Images.py -h
```
*Example*
```
python Videos2Images.py --filename Untitled.mp4 --fps 0.5 --imageExt .jpg --OutputName frame
```