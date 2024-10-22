from dash import Dash
import dash_bootstrap_components as dbc

# Crear la aplicación Dash
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)
server = app.server
