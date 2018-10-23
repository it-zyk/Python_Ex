# coding=utf-8
import csv
import pygal_maps_world.maps as pmw
from pygal.style import RedBlueStyle as RB
from pygal_maps_world.i18n import COUNTRIES

# 指定CSV文件
file_name = 'API_SP.POP.65UP.TO.ZS_DS2_en_csv_v2.csv'


def get_country_code(country_name):
    """建立函数：根据指定国家，返回Pygal使用的两个字母的国别码"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code

    return None


with open(file_name) as f:
    # 加载CSV阅读器
    reader = csv.reader(f)

    # 先读取CSV数据中前五个没有数据的行
    for i in range(5):
        header = next(reader)

    # 建立空字典
    proportion_countries = {}

    for row in reader:
        # 第一列数据为国家名
        country = row[0]

        # 利用函数获取国家代码
        country_code = get_country_code(country)

        # 如果国家代码存在
        if country_code:

            # 读取存储于第60列（2016年）的数据，用try-except循环判断： 如果不为数字格式（或为空），则置为0
            try:
                # 转化为浮点格式，并保存两位小数
                proportion = round(float(row[60]), 2)

            except ValueError:
                proportion = 0

            # 将国家代码和人口比例依次写入字典中
            proportion_countries[country_code] = proportion

# 创建三个字典，将不同比例范围的数值写入三个字典中
dict_1, dict_2, dict_3 = {}, {}, {}
for name, value in proportion_countries.items():
    if value >= 15:
        dict_1[name] = value
    elif value >= 10:
        dict_2[name] = value
    else:
        dict_3[name] = value

# 初始化地图，设置颜色风格，添加标题
wm = pmw.World(style=RB)
wm.title = 'Proportion of 65+ population (2016)'

# 依次添加地图数据
wm.add('large than 15', dict_1)
wm.add('between 10 - 15', dict_2)
wm.add('smaller than 10', dict_3)

# 保存文件
wm.render_to_file('Proportion of 65+ population.svg')
