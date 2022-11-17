import get_data
from dash import Dash, html, dcc
from dash.dependencies import Input, Output, State

app = Dash(__name__)

app.layout = html.Div(
    className="body",
    children=[
        html.Div(
            className="search-bar",
            children=[
                html.Div(
                    className="search-input",
                    children= [
                        dcc.Input(className="username", id="username", type="text", value="@elonmusk")
                    ]
                ),
                html.Div(
                    className="submit-button",
                    children= [
                        html.Button(className="submit", id="submit", children="submit", n_clicks=0)
                    ]
                ),
            ]
        ),
        html.Div(
            className="basic-data",
            children=[
                html.Div(
                    className="username-data",
                    children= [
                        html.H2(className="username-recibed", id="username-recibed", children="")
                    ]
                ),
                html.Div(
                    className="cards",
                    children= [
                        html.Div(
                            className="followers-count",
                            children= [
                                html.P(className="followers-text", id="followers-text", children="Contador de seguidores"),
                                html.P(className="followers-number", id="followers-number", children="12345")
                            ]
                        ),
                        html.Div(
                            className="following-count",
                            children= [
                                html.P(className="following-text", id="following-text", children="Contador de seguidos"),
                                html.P(className="following-number", id="following-numbre", children="12345")
                            ]
                        ),
                        html.Div(
                            className="favourites-count",
                            children= [
                                html.P(className="favourites-text", id="favourites-text", children="Contador de me gusta"),
                                html.P(className="favourites-number", id="favourites-number", children="12345")
                            ]
                        ),
                    ]
                ),
            ]
        ),
    ]
)

@app.callback(
    Output('username-recibed', 'children'),
    Input('submit', 'n_clicks'),
    State('username', 'value')
)
def update_output(n_clicks, username):
    get_data.visualizeUsers(username)
    return u'{}'.format(username)

@app.callback(
    Output('favourites-number', 'children'),
    Input('submit', 'n_clicks')
)
def send_number(n_clicks):
    favourites_number = 283
    return u'{}'.format(favourites_number)

if __name__ == '__main__':
    app.run_server(debug=True)
