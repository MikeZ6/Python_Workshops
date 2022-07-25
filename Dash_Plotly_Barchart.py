"""
Author: Mike Zhang

Plot bar charts with selection of a particular day to view sales based on branch and time session
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

 
salesList={'day':[1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3],
           'branch' :['N','N','N','S','S','E','N','N','S','S','E','N','N',
                      'S','S','E','N','N','S','S','E','E','S','N'],
           'session':['am','am','am','pm','pm','pm','am','am','am','pm',
                      'pm','pm','am','am','am','pm','pm','pm','am','am','am','pm','pm','pm'],
           'sales':[1234.56, 2311.53, 501.22, 325.2, 6590.5,
                         4214.56, 7421.53, 591.22, 1729.2, 5650.65,
                         3231.69, 2114.30, 2501.82, 7625.10, 3950.5,
                         1433.69, 231.53, 951.22, 4325.32, 9150.85,
                         3134.56, 8231.73, 751.22, 345.2]}

df =pd.DataFrame(salesList)
print(df.info())

days = df.day.unique()
print(days)


app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Dropdown(
        id="dropdown",
        options=[{"label": x, "value":x} for x in days],
        value=days[0],
        clearable=False,
    ),
    dcc.Graph(id="bar-chart"),
])


@app.callback(
    Output("bar-chart", "figure"), 
    [Input("dropdown", "value")])
def update_bar_chart(day):
    mask = df["day"] == day
    fig = px.bar(df[mask], x="branch", y = "sales",
                 color = "session", barmode = "group")
    return fig

app.run_server(debug= False)