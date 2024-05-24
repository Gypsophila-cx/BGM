from pyecharts.charts import Scatter
import pyecharts.options as opts
from pyecharts.commons.utils import JsCode

data = [
    ["攻壳机动队 S.A.C. 2nd GIG", 9.2, 50],
    ["攻壳机动队 S.A.C. 1st GIG", 9.1, 45],
    ["某动画", 8.5, 60],
    ["另一动画", 8.7, 52]
]
x_data = [d[2] for d in data]
y_data = [d[1] for d in data]
names = [d[0] for d in data]

(
    Scatter()
    .add_xaxis(xaxis_data=x_data)
    .add_yaxis(
        series_name="",
        y_axis=[list(z) for z in zip(y_data, names)],
        symbol_size=10,
        label_opts=opts.LabelOpts(is_show=False),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="评分人数 vs 分数"),
        xaxis_opts=opts.AxisOpts(
            type_="value", 
            splitline_opts=opts.SplitLineOpts(is_show=True),
            min_ = 'dataMin',
        ),
        yaxis_opts=opts.AxisOpts(
            type_="value",
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
        datazoom_opts=opts.DataZoomOpts(
            is_show=True,
            range_start = 0,
            range_end = 100,
        ),
        tooltip_opts=opts.TooltipOpts(
            is_show=True,
            formatter=JsCode(
            "function (params) {return params.value[2];}"
            ),
        ),
    )
    .render()
)