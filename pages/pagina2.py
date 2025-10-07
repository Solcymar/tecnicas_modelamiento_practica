import dash
from dash import dcc, html
import numpy as np

dash.register_page(__name__, path='/pagina2', name="Página 2")

# === Modelo Logístico ===
P0 = 100     # Población inicial
r = 0.03     # Tasa de crecimiento
K = 1000     # Capacidad de carga
t = np.linspace(0, 100, 200)
P = K / (1 + ((K - P0) / P0) * np.exp(-r * t))

layout = html.Div(style={
    'display': 'flex',
    'height': 'calc(100vh - 60px)',
    'margin': '0',
    'padding': '0',
    'fontFamily': 'Segoe UI, sans-serif',
    'fontSize': '15px',
    'color': '#202122',
    'backgroundColor': '#f8f9fa'
}, children=[

    # ==== Panel Izquierdo: Explicación ====
    html.Div(style={
        'width': '50%',
        'padding': '40px',
        'overflowY': 'auto',
        'backgroundColor': '#ffffff',
        'borderRight': '1px solid #dcdcdc',
        'boxSizing': 'border-box',
    }, children=[

        html.H2("Modelo de Crecimiento Logístico", style={
            'color': '#2b2b2b',
            'marginBottom': '20px',
            'fontWeight': '600'
        }),

        dcc.Markdown("""
El modelo logístico describe cómo una población crece en un ambiente con recursos limitados.  
A diferencia del crecimiento exponencial, este modelo incluye una **capacidad de carga** \(K\), que representa el tamaño máximo de población que el entorno puede sostener.

### Ecuación diferencial

$$
\\frac{dP}{dt} = rP\\left(1 - \\frac{P}{K}\\right)
$$

### Solución general

$$
P(t) = \\frac{K}{1 + \\left(\\frac{K - P_0}{P_0}\\right)e^{-rt}}
$$

### Parámetros usados en este ejemplo

- \( P_0 = 100 \): población inicial  
- \( r = 0.03 \): tasa de crecimiento  
- \( K = 1000 \): capacidad de carga máxima  

Con estos valores, observamos cómo la población se aproxima a \(K\) conforme \(t\) aumenta.
        """, mathjax=True, style={'whiteSpace': 'pre-line'})
    ]),

    # ==== Panel Derecho: Gráfico ====
    html.Div(style={
        'width': '50%',
        'padding': '20px',
        'backgroundColor': '#ffffff',
        'boxSizing': 'border-box',
        'display': 'flex',
        'flexDirection': 'column',
        'justifyContent': 'center',
        'alignItems': 'center',
        'borderLeft': '1px solid #dcdcdc'
    }, children=[

        dcc.Graph(
            id='logistic-growth-graph',
            figure={
                'data': [{
                    'x': t,
                    'y': P,
                    'mode': 'lines+markers',
                    'line': {'dash': 'solid', 'color': '#0074D9', 'width': 2},
                    'marker': {'color': '#7FDBFF', 'symbol': 'circle', 'size': 5},
                    'name': 'P(t)',
                    'hovertemplate': 't: %{x:.1f}<br>P(t): %{y:.1f}<extra></extra>'
                }],
                'layout': {
                    'title': {
                        'text': '<b>Evolución del Crecimiento Logístico</b>',
                        'font': {'size': 20, 'color': '#111111'},
                        'x': 0.5
                    },
                    'xaxis': {'title': 'Tiempo (t)', 'gridcolor': '#e0e0e0'},
                    'yaxis': {'title': 'Población P(t)', 'gridcolor': '#e0e0e0'},
                    'margin': {'l': 60, 'r': 30, 't': 60, 'b': 60},
                    'paper_bgcolor': 'rgba(0,0,0,0)',
                    'plot_bgcolor': '#ffffff',
                    'font': {'family': 'Segoe UI, Arial, sans-serif', 'size': 13, 'color': '#202122'},
                    'legend': {'bgcolor': 'rgba(0,0,0,0)', 'bordercolor': '#dddddd', 'borderwidth': 1}
                }
            },
            style={
                'height': '100%',
                'width': '100%',
                'border': '1px solid #e1e4e8',
                'borderRadius': '8px',
                'backgroundColor': 'white',
                'padding': '10px'
            }
        )
    ])
])
