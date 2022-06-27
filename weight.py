import plotly.express as pe
import pandas as pd
import plotly.figure_factory as ff

df=pd.read_csv("data.csv")
x=df["Weight(Pounds)"].tolist()
fig=ff.create_distplot([x], ["Weight In Inches"], show_hist=False)
fig.show()