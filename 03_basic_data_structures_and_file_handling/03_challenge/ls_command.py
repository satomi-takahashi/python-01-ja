import os
import shutil

def ls_command(directory):
    files_by_extension = {}

    # 指定されたディレクトリのファイルを探す
    for file_name in os.listdir(directory):
        if os.path.isfile(os.path.join(directory,file_name)):

            # ファイルの拡張子を取得
            _, extension = os.path.splitext(file_name) 
            extension = extension [1:]

            # 拡張子に基づいて各ファイルをフォルダにまとめる
            if extension in files_by_extension:
                files_by_extension[extension].append(file_name)
            else:
                files_by_extension[extension] = [file_name]

    # 拡張子に対応するフォルダを作成し、ファイルを移動する
<<<<<<< HEAD
    for extention, files in files_by_extension.items():
=======
    for extension, files in files_by_extension.items():
>>>>>>> 90357c0f2a5d876184b51f14c8568185b81a8a13
        folder_path = os.path.join(directory, extension)

    # フォルダが存在しない場合は作成する    
        os.makedirs(folder_path, exist_ok=True)  

        for file in files:
            source_path = os.path.join(directory, file)
            destination_path = os.path.join(folder_path, file)
            shutil.move(source_path, destination_path)

    # 各フォルダのファイル数を表示
    for extension, files in files_by_extension.items():
<<<<<<< HEAD
        print(f"{extension}：{len(files)}")
        
=======
        print(f"拡張子'{extension}'のファイル数：{len(files)}")
              
>>>>>>> 90357c0f2a5d876184b51f14c8568185b81a8a13
    return files_by_extension

if __name__ == "__main__":
    directory_path = input("Enter directory path to organize files: ")

    if not os.path.isdir(directory_path):
        print("Invalid directory path.")
    else:
        ls_command(directory_path)
