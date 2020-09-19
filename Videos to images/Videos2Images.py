'''
Python code to extract the images from videos based on custom fps

'''
print(__doc__)
# Importing all necessary libraries 
import cv2 
import os 
import argparse

def run(filename,fps,imageExt,OutputName):
    '''Main function to run the program'''
    inputIMG = cv2.VideoCapture(f"{path}/SourceDump/{filename}") # Read the video from specified path 
    if not os.path.exists('OutputDump'): os.makedirs('OutputDump') # creating a folder named data 

    def getFrame(sec,imageExt,count):
        ''' Function to create the images from videos'''
        inputIMG.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
        # Reading from frame 
        ret,frame = inputIMG.read()
        if ret: 
            name = f'{path}/OutputDump/{OutputName}' + str(count) + imageExt
            print ('Creating...' + name) 
            cv2.imwrite(name, frame) 
        return ret

    sec = 0
    count=1
    success = getFrame(sec,imageExt,count)
    print(success)
    while success:
        count = count + 1
        sec = sec + fps
        sec = round(sec, 2)
        success = getFrame(sec,imageExt,count)

    inputIMG.release() 
    cv2.destroyAllWindows() 

  
if __name__=="__main__":

    path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".")).replace("\\", "/") # To get current working path

    # run('Untitled.mp4',0.5,'.jpg','frame')

    parser=argparse.ArgumentParser()
    
    parser.add_argument("--filename",type=str,help='File name of the input video')
    parser.add_argument("--fps",type=float,default=0.5,help='Frame per second, Default=0.5')
    parser.add_argument("--imageExt",type=str,default='.jpg',help='Output file extension, Default=".jpg"')
    parser.add_argument("--OutputName",type=str,default='frame',help='Output file name, Default="frame"')
    args=parser.parse_args()
    run(
        filename=args.filename,
        fps=args.fps,
        imageExt=args.imageExt,
        OutputName=args.OutputName,
    )
