import os
import random


def main():
    random.seed(0)  # 设置随机种子，保证随机结果可复现

    files_path = "./VOCdevkit/VOC2007/Annotations"  #遍历该路径下的文件
    # assert os.path.exists(files_path), "path: '{}' does not exist.".format(files_path)

    if not os.path.exists(files_path):
        print("文件夹不存在")
        exit(1)

    val_rate = 0.5  #验证集比例

    files_name = sorted([file.split(".")[0] for file in os.listdir(files_path)])    #排列分割出文件名称
    files_num = len(files_name)                                                     #拿到所有文件的数量
    val_index = random.sample(range(0, files_num), k=int(files_num*val_rate))       #随机采样，采样范围从0到files_num，采样个数为事先设定的训练集比例
    train_files = []                        #建立空列表存储训练集
    val_files = []                          #建立空列表存储确认集
    for index, file_name in enumerate(files_name):                                  #索引判断，在val_index里就放到val_file文件中，不在就放到train_file文件中
        if index in val_index:
            val_files.append(file_name)
        else:
            train_files.append(file_name)

    try:
        train_f = open("train.txt", "x")
        eval_f = open("val.txt", "x")
        train_f.write("\n".join(train_files))#换行符拼接列表内容>>>>>拼接成字符
        eval_f.write("\n".join(val_files))
    except FileExistsError as e:
        print(e)
        exit(1)


if __name__ == '__main__':
    main()
