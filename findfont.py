import matplotlib.font_manager as fm

# 获取系统中所有字体
font_list = fm.findSystemFonts(fontpaths=None, fontext='ttf')

# 打印所有字体路径
for font in font_list:
    print(font)

# 检查特定的中文字体是否存在
chinese_fonts = [f for f in font_list if 'SimHei' in f or 'simsun' in f or 'NotoSansCJK' in f or 'msyh' in f]
print("Available Chinese fonts:")
for font in chinese_fonts:
    print(font)
