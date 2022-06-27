import plotly.express as pe
import random 

import plotly.figure_factory as ff

dice_result=[]
count=[]
for i in range(1,100):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    dice_result.append(dice1+dice2)
    count.append(i)
#fig=pe.bar(x=dice_result, y=count)

# draw a distribution plot - create_distplot( [data] , ["Label for graph"] )
fig = ff.create_distplot( [dice_result] , ["Dice Result"] , show_hist=False  )
fig.show()