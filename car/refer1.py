import os

# 指定要创建文件夹的父文件夹路径
parent_folder = 'E:/refer1'  # 替换为实际的父文件夹路径

# 定义字符列表
characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
              'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
              'X', 'Y', 'Z',
              '藏', '川', '鄂', '甘', '赣', '贵', '桂', '黑', '沪', '吉', '冀', '津', '晋', '京', '辽', '鲁', '蒙', '闽',
              '宁',
              '青', '琼', '陕', '苏', '皖', '湘', '新', '渝', '豫', '粤', '云', '浙']

# 循环创建字符命名的文件夹
for character in characters:
    folder_path = os.path.join(parent_folder, character)
    os.makedirs(folder_path, exist_ok=True)
    print("Created folder:", folder_path)