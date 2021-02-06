import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from app import server
from apps import app1

app.layout = html.Div([
    html.Div([
        dcc.Link("registration_statistics", href="apps/app1")
    ], className="row"),
    dcc.Location(id="url", refresh=False),
    html.Div(id="page-content", children=[])
])


@app.callback(Output(component_id="page-content", component_property="children"),
              Input(component_id="url", component_property="pathname"))
def display_page(pathname):
    if pathname == "/apps/app1":
        return app1.layout
    else:
        return "404 page error!"


if __name__ == '__main__':
    app.run_server(debug=False)
