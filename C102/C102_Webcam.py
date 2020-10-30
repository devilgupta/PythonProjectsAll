import cv2.cv as cv
import cv2,cv
import dropbox
import time
import random

start_time=time.time()

def take_snapshot():
    number=random.randint(0,100)
    videoCaptueObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame = videoCaptureObject.read()
        cv2.imwrite("new picture 1.jpg",frame)
        result=False
    
    videoCaptueObject.release()
    cv2.destroyAllWindows()

def upload_files(img,name):
    access_token="sl.Aiaid9ghHqK27B07Y5LswliapcuvgOucjDCjzYnWggJhxBYShWvcXb_A-DcL0P6rU5up71n9l9qplMYiFLjUUONrH1VeAw20qCsuGuiJgGTaec3WYsZuACX9vSodjDbuxtFMl3g"
    file=img_counter
    file_from=file
    file_to = "/newfolder1/"+(img_name)
    dbx=dropbox.Dropbox(access_token)

    with open(file_from,'rb')as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)

def main():
    while(True):
        if((time.time()-start_time)>=300):
            name=take_snapshot()
            upload_files(name)
main()
