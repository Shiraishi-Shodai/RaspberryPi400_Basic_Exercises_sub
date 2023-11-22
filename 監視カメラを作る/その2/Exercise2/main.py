import cv2
import glob
import os

def get_f_names(dir_path, ext_list)-> list:
    '''
    指定したディレクトリパスと拡張子のリストから存在するファイル名を全て取得する(拡張子は含まない)
    
    :param dir_path: 検索するディレクトリパス
    :param ext_list: 検索する拡張子のリスト
    :type str, list
    
    :return: f_name_list: 検索結果のファイル名リスト
    :rtype: list
    
    '''
    f_name_list = []
    for ext in ext_list:
        # dir_pathで指定したパスに一致するファイルを取得
        path = dir_path + "*" + ext
        file_paths = glob.glob(path)
        for f_path in file_paths:
            f_name = os.path.basename(f_path).split('.', 1)[0]
            # file_listに一致するファイルパスを追加
            f_name_list.append(f_name)        

    return f_name_list


def get_new_f_name(f_name_list):
    '''
    新しいファイル名を生成し返却
    
    :param: f_name_list: 既存のファイル名リスト
    :type: list
    :return: f_name: 3桁で0埋めした新しいファイル名
    :rtype: str
    '''
    if len(f_name_list) == 0:
        f_name = '{0:03}'.format(1)
    else:
        try:
            f_name_list.sort()
            n = int(f_name_list[-1]) + 1
            f_name = '{0:03}'.format(n)
        except ValueError as e:
            print(e)

    return f_name + ".jpg"

def main():
    
    camera = cv2.VideoCapture(0)
    ret, frame = camera.read()
    
    if ret:
        
        dir_path = "/home/pi/python/RaspberryPi400_Basic_Exercises/監視カメラを作る/その2/Exercise2/"
        f_name_list = get_f_names(dir_path, [".jpg"])
        f_name = get_new_f_name(f_name_list)
        cv2.imwrite(dir_path + f_name, frame)

    camera.release()

if __name__ == "__main__":
    main()