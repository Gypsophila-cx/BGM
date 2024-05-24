from pyecharts.charts import Scatter
import pyecharts.options as opts
from pyecharts.commons.utils import JsCode
import pandas as pd
import re


def readcsv(filename):
    df = pd.read_csv(filename)
    votes = df['Votes']
    votecol = pd.DataFrame(columns=['Votes'])

    for vote in votes:
        vote = re.search(r'\d+', vote).group()
        votecol = pd.concat([votecol, pd.DataFrame({'Votes': [int(vote)]})], ignore_index=True)
    # print(type(votecol['Votes'].iloc[0]))

    df['Votes'] = votecol['Votes']
    return df


def df2list(df):
    data = []
    for i in range(len(df)):
        data.append([df['Name'][i], df['Grade'][i], df['Votes'][i]])
    return data


def ploting(x_data, y_data, names):
    (
        Scatter(
            init_opts=opts.InitOpts(width="1600px", height="800px")
                )
        .add_xaxis(xaxis_data=x_data)
        .add_yaxis(
            series_name="",
            y_axis=[list(z) for z in zip(y_data, names)],
            symbol_size=5,
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
                min_ = 'dataMin',
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

if __name__ == '__main__':

    df = readcsv('gradevsvotes.csv')
    data = df2list(df)

    x_data = [d[2] for d in data]
    y_data = [d[1] for d in data]
    names = [d[0] for d in data]

    ploting(x_data, y_data, names)