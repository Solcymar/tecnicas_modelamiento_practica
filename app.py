import dash
from dash import html, dcc

app = dash.Dash(
    __name__,
    use_pages=True,
    assets_folder='assets',
    assets_url_path='assets'
)

app.layout = html.Div([
    # Header principal
    html.Header([
        html.Div([
            html.H1("Técnicas de Modelamiento", className='header-title'),
            html.P("Escuela de Computación Científica", className='header-subtitle')
        ], className='header-content')
    ], className='app-header'),
    
    # Barra de navegación
    html.Nav([
        html.Div([
            html.Div([
                dcc.Link(
                    f"{page['name']}", 
                    href=page["relative_path"],
                    className='nav-link'
                )
                for page in dash.page_registry.values()
            ], className='nav-links-container')
        ], className='nav-inner')
    ], className='navigation'),
    
    # Contenido principal
    html.Main([
        dash.page_container
    ], className='main-content'),
    
    # Footer
    html.Footer([
        html.Div([
            html.P("© 2025 Marcela Ventura - Técnicas de Modelamiento"),
            html.Div([
                dcc.Link("Inicio", href="/", className='footer-link'),
                dcc.Link("Página 1", href="/pagina1", className='footer-link'),
                dcc.Link("Página 2", href="/pagina2", className='footer-link')
            ], className='footer-links')
        ], className='footer-content')
    ], className='app-footer')
], className='app-container')

if __name__ == "__main__":
    app.run(debug=True)