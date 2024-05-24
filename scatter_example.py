import pyecharts.options as opts
from pyecharts.charts import Scatter

"""
Gallery 使用 pyecharts 1.1.0
参考地址: https://echarts.apache.org/examples/editor.html?c=scatter-simple

目前无法实现的功能:

1、暂无
"""

data = [
    ["攻壳机动队 S.A.C. 2nd GIG", 9.2, 50],
    ["攻壳机动队 S.A.C. 1st GIG", 9.1, 45],
    ["某动画", 8.5, 60],
    ["另一动画", 8.7, 52]
]
# data.sort(key=lambda x: x[2])
x_data = [d[2] for d in data]
y_data = [d[1] for d in data]

(
    Scatter()
    .add_xaxis(xaxis_data=x_data)
    .add_yaxis(
        series_name="",
        y_axis=y_data,
        symbol_size=20,
        label_opts=opts.LabelOpts(is_show=False),
    )
    .set_series_opts()
    .set_global_opts(
        xaxis_opts=opts.AxisOpts(
            type_="value", splitline_opts=opts.SplitLineOpts(is_show=True)
        ),
        yaxis_opts=opts.AxisOpts(
            type_="value",
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
        tooltip_opts=opts.TooltipOpts(is_show=False),
    )
    .render("basic_scatter_chart.html")
)
