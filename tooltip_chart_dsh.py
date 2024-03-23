import dash
import dash_core_components as dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import random
import numpy as np

# Generiere fiktive Daten für die Eieranzahl
tage_30 = list(range(1, 31))
tage_90 = list(range(1, 91))
tage_7 = list(range(1, 8))
eieranzahl_30 = [random.randint(20, 40) for _ in range(30)]
eieranzahl_90 = [random.randint(20, 40) for _ in range(90)]
eieranzahl_7 = [random.randint(20, 40) for _ in range(7)]
eieranzahl_mean_30 = [np.mean(eieranzahl_30)] * len(eieranzahl_30)
eieranzahl_mean_90 = [np.mean(eieranzahl_90)] * len(eieranzahl_90)
eieranzahl_mean_7 = [np.mean(eieranzahl_7)] * len(eieranzahl_7)

# Erstelle Subplots für 30 und 90 Tage
fig_30 = make_subplots(rows=1, cols=2, shared_xaxes=True, shared_yaxes=True, vertical_spacing=0, horizontal_spacing=0)
fig_30.add_trace(go.Scatter(x=tage_30, y=eieranzahl_30, mode='lines+markers', name='Eieranzahl (30 Tage)'), row=1,
                 col=1)
fig_30.add_trace(go.Scatter(x=tage_30, y=eieranzahl_mean_30, mode='lines', name='Mittelwert Eieranzahl (30 Tage)'),
                 row=1, col=1)
fig_30.add_trace(go.Histogram(y=eieranzahl_30, name='Histogramm (30 Tage)'), row=1, col=2)

fig_90 = make_subplots(rows=1, cols=2, shared_xaxes=True, shared_yaxes=True, vertical_spacing=0, horizontal_spacing=0)
fig_90.add_trace(go.Scatter(x=tage_90, y=eieranzahl_90, mode='lines+markers', name='Eieranzahl (90 Tage)'), row=1,
                 col=1)
fig_90.add_trace(go.Scatter(x=tage_90, y=eieranzahl_mean_90, mode='lines', name='Mittelwert Eieranzahl (90 Tage)'),
                 row=1, col=1)
fig_90.add_trace(go.Histogram(y=eieranzahl_90, name='Histogramm (90 Tage)'), row=1, col=2)

fig_7 = make_subplots(rows=1, cols=2, shared_xaxes=True, shared_yaxes=True, vertical_spacing=0, horizontal_spacing=0)
fig_7.add_trace(go.Scatter(x=tage_7, y=eieranzahl_7, mode='lines+markers', name='Eieranzahl (30 Tage)'), row=1,
                 col=1)
fig_7.add_trace(go.Scatter(x=tage_7, y=eieranzahl_mean_7, mode='lines', name='Mittelwert Eieranzahl (30 Tage)'),
                 row=1, col=1)
fig_7.add_trace(go.Histogram(y=eieranzahl_7, name='Histogramm (30 Tage)'), row=1, col=2)

# Layout anpassen
fig_30.update_layout(title_text="Eieranzahl über 30 Tage",
                     xaxis_title="Tage",
                     yaxis_title="Eieranzahl",
                     height=580,
                     bargap=0.1)

fig_90.update_layout(title_text="Eieranzahl über 90 Tage",
                     xaxis_title="Tage",
                     yaxis_title="Eieranzahl",
                     height=580,
                     bargap=0.1)

fig_7.update_layout(title_text="Eieranzahl über 7 Tage",
                     xaxis_title="Tage",
                     yaxis_title="Eieranzahl",
                     height=580,
                     bargap=0.1)

# Dash-App erstellen
app = dash.Dash(__name__)

# Layout der Dash-App
app.layout = html.Div([
    dcc.Graph(
        id='main-chart',
    ),
    dcc.Dropdown(
        id='dropdown-days',
        options=[
            {'label': '30 Tage', 'value': 30},
            {'label': '90 Tage', 'value': 90},
            {'label': '7 Tage', 'value': 7}
        ],
        value=30,
        style={'width': '150px', 'margin': '0 auto'}  # Anpassen der Breite des Dropdown-Menüs
    ),
],
    style={'margin': '0 auto'})  # Anpassen der Position und Breite der Visualisierungen)


# Callback für die Aktualisierung des Subplots basierend auf Dropdown-Wert
@app.callback(
    Output('main-chart', 'figure'),
    [Input('dropdown-days', 'value')]
)
def update_chart(selected_days):
    if selected_days == 30:
        return fig_30
    elif selected_days == 90:
        return fig_90
    else:
        return fig_7


# Dash-App starten
if __name__ == '__main__':
    app.run_server(debug=True)

server = app.server
