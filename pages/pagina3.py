import dash
from dash import dcc, html, Input, Output, callback_context
import numpy as np
import plotly.graph_objects as go

# Registrar esta página
dash.register_page(__name__, path='/pagina3', name="Página 3")

# === LAYOUT ===
layout = html.Div(style={
    'fontFamily': 'Segoe UI, sans-serif',
    'backgroundColor': '#ffffff',
    'padding': '30px'
}, children=[

    html.Div(style={'display': 'flex', 'justifyContent': 'space-between'}, children=[

        # PANEL IZQUIERDO
        html.Div([
            html.H4("Parámetros del modelo", style={'textAlign': 'center', 'marginBottom': '25px'}),

            # P(0)
            html.Label("Población inicial P(0):", style={'fontWeight': 'bold'}),
            dcc.Input(id='input-P0', type='number', value=400, style={'width': '100%', 'marginBottom': '8px'}),
            dcc.Slider(id='slider-P0', min=100, max=1000, step=10, value=400,
                       tooltip={"placement": "bottom"},
                       marks={100: '100', 500: '500', 1000: '1000'}),
            html.Br(),

            # r
            html.Label("Tasa de crecimiento (r):", style={'fontWeight': 'bold'}),
            dcc.Input(id='input-r', type='number', value=0.08, step=0.01,
                      style={'width': '100%', 'marginBottom': '8px'}),
            dcc.Slider(id='slider-r', min=0.01, max=0.2, step=0.005, value=0.08,
                       tooltip={"placement": "bottom"},
                       marks={0.01: '0.01', 0.1: '0.1', 0.2: '0.2'}),
            html.Br(),

            # K
            html.Label("Capacidad de carga (K):", style={'fontWeight': 'bold'}),
            dcc.Input(id='input-K', type='number', value=750, style={'width': '100%', 'marginBottom': '8px'}),
            dcc.Slider(id='slider-K', min=200, max=1500, step=10, value=750,
                       tooltip={"placement": "bottom"},
                       marks={200: '200', 800: '800', 1500: '1500'}),
            html.Br(),

            # tmax
            html.Label("Tiempo máximo (t):", style={'fontWeight': 'bold'}),
            dcc.Input(id='input-tmax', type='number', value=200, style={'width': '100%', 'marginBottom': '8px'}),
            dcc.Slider(id='slider-tmax', min=50, max=500, step=10, value=200,
                       tooltip={"placement": "bottom"},
                       marks={50: '50', 250: '250', 500: '500'}),
            html.Br(),

            # modelos + ecuaciones
            html.Label("Modelos a mostrar:", style={'fontWeight': 'bold', 'marginBottom': '10px'}),
            dcc.Checklist(
                id='model-select',
                options=[
                    {'label': 'Logístico', 'value': 'log'},
                    {'label': 'Exponencial', 'value': 'exp'}
                ],
                value=['log'],
                inline=True,
                style={'marginBottom': '10px'}
            ),
            html.Div([
                dcc.Markdown("**Modelo Logístico:**  \n"
                             "$$\\frac{dP}{dt} = rP\\left(1 - \\frac{P}{K}\\right)$$",
                             mathjax=True, style={'marginBottom': '8px'}),
                dcc.Markdown("**Modelo Exponencial:**  \n"
                             "$$\\frac{dP}{dt} = rP$$", mathjax=True)
            ], style={'backgroundColor': '#f1f1f1', 'padding': '10px', 'borderRadius': '8px',
                      'border': '1px solid #ddd', 'fontSize': '14px', 'marginBottom': '20px'}),

            # botón
            html.Button("Ver desde el punto cero", id='btn-reset', n_clicks=0, style={
                'width': '100%', 'backgroundColor': '#6c757d', 'color': 'white',
                'padding': '10px', 'border': 'none', 'borderRadius': '6px',
                'fontSize': '16px', 'cursor': 'pointer'
            })

        ], style={'width': '38%', 'padding': '25px', 'border': '2px solid #e0e0e0',
                  'borderRadius': '10px', 'backgroundColor': '#f9f9f9',
                  'boxShadow': '0px 2px 5px rgba(0,0,0,0.05)'}),

        # PANEL DERECHO (Gráfica)
        html.Div([
            html.H4("Gráfica del modelo", style={'textAlign': 'center', 'color': '#111', 'marginBottom': '10px'}),
            dcc.Graph(
                id='logistic-graph',
                style={'height': '75vh', 'width': '100%',
                       'border': '1px solid #ddd',
                       'borderRadius': '8px', 'backgroundColor': 'white'}
            )
        ], style={'width': '58%'}),
    ])
])


# === CALLBACK PARA SINCRONIZAR INPUTS ↔ SLIDERS ===
@dash.callback(
    Output('input-P0', 'value'),
    Output('slider-P0', 'value'),
    Output('input-r', 'value'),
    Output('slider-r', 'value'),
    Output('input-K', 'value'),
    Output('slider-K', 'value'),
    Output('input-tmax', 'value'),
    Output('slider-tmax', 'value'),
    Input('input-P0', 'value'),
    Input('slider-P0', 'value'),
    Input('input-r', 'value'),
    Input('slider-r', 'value'),
    Input('input-K', 'value'),
    Input('slider-K', 'value'),
    Input('input-tmax', 'value'),
    Input('slider-tmax', 'value'),
)
def sync_all(inp_P0, sld_P0, inp_r, sld_r, inp_K, sld_K, inp_tmax, sld_tmax):
    ctx = callback_context
    triggered = ctx.triggered[0]['prop_id'] if ctx.triggered else None

    def to_float_or(x, default):
        try:
            return float(x)
        except:
            return default

    P0 = to_float_or(inp_P0, 400)
    r = to_float_or(inp_r, 0.08)
    K = to_float_or(inp_K, 750)
    tmax = to_float_or(inp_tmax, 200)

    # Sincronización bidireccional
    if triggered and 'slider-P0.value' in triggered:
        inp_P0 = sld_P0
    elif triggered and 'input-P0.value' in triggered:
        sld_P0 = inp_P0

    if triggered and 'slider-r.value' in triggered:
        inp_r = sld_r
    elif triggered and 'input-r.value' in triggered:
        sld_r = inp_r

    if triggered and 'slider-K.value' in triggered:
        inp_K = sld_K
    elif triggered and 'input-K.value' in triggered:
        sld_K = inp_K

    if triggered and 'slider-tmax.value' in triggered:
        inp_tmax = sld_tmax
    elif triggered and 'input-tmax.value' in triggered:
        sld_tmax = inp_tmax

    return inp_P0, sld_P0, inp_r, sld_r, inp_K, sld_K, inp_tmax, sld_tmax


# === CALLBACK PRINCIPAL ===
@dash.callback(
    Output('logistic-graph', 'figure'),
    Input('input-P0', 'value'),
    Input('input-r', 'value'),
    Input('input-K', 'value'),
    Input('input-tmax', 'value'),
    Input('model-select', 'value'),
    Input('btn-reset', 'n_clicks')
)
def actualizar_grafica(P0, r, K, tmax, modelos, n_reset):
    ctx = callback_context
    triggered = ctx.triggered[0]['prop_id'] if ctx.triggered else ''

    # Si el usuario NO ha presionado el botón aún, no mostramos nada
    if 'btn-reset' not in triggered or n_reset == 0:
        fig = go.Figure()
        fig.update_layout(
            title="<b>Modelos de Crecimiento Poblacional</b><br>(Presiona 'Ver desde el punto cero' para iniciar)",
            xaxis_title="Tiempo (t)",
            yaxis_title="Población P(t)",
            template="plotly_white",
            margin=dict(l=60, r=40, t=60, b=60),
            annotations=[dict(
                text="⬅️ Ajusta los parámetros y luego presiona el botón para ver la simulación",
                xref="paper", yref="paper",
                x=0.5, y=0.5, showarrow=False, font=dict(size=14, color="gray")
            )]
        )
        return fig

    # Cálculos solo si se presionó el botón
    try:
        P0, r, K, tmax = float(P0), float(r), float(K), float(tmax)
    except:
        return go.Figure()

    t = np.linspace(0, tmax, 300)
    fig = go.Figure()

    if 'log' in modelos:
        P_log = K / (1 + ((K - P0) / P0) * np.exp(-r * t))
        fig.add_trace(go.Scatter(x=t, y=P_log, mode='lines', name='Logístico',
                                 line=dict(color='#0074D9', width=2)))

    if 'exp' in modelos:
        P_exp = P0 * np.exp(r * t)
        fig.add_trace(go.Scatter(x=t, y=P_exp, mode='lines', name='Exponencial',
                                 line=dict(color='green', dash='dash')))

    fig.update_layout(
        title="<b>Modelos de Crecimiento Poblacional</b>",
        xaxis_title="Tiempo (t)",
        yaxis_title="Población P(t)",
        template="plotly_white",
        margin=dict(l=60, r=40, t=60, b=60),
        legend=dict(x=0.02, y=0.98)
    )

    # Ajustar ejes al reiniciar
    fig.update_xaxes(range=[0, tmax])
    fig.update_yaxes(range=[0, max(P0, K) * 1.1])

    return fig
