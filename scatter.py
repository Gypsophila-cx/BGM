from pyecharts.charts import Scatter

data = [
    ["攻壳机动队 S.A.C. 2nd GIG", 9.2, 50],
    ["攻壳机动队 S.A.C. 1st GIG", 9.1, 45],
    ["某动画", 8.5, 60],
    ["另一动画", 8.7, 52]
]

print([type(row[1]) for row in data])

scatter = Scatter()
scatter.add_xaxis([row[2] for row in data])
scatter.add_yaxis("Grade", [row[1] for row in data])
# render 会生成本地 HTML 文件，默认会在当前目录生成 render.html 文件
# 也可以传入路径参数，如 bar.render("mycharts.html")
scatter.render()