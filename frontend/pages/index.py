import dash
from dash import html, dcc

dash.register_page(__name__,
                    path="/",
                    title="Sitio de administración de TipOn",
                    name="inicio")

layout = html.Div(
    className="bg-gray-50",
    children=[
        html.Div(
            className="bg-cover bg-no-repeat",
            style={"background-image": "url(assets/images/propina.jpg)"},
            children=[html.Div(className="bg-black bg-opacity-50 w-full h-full")],
        ),
        html.Header(
            className="bg-blue-600 bg-cover bg-no-repeat drop-shadow-lg px-2 py-80 text-center text-white py",
            style={"background-image": "url(./assets/images/propina.jpg)"},
            children=[
                html.Div(className="absolute inset-0 bg-blue-400 opacity-50"),
                html.Div(
                    className="relative",
                    children=[
                        html.H2(
                            className="mb-4 font- text-6xl md:text-6xl type font-bold font-serif",
                            children=["AnalyTips"],
                        ),
                        html.P(
                            className="mb-6 text-2xl md:text-3xl",
                            children=[
                                "Sitio de administración del sistema de propinas de TipOn"
                            ],
                        ),
                    ],
                ),
            ],
        ),
        html.Main(
            className="mx-auto px-4 py-10 max-w-7xl min-h-screen",
            children=[
                html.Section(
                    className="flex md:flex-row flex-col items-center bg-white shadow-xl mb-10 p-6 rounded-lg text-gray-700 align-baseline",
                    children=[
                        html.Div(
                            className="mb-4 md:mb-0 md:pr-6 md:w-1/2 text-center md:text-left",
                            children=[
                                html.H2(
                                    className="mb-4 font-bold text-4xl",
                                    children=["Acerca del sitio"],
                                ),
                                html.P(
                                    className="text-justify",
                                    children=[
                                        "Ahorra tiempo y esfuerzo en el seguimiento de las propinas. Esta herramienta automatiza el proceso de recopilación y análisis de datos, proporcionándote informes detallados"
                                    ],
                                ),
                            ],
                        ),
                        html.Img(
                            className="shadow-lg rounded-lg md:w-1/2",
                            src=dash.get_asset_url("images/tips.jpg"),
                            alt="Propinas",
                        ),
                    ],
                ),
                html.Div(
                    className="mx-auto container",
                    children=[
                        html.Div(
                            className="gap-4 grid grid-cols-3",
                            children=[
                                html.Div(
                                    className="bg-blue-100 shadow-md p-4",
                                    children=[
                                        html.Img(
                                            className="shadow-lg rounded-lg",
                                            src=dash.get_asset_url("images/restaurant-icon.jpg"),
                                            alt="Imagen representativa de negocios",
                                        ),
                                        html.H2(
                                            className="font-bold text-3xl text-center",
                                            children=["Negocios"],
                                        ),
                                        html.P(
                                            className="text-justify",
                                            children=[
                                                "Encuentra y administra información sobre los negocios asociados. Obten informes detallados sobre las propinas recibidas."
                                            ],
                                        ),
                                        html.Div(
                                            className="mb-4 text-center",
                                            children=[
                                                html.A(
                                                    className="inline-block bg-gradient-to-br from-teal-400 hover:from-teal-600 to-blue-500 hover:to-blue-800 shadow-lg mt-6 px-6 py-3 rounded-lg font-semibold text-white",
                                                    href="/negocios.py",
                                                    children=["Ver Negocios"],
                                                )
                                            ],
                                        ),
                                    ],
                                ),
                                html.Div(
                                    className="bg-blue-100 shadow-md p-4",
                                    children=[
                                        html.Img(
                                            className="shadow-lg rounded-lg",
                                            src=dash.get_asset_url("images/dashboard-icon.jpg"),
                                            alt="Imagen representativa de Dashboards",
                                        ),
                                        html.H2(
                                            className="font-bold text-3xl text-center",
                                            children=["Dashboards"],
                                        ),
                                        html.P(
                                            className="text-justify",
                                            children=[
                                                "Visualiza tus datos de propinas de manera intuitiva con nuestros dashboards personalizados. Estos dashboards permiten identificar oportunidades de mejora y tomar decisiones más informadas."
                                            ],
                                        ),
                                        html.Div(
                                            className="mb-4 text-center",
                                            children=[
                                                html.A(
                                                    className="inline-block bg-gradient-to-br from-teal-400 hover:from-teal-600 to-blue-500 hover:to-blue-800 shadow-lg mt-6 px-6 py-3 rounded-lg font-semibold text-white",
                                                    href="/dashboard",
                                                    children=["Ver Dashboards"],
                                                )
                                            ],
                                        ),
                                    ],
                                ),
                                html.Div(
                                    className="bg-blue-100 shadow-md p-4",
                                    children=[
                                        html.Img(
                                            className="shadow-lg rounded-lg",
                                            src=dash.get_asset_url("images/prediction-icon.jpg"),
                                            alt="Imagen representativa de predicción",
                                        ),
                                        html.H2(
                                            className="font-bold text-3xl text-center",
                                            children=["Predicción"],
                                        ),
                                        html.P(
                                            className="text-justify",
                                            children=[
                                                "Toma decisiones más inteligentes con la herramienta de predicción para identificar patrones en los datos e identificar futuros clientes"
                                            ],
                                        ),
                                        html.Div(
                                            className="mb-4 text-center",
                                            children=[
                                                html.A(
                                                    className="inline-block bg-gradient-to-br from-teal-400 hover:from-teal-600 to-blue-500 hover:to-blue-800 shadow-lg mt-6 px-6 py-3 rounded-lg font-semibold text-white",
                                                    href="/prediccion",
                                                    children=["Ver Predicciones"],
                                                )
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                        )
                    ],
                ),
            ],
        ),
    ],
)
