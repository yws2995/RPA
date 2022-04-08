# 파일 기본
import os
# print(os.getcwd()) # current working directory
# os.chdir("..")
# print(os.getcwd()) # current working directory
# os.chdir("../..") # 조부모 폴더로 이동
# print(os.getcwd()) # current working directory
# os.chdir("c:/") # 주어진 절대 경로로 이동
# print(os.getcwd()) # current working directory

# 파일 경로를 만드는 작업
file_path = print(os.path.join(os.getcwd(), "my_file.txt"))

# print(os.path.join(os.getcwd(), "my_file.txt")) # 절대 경로 생성
# print(file_path)

# 파일 경로에서 폴더 정보 가져오기 
# print(os.path.dirname(r"C:\Users\yws29\OneDrive\Desktop\PythonWorkspace\my_file.txt ")) # r은 백슬래쉬무시

# # 파일 정보 가져오기 
# import time
# import datetime

# #파일의 생성 날짜
# file_path_2 = "rpa_basic/2_desktop/11_file_system.py"
# ctime=os.path.getctime("file_menu.png")
# print(ctime)
# # 날짜 정보를 strftime을 통해서 출력
# print(datetime.datetime.fromtimestamp(ctime).strftime( "%Y%m%d %H%M%S"))

# # 파일의 수정 날짜
# mtime = os.path.getmtime("file_menu.png")
# print(datetime.datetime.fromtimestamp(mtime).strftime( "%Y%m%d %H%M%S"))

# # 파일의 마지막 접근 날짜
# atime = os.path.getatime("file_menu.png")
# print(datetime.datetime.fromtimestamp(atime).strftime( "%Y%m%d %H%M%S"))

# # 파일 크기
# size = os.path.getsize(file_path_2)
# print(size) #파일 크기를 바이트 단위로


# 파일 목록 가져오기
# print(os.listdir()) # 작업공간 아래에 있는 모든 폴더와 파일을 보여준다.
# print(os.listdir("rpa_basic")) # 주어진 폴더 아래에서 모든 폴더와 파일 목록을 가져옴

# 파일 목록 가져오기( 하위 폴더 모두 포함 )
result = os.walk("rpa_basic") # 주어진 폴더 밑에 있는 모든 폴더, 파일 목록 가져오기
# print(result)

# for root, dirs, files in result:
#     print(root, dirs, files)

# # 만약 폴더 내에서 특정 파일들을 찾으려면?
# name = "11_file_system.py"
# result = []
# for root, dirs, files in os.walk("."):
#     # [a.txt, b.txt, c.txt,..., 11_file_system.py]
#     if name in files:
#         result.append(os.path.join(root,name))

# print(result)

# ".xlsx", "txt", 자동화*.png" 
#  폴더 내에서 특정 패턴을 가진 파일들을 찾으려면?
# import fnmatch
# pattern = "*.py" #.py로 끝나는 모든 파일
# result = []
# for root, dirs, files in os.walk("."):
#     #     # [a.txt, b.txt, c.txt,..., 11_file_system.py]
#     for name in files:
#         if fnmatch.fnmatch(name, pattern): # 이름과 패턴이 일치하면
#             result.append(os.path.join(root, name))

# print(result)

# # 주어진 경로가 파일인지? 폴더인지?
# print(os.path.isdir("rpa_basic")) # rpa_basic은 폴더인가? -> True
# print(os.path.isfile("rpa_basic")) # rpa_basic은 폴더인가? -> False

# print(os.path.isdir("file_menu.png"))
# print(os.path.isfile("file_menu.png"))

# # 만약에 지정된 경로에 해당하는 파일/ 폴더가  없다면? 
# print(os.path.isfile("file_menuㅕuuu.png")) #False 반환

# 주어진 경로가 존재하는지?
# if os.path.exists("rpa_basic"):
#     print("파일 또는 폴더가 존재합니다.")
# else:
#     print("존재하지 않습니다.")

# 파일 만들기 
# open("new_file.txt", "a").close() # 빈 파일 생성

# 파일명 변경하기 
# os.rename("new_file.txt", "new_file_rename.txt") # new_file.txt -> new_file_rename.txt

# 파일 삭제하기
# os.remove("new_file_rename.txt")

# 폴더 만들기
# os.mkdir("new_folder") # 현재 경로 기준으로 폴더 생성
# os.mkdir("c:/users...") # 절대 경로 기준으로 폴더 생성

# os.mkdir("new_folders/a/b/c") # 하위 폴더를 가지는 폴더 생성 시도 
# os.makedirs("new_folders/a/b/c") # 위가 아니라 아래처럼 만들어야 여러개가 만들어진다. 

# 폴더명 변경하기 
# os.rename("new_folder", "new_folder_rename")

# 폴더 지우기
# os.rmdir("new_folders_rename") # rmdir은 폴더 안이 비어있을 경우에만 삭제할 수 있다. 

import shutil #shell utilites
# shutil.rmtree("new_folders") # 폴더 안이 비어있지 않아도 완전 삭제 가능
# 모든 파일이 삭제될 수 있음으로 주의!!!

# 파일 복사하기 
# 어떤 파일을 폴더 안으로 복사하기
# shutil.copy("file_menu.png", "test_folder") #원본 경로, 대상 경로
# 어떤 파일을 폴더 안에 새로운 파일 이름으로 복사하기 
# shutil.copy("file_menu.png", "test_folder/copied_file_menu.png") #원본 경로, 대상 경로

# shutil.copyfile("file_menu.png", "test_folder/copied_file_menu_2.png") # 원본 파일 경로, 대상 파일 경로
# shutil.copy2("file_menu.png", "test_foleder/copied2_file_menu.png") # 원본 파일 경로, 대상 폴더(파일 경로)

# copy, copyfile : 메타정보 복사x
# copy2 : 메타정보 복사 O

# 폴더 복사
# shutil.copytree("test_folder", "test_folder2") # 원본 폴더 경로, 대상 폴더 경로
# shutil.copytree("test_folder", "test_folder3")

# 폴더 이동 
# shutil.move("test_folder", "test_folder3")
# shutil.move("test_folder2", "test_folder3")
# shutil.move("test_folder3", "test_folder_rename") # 폴더명 변경 효과





