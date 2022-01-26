from pdf2image import convert_from_path
from pdf2image.exceptions import (
 PDFInfoNotInstalledError,
 PDFPageCountError,
 PDFSyntaxError
)
from PIL import Image
from pytesseract import pytesseract
from os import path
from gtts import gTTS
import os


def pdf_to_image(bookfile,foldername):
    folder = foldername
    os.makedirs(folder, exist_ok=True)
    images = convert_from_path(bookfile)
    for i, image in enumerate(images):
        fname = 'image'+str(i)+'.png'
        completeName = os.path.join(folder, fname)         
        image.save(completeName, "PNG")
    return folder

def get_text_from_im(folder):
    path_to_tesseract = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
    condition = True
    i = 0
    while condition:
        from os import path
        if path.exists(f"{folder}\image{i}.png"):
            try:
                image_path = f"{folder}\image{i}.png"
                img = Image.open(image_path)
                pytesseract.tesseract_cmd = path_to_tesseract
                text = pytesseract.image_to_string(img)
                text_to_speech(text,i, folder)
            except:

                folder_name = f'{folder}\sound'.format(folder)
                fname = f"sound{i}.mp3"
                completeName = os.path.join(folder_name, fname)  
                path = r"my/path/to/file.txt"
                assert os.path.isfile(completeName)
                with open(completeName, 'w') as fp:
                    pass
                print(f"save {folder}\sound\sound{i}.mp3".format(folder))
        else:
            condition = False
        i+=1
    return text

def text_to_speech(text, i, folder):
    folder_name = f'{folder}\sound'.format(folder)
    os.makedirs(folder_name, exist_ok=True)
    language = 'en'
    myobj = gTTS(text=text, lang=language, slow=False)
    fname = f"sound{i}.mp3"
    completeName = os.path.join(folder_name, fname)  
    myobj.save(completeName)
    print(f"save {folder}\sound\sound{i}.mp3".format(folder))        
    return
