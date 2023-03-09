import pandas as pd
import plotly.express as px

one_worker_DF = pd.read_csv('1_worker_1678179335.177705.csv')
one_worker_DF['num_workers'] = 1 
three_worker_DF = pd.read_csv('3_workers_1678182062.994196.csv')
three_worker_DF['num_workers'] = 3
five_worker_DF = pd.read_csv('5_workers_1678197207.055081.csv')
five_worker_DF['num_workers'] = 5


all_data = pd.concat([one_worker_DF, three_worker_DF, five_worker_DF])

print(all_data)

fig = px.line(all_data, x="Name", y="Average Response Time", color='num_workers')

fig.show()
