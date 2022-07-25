"""
Author: Mike Zhang

Plot pie charts with selection of either area or branch and the plots may be either sales or qty
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd



salesList={
           'area' :['N','N','S','S','E'],
           'branch':['1','2','3','4','5'],
           'sales':[1,2,3,4,5],
           'qty':[1, 23, 5, 3, 6]}
df =pd.DataFrame(salesList)
print(df)
app = dash.Dash(__name__)


app.layout = html.Div([
    html.P("Names:"),
    dcc.Dropdown(
        id='names', 
        value='area', 
        options=[{'value': x, 'label': x} 
                 for x in ['area', 'branch']],
        clearable=False
    ),
    html.P("Values:"),
    dcc.Dropdown(
        id='values', 
        value='sales', 
        options=[{'value': x, 'label': x} 
                 for x in ['sales', 'qty']],
        clearable=False
    ),
    dcc.Graph(id="pie-chart"),
])


@app.callback(
    Output("pie-chart", "figure"), 
    [Input("names", "value"), 
     Input("values", "value")])
def generate_chart(names, values):
    fig = px.pie(df, values=values, names=names)
    return fig

app.run_server(debug=False)
