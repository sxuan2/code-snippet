import os
import pandas as pd
import shutil

main_path = r'I:\carRecording'
output_path = r'I:\carRecording_output'
file_ls = os.listdir(main_path)
file_ls_pd = pd.DataFrame(file_ls)


file_name_ls = file_ls_pd[0].str.split('-').str[0].str[4:].unique().tolist()

for path in file_name_ls:
    print(path)
    isExist = os.path.exists(os.path.join(output_path,path))
    if not isExist:
        os.mkdir(os.path.join(output_path,path))
        for file in file_ls:
            if file[4:10] == path:
                shutil.move(os.path.join(main_path,file),os.path.join(output_path,path,file))
    else:
        for file in file_ls:
            if file[4:10] == path:
                shutil.move(os.path.join(main_path,file),os.path.join(output_path,path,file))
                