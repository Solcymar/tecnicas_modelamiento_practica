import dash
from dash import html, dcc

# === CONFIGURACIÓN DE LA APP ===
app = dash.Dash(
    __name__,
    use_pages=True,  # Activa sistema de multipáginas
    suppress_callback_exceptions=True,  # 👈 evita errores "ID not found in layout"
    assets_folder='assets',
    assets_url_path='assets'
)

# === LAYOUT PRINCIPAL ===
app.layout = html.Div([

    # === HEADER PRINCIPAL ===
    html.Header([
        html.Div([
            html.H1("Técnicas de Modelamiento", className='header-title'),
            html.P("Escuela de Computación Científica", className='header-subtitle')
        ], className='header-content')
    ], className='app-header'),
    
    # === BARRA DE NAVEGACIÓN ===
    html.Nav([
        html.Div([
            html.Div([
                # Genera enlaces automáticos a todas las páginas registradas
                dcc.Link(
                    f"{page['name']}", 
                    href=page["relative_path"],
                    className='nav-link'
                )
                for page in dash.page_registry.values()
            ], className='nav-links-container')
        ], className='nav-inner')
    ], className='navigation'),
    
    # === CONTENIDO PRINCIPAL ===
    html.Main([
        dash.page_container  # 👈 aquí se muestra el contenido de cada página
    ], className='main-content'),
    
    # === FOOTER ===
    html.Footer([
        html.Div([
            html.P("© 2025 Marcela Ventura - Técnicas de Modelamiento"),
            html.Div([
                dcc.Link("Inicio", href="/", className='footer-link'),
                dcc.Link("Página 1", href="/pagina1", className='footer-link'),
                dcc.Link("Página 2", href="/pagina2", className='footer-link'),
                dcc.Link("Página 3", href="/pagina3", className='footer-link')  # 👈 añadida para acceso rápido
            ], className='footer-links')
        ], className='footer-content')
    ], className='app-footer')

], className='app-container')


# === INICIO DEL SERVIDOR ===
if __name__ == "__main__":
    app.run(debug=True)
