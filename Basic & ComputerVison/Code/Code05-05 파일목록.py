import os

file_address = 'C:/images/'

# 해당 폴더에서 원하는 확장자만 불러오기
for dir_name, sub_dir_list, file_names in os.walk(file_address):
    for file_name in file_names:
        if os.path.splitext(file_name)[1].upper() == '.GIF' :
            print(os.path.join(dir_name,file_name))
    # C:/images/Pet_GIF\Pet_GIF(128x128)\cat01_128.gif      
    # C:/images/Pet_GIF\Pet_GIF(128x128)\cat02_128.gif      
    # C:/images/Pet_GIF\Pet_GIF(128x128)\cat03_128.gif      
    # C:/images/Pet_GIF\Pet_GIF(128x128)\cat04_128.gif
    # ...

for dir_name, sub_dir_list, file_names in os.walk(file_address):
    print(dir_name)
    # 파일 내부에 모든 폴더 주소를 보여줌
    # C:/images/
    # C:/images/csv
    # C:/images/CSV&XLS
    # C:/images/image(BigSize)
    # C:/images/image(BigSize)\image(BigSize)   
    # ...

for dir_name, sub_dir_list, file_names in os.walk(file_address):
    print(sub_dir_list)
    # 폴더 내부의 폴더들의 주소들을 리스트로 반환, 폴더 내부의 폴더가 존재하지 않을경우 빈 리스트([])로 반환
    # ['csv', 'CSV&XLS', 'image(BigSize)', 'images(ML)', 'Pet_GIF', 'Pet_PNG', 'Pet_RAW']
    # []
    # []
    # []
    # ['image(BigSize)']
    # []
    # ...
    
for dir_name, sub_dir_list, file_names in os.walk(file_address):
    print(file_names)
    # 폴더 내부의 모든 파일들의 이름을 리스트로 반환
    # ['CSV&XLS.zip', 'csv.zip', 'image(BigSize).zip', 'images(ML).zip', 'Pet_GIF.zip', 'Pet_PNG.zip', 'Pet_RAW.zip', '붓꽃.csv']
    # ...
