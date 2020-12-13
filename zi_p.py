
import zipfile
import os

''' Zip files in folder news to testzip.zip  '''
def zipit():
    folder_to_be_zipped = 'output'

    with zipfile.ZipFile('webzip.zip', 'w', zipfile.ZIP_DEFLATED) as newzip:
        for dirpath, dirnames, files in os.walk(folder_to_be_zipped):
            for file in files:
                newzip.write(os.path.join(dirpath, file))
    


    
