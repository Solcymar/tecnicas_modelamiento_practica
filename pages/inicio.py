import dash
from dash import html, dcc

dash.register_page(__name__, path="/", name="Inicio")

layout = html.Div(
    className="warm-minimal-main",
    id="mainContent",
    children=[
        
        # Hero Section
        html.Section(
            className="hero",
            children=[
                html.Div(
                    className="hero-content",
                    children=[
                        html.Div(
                            className="hero-text",
                            children=[
                                html.H2("Marcela Marisol Ventura Castillo", className="hero-tagline"),
                                html.P(
                                    '"Estudiante de Pregrado en Computación Científica. '
                                    'Facultad de Ciencias Matemática."',
                                    className="hero-description"
                                ),
                                html.Div(
                                    className="hero-cta",
                                    children=[
                                        dcc.Link("Sobre mí", href="/", className="cta-button primary"),
                                        dcc.Link("Ver Proyectos", href="/", className="cta-button secondary")
                                    ]
                                )
                            ]
                        ),
                        html.Div(
                            className="hero-image",
                            children=[
                                html.Div(
                                    className="profile-frame",
                                    children=[
                                        
                                        html.Img(
                                          src="/assets/images/perfil.jpg",
                                          className="profile-photo"  
                                        ),
                                        
                                        html.Div(className="decorative-circle circle-1"),
                                        html.Div(className="decorative-circle circle-2"),
                                        html.Div(className="decorative-circle circle-3")
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ]
        ),

        # Sobre Mí
        html.Section(
            className="about",
            children=[
                html.H2("Sobre Mí", className="section-title"),
                html.Div(
                    className="about-content",
                    children=[
                        html.Div(
                            className="about-text",
                            children=[
                                html.P([
                                    "Mi nombre es ",
                                    html.Strong("Marcela Marisol Ventura Castillo"),
                                    ". Estudio ",
                                    html.Em("Computación Científica"),
                                    " en la Universidad Nacional Mayor de San Marcos y formo parte de la ",
                                    html.Em("IEEE Computational Intelligence Society (CIS)"),
                                    ", donde soy SubDirectora del área de Eventos. Me gusta pensar en mi trabajo como una forma de organizar ideas y transformarlas en algo que tenga impacto."
                                ]),
                                html.P(
                                    "Me interesa explorar cómo la estética y la tecnología pueden encontrarse para dar lugar a experiencias digitales que sean tanto funcionales como memorables."
                                ),
                                html.P(
                                    "Además del código y el diseño, tengo un fuerte vínculo con la literatura y la escritura, encontrando inspiración en historias cargadas de realismo. También disfruto bailar y, sobre todo, las conversaciones profundas: esas que abren espacio a la ironía, la risa y, a veces, a verdades incómodas."
                                ),
                                
                            ]
                        ),
                        html.Div(
                            className="about-stats",
                            children=[
                                html.Div(
                                    className="stat-item",
                                    children=[
                                        html.Div("20", className="stat-number"),
                                        html.Div("años", className="stat-label")
                                    ]
                                ),
                                html.Div(
                                    className="stat-item",
                                    children=[
                                        html.Div("6to", className="stat-number"),
                                        html.Div("Ciclo", className="stat-label")
                                    ]
                                ),
                                html.Div(
                                    className="stat-item",
                                    children=[
                                        html.Div("100%", className="stat-number"),
                                        html.Div("Interés tecnológico", className="stat-label")
                                    ]
                                ),
                                html.Div(
                                    className="stat-item",
                                    children=[
                                        html.Div("∞", className="stat-number"),
                                        html.Div("Tazas de café", className="stat-label")
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ]
        ),

        # Proyectos Destacados
        html.Section(
            id="proyectos",
            className="section",
            children=[
                html.H2("Proyectos Destacados", className="section-title"),
                html.Div(
                    className="projects-grid",
                    children=[
                        html.Div(
                            className="project-card",
                            children=[
                                html.Div(
                                    className="project-image",
                                    children=[
                                        html.Img(
                                            src="/assets/images/ollama_clase.jpg",
                                            className="project-img")]
                                ),
                                html.Div(
                                    className="project-content",
                                    children=[
                                        html.H3("Organizadora del 1er CIS Talk del CIS", className="project-title"),
                                        html.P(
                                            "Tu primer Agente IA con Python y Ollama: construyendo desde cero",
                                            className="project-description"
                                        ),
                                        html.Div(
                                            className="project-tags",
                                            children=[
                                                html.Span("Ollama", className="project-tag"),
                                                html.Span("LangChain", className="project-tag"),
                                                html.Span("Streamlit", className="project-tag")
                                            ]
                                        ),
                                        dcc.Link(
                                            "Ver proyecto",
                                            href="https://www.instagram.com/p/DLkdzjtMikb/",
                                            className="project-link"
                                        )
                                    ]
                                )
                            ]
                        ),
                        html.Div(
                            className="project-card",
                            children=[
                                html.Div(
                                    className="project-image",
                                    children=[
                                        html.Img(
                                            src="/assets/images/hackaton_wis.jpg",
                                            className="project-img")]
                                ),
                                html.Div(
                                    className="project-content",
                                    children=[
                                        html.H3("Colaboradora en Hackatón Women in Science LATAM 2025", className="project-title"),
                                        html.P(
                                            "Colaboración en alianza con la organización Women in Science (WIS) para Hackatón.",
                                            className="project-description"
                                        ),
                                        html.Div(
                                            className="project-tags",
                                            children=[
                                                html.Span("WIS", className="project-tag"),
                                                html.Span("CIS", className="project-tag")
                                            ]
                                        ),
                                        dcc.Link(
                                            "Ver proyecto",
                                            href="https://www.instagram.com/p/DKn57HNRcPX/?img_index=1",
                                            className="project-link"
                                        )
                                    ]
                                )
                            ]
                        ),
                        html.Div(
                            className="project-card",
                            children=[
                                html.Div(
                                    className="project-image",
                                    children=[
                                        html.Img(
                                            src="/assets/images/data_certificado.jpg",
                                            className="project-img",)]
                                ),
                                html.Div(
                                    className="project-content",
                                    children=[
                                        html.H3("Página Web para negocio", className="project-title"),
                                        html.P(
                                            "Creación de página web para un negocio de catering, se le dio estructura, estilo, diseño e interactividad con los correspondientes lenguajes y programas.",
                                            className="project-description"
                                        ),
                                        html.Div(
                                            className="project-tags",
                                            children=[
                                                html.Span("Python", className="project-tag"),
                                                html.Span("Django", className="project-tag"),
                                                html.Span("Html", className="project-tag"),
                                                html.Span("Css", className="project-tag"),
                                                html.Span("Javascript", className="project-tag")
                                            ]
                                        ),
                                        dcc.Link(
                                            "Ver proyecto",
                                            href="https://github.com/Solcymar/tradicri",
                                            className="project-link"
                                        )
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ]
        ),

        # Áreas de Experiencia
        html.Section(
            id="habilidades",
            className="skills",
            children=[
                html.H2("Áreas de Experiencia", className="section-title"),
                html.Div(
                    className="skills-container",
                    children=[
                        html.Div(
                            className="skill-category",
                            children=[
                                html.H3("Desarrollo Web", className="skill-category-title"),
                                html.Div(
                                    className="skills-grid",
                                    children=[
                                        html.Div(
                                            className="skill-item",
                                            children=[
                                                html.Div("HTML", className="skill-name")
                                            ]
                                        ),
                                        html.Div(
                                            className="skill-item",
                                            children=[
                                                html.Div("CSS", className="skill-name")
                                            ]
                                        ),
                                        html.Div(
                                            className="skill-item",
                                            children=[
                                                html.Div("JavaScript", className="skill-name")
                                            ]
                                        )
                                    ]
                                )
                            ]
                        ),
                        html.Div(
                            className="skill-category",
                            children=[
                                html.H3("Lenguajes de Programación", className="skill-category-title"),
                                html.Div(
                                    className="skills-grid",
                                    children=[
                                        html.Div(
                                            className="skill-item",
                                            children=[
                                                html.Div("Python", className="skill-name")
                                            ]
                                        ),
                                        html.Div(
                                            className="skill-item",
                                            children=[
                                                html.Div("PHP", className="skill-name")
                                            ]
                                        ),
                                        html.Div(
                                            className="skill-item",
                                            children=[
                                                html.Div("C++", className="skill-name")
                                            ]
                                        )
                                    ]
                                )
                            ]
                        ),
                        html.Div(
                            className="skill-category",
                            children=[
                                html.H3("Bases de Datos", className="skill-category-title"),
                                html.Div(
                                    className="skills-grid",
                                    children=[
                                        html.Div(
                                            className="skill-item",
                                            children=[
                                                html.Div("PostgreSQL", className="skill-name")
                                            ]
                                        ),
                                        html.Div(
                                            className="skill-item",
                                            children=[
                                                html.Div("MySQL", className="skill-name")
                                            ]
                                        ),
                                        html.Div(
                                            className="skill-item",
                                            children=[
                                                html.Div("SQLite", className="skill-name")
                                            ]
                                        )
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ]
        ),

        # Mis Pasiones
        html.Section(
            id="pasiones",
            className="section",
            children=[
                html.H2("Mis Pasiones", className="section-title"),
                html.Div(
                    className="interests-grid",
                    children=[
                        html.Div(
                            className="interest-card",
                            children=[
                                html.Div("📚", className="interest-icon"),
                                html.H3("Literatura & Escritura", className="interest-title"),
                                html.P(
                                    "Exploradora de mundos a través de las palabras, tanto en la lectura como en la creación de narrativas propias.",
                                    className="interest-description"
                                )
                            ]
                        ),
                        html.Div(
                            className="interest-card",
                            children=[
                                html.Div("💻", className="interest-icon"),
                                html.H3("Tecnología Creativa", className="interest-title"),
                                html.P(
                                    "Fusionar el arte con la tecnología para crear experiencias digitales memorables y significativas.",
                                    className="interest-description"
                                )
                            ]
                        ),
                        html.Div(
                            className="interest-card",
                            children=[
                                html.Div("🎨", className="interest-icon"),
                                html.H3("Arte & Expresión", className="interest-title"),
                                html.P(
                                    "La danza y la música como formas de expresión que complementan mi visión creativa en el diseño.",
                                    className="interest-description"
                                )
                            ]
                        )
                    ]
                )
            ]
        ),

        # Script para smooth scrolling
        dcc.Location(id='url', refresh=False),
        html.Script('''
            document.addEventListener('DOMContentLoaded', function() {
                document.querySelectorAll('a[href^="#"]').forEach(anchor => {
                    anchor.addEventListener('click', function (e) {
                        e.preventDefault();
                        const targetId = this.getAttribute('href');
                        if (targetId === '#') return;
                        
                        const targetElement = document.querySelector(targetId);
                        if (targetElement) {
                            targetElement.scrollIntoView({
                                behavior: 'smooth',
                                block: 'start'
                            });
                        }
                    });
                });
            });
        ''')
    ]
)