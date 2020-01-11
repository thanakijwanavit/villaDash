import dash
import dash_html_components as html
import flask

app = flask.Flask(__name__)
dash_app = dash.Dash(__name__, server = app, url_base_pathname = '/')

dash_app.css.append_css({"external_url" : "https://codepen.io/chriddyp/pen/bWLwgP.css"})

colors = {
    'background' : '#a9a9a9',
    'text' : '#7FDBFF'
}


dash_app.layout = html.Div(
    [
        html.Div(
            [
                html.H1(
                    "Villa_dash",
                    style={
                        'text-align':'center',
                    }
                ),
            ],
        )
    ],
)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=80)