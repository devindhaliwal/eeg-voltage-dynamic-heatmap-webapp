import dash
import dash_core_components as dcc
import dash_html_components as html
import eeg_voltage_heatmap_dynamic


app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure=eeg_voltage_heatmap_dynamic.generate_plot())
])

app.run_server(debug=False, use_reloader=True)

