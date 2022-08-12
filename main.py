import os
import shutil

current_folders_list = os.listdir('./')
folders_name = ['coding files', 'Exe Files', 'Exel and Csv', 'Folders', 'Gif', 'Images', 'MicrosoftFiles', 'PDF', 'Text', 'Videos', 'ZipFiles']
for i in folders_name:
    if i not in current_folders_list:
        os.mkdir(f'./{i}')

os.chdir('../')
dir_list = os.listdir('./')
    

image_extension = ['jpg', 'png', 'webp', 'jpeg', 'jfif', 'bmp']
code_extensions = ['py', 'ipynb', 'cpp', 'c', 'java', 'html', 'css', 'js', 'db']
for i in dir_list:
    try:
        if i.find('.') != -1:
            arr = i.split('.')
            extension = arr[-1]
            if extension in image_extension:
                os.replace(f'./{i}', f'./Organize Files/Images/{i}')
                continue

            if (extension == 'zip'):
                os.replace(f'./{i}', f'./Organize Files/ZipFiles/{i}')
                continue
            
            if (extension == 'pdf'):
                os.replace(f'./{i}', f'./Organize Files/PDF/{i}')
                continue

            if (extension == 'exe'):
                os.replace(f'./{i}', f'./Organize Files/Exe Files/{i}')
                continue
            
            if (extension == 'mp4') or (extension == 'mkv'):
                os.replace(f'./{i}', f'./Organize Files/Videos/{i}')
                continue

            if (extension == 'xlsx') or (extension == 'csv' or (extension == 'xls')):
                os.replace(f'./{i}', f'./Organize Files/Exel and Csv/{i}')
                continue

            if (extension == 'gif'):
                os.replace(f'./{i}', f'./Organize Files/Gif/{i}')
                continue
            
            if extension in code_extensions:
                os.replace(f'./{i}', f'./Organize Files/coding files/{i}')
                continue

            if (extension == 'txt'):
                os.replace(f'./{i}', f'./Organize Files/Text/{i}')
                continue

            if (extension == 'pptx') or (extension == 'docx') or (extension == 'ppt'):
                os.replace(f'./{i}', f'./Organize Files/Gif/{i}')
                continue

        else:
            if i != 'Organize Files':
                os.replace(f'./{i}', f'./Organize Files/Folders/{i}')

    except ValueError:
        print(f'Error occur at {i}')

