import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from app import server
from apps import home, prov, registration

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output(component_id="page-content", component_property="children"),
              Input(component_id="url", component_property="pathname"))
def display_page(pathname):
    if pathname == "/":
        return home.layout
    elif pathname == "/home":
        return home.layout
    elif pathname == "/provenance":
        return prov.layout
    elif pathname == "/registration":
        return registration.layout
    else:
        return "404 page error!"


if __name__ == '__main__':
    app.run_server(debug=False)
