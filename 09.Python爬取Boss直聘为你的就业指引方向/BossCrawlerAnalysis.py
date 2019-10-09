from pyecharts.charts import Line
import pandas as pd
from eplot import eplot


class BossCrawlerAnalysis:
    def __init__(self):
        pass

    def read_csv(self):
        data = pd.read_csv("boss_info1.csv", sep=",", header=0)
        print(data.groupby('城市').mean()['薪资'].to_frame('sla').reset_index().sort_values('sla', ascending=False))
        result = data.groupby('城市').apply(lambda x: x.mean()).round(1)['薪资'].to_frame(
            'sla').reset_index().sort_values('薪资', ascending=False)
        charts_bar = (
            Line()
                .set_global_opts(
                title_opts={"text": "全国python薪酬榜"})
                .add_xaxis(result.city.values.tolist())
                .add_yaxis("薪资", result.sla.values.tolist())
        )
        charts_bar.render('Python.html')


if __name__ == '__main__':
    main = BossCrawlerAnalysis()
    main.read_csv()
