import dash
import dash_svg
import pandas as pd
import plotly.express as px
import requests
from dash import html, dcc, callback, Input, Output, State, ALL, ctx

#backend_url = "http://127.0.0.1:8000"

df_restaurants = pd.read_csv('TOTAL.csv')

dash.register_page(__name__,
                    path="/negocios",
                    title="Vista de negocios",
                    name="negocios")

layout = html.Div(
    className="bg-gray-50",
    children=[
        html.Main(
            className="mx-auto px-4 py-10 max-w-7xl min-h-screen text-gray-700",
            children=[
                html.Section(
                    className="flex flex-col bg-white shadow-xl p-6 rounded-lg",
                    children=[
                        html.Div(className="flex justify-end mb-4"),
                            html.Div(
                                className="text-center",
                                children=[
                                    html.H2(
                                        className="mb-4 font-semibold text-5xl",
                                        children=["Restaurantes con los que trabajamos"],
                                    )
                                ],
                            ),

                        # Search bar
                        html.Div(
                            className="mb-4 flex justify-center",
                            children=[
                                #dcc.Input(                                   id="search-terms",                                    className="w-96 rounded-l-lg border border-gray-300 px-4 py-2 focus:outline-none focus:ring focus:ring-blue-300"),
                                
                                # Botón para cargar restaurantes

                                html.Button(
                                    id="load-button",
                                    n_clicks=0,
                                    #id="search-button",
                                    className="rounded-r-lg bg-blue-600 px-4 text-white hover:bg-blue-700 focus:outline-none focus:ring focus:ring-blue-300",
                                    children=["Cargar Restaurantes"],
                                )
                            ],
                        ),
                        # Placeholder for the restaurant list
                        html.Div(id="restaurant-list", className="mt-8"),

                        # Contenedor para los detalles
                        # Contenedor para el modal de detalles del restaurante
                        html.Div(
                            id="modal",
                            className="fixed inset-0 flex items-center justify-center bg-gray-800 bg-opacity-50 hidden",
                            children=[
                                html.Div(
                                    className="bg-white p-6 rounded-lg shadow-lg w-1/2",
                                    children=[
                                        html.H2(
                                            id="modal-title",
                                            className="text-2xl font-semibold mb-4"
                                        ),
                                        html.P(
                                            id="modal-content",
                                            className="text-gray-700"
                                        ),
                                        html.Button(
                                            id="close-modal",
                                            className="mt-4 rounded-lg bg-red-500 px-4 py-2 text-white hover:bg-red-600",
                                            children=["Cerrar"]
                                        )
                                    ]
                                )
                            ]
                        )

                        
                    ],
                ),
            ],
        ),
    ],
)

# Callback to update the restaurant list
@callback(
    Output("restaurant-list", "children"),
    #[Input("load-button", "n_clicks"), Input("search-terms", "value")]
    Input("load-button", "n_clicks")
)
def update_restaurant_list(n_clicks):
    if n_clicks is not None:
        try:
        # Realizar la solicitud al backend FastAPI
            response = requests.get('http://localhost:8000/api/restaurantes')
            response.raise_for_status()  # Esto generará una excepción si hay un error HTTP

        
        # Comprobar si la solicitud fue exitosa
        #if response.status_code == 200:
            data = response.json()
            
            # Crear una lista de elementos HTML con los datos de los restaurantes
            #restaurant_elements = []
            restaurants=data.get('restaurants', [])
            #for restaurant in restaurants:
            restaurant_elements=[
                html.Section(
                    className="bg-blue-50 shadow-md p-4 mb-4 rounded-lg flex flex-col",
                    children=[
                        html.H3(
                            className="text-xl font-bold text-blue-800",
                            children=[f"Restaurante {restaurant[0]}"]
                        ),
                        html.H2(
                            className="text-gray-500 text-xl font-bold",
                            children=[f" {restaurant[1]}"]
                        ),
                        html.Button(
                                        id={"type":"restaurant-button", "index":restaurant[0]},
                                        className="rounded-md bg-gradient-to-br from-teal-400 to-blue-500 px-2 py-1 font-semibold text-white hover:from-pink-300 hover:to-orange-600",
                                        children=["Ver detalles"],
                                    ),
                    ]
                ) for restaurant in restaurants
            ]
                
            return restaurant_elements
        
        except requests.exceptions.RequestException as e:
            # Mostrar el error en la interfaz si ocurre un problema con la solicitud
            return [html.P(f"Error al cargar los datos de los restaurantes: {e}")]
    
        #else:             return [html.P("Error al cargar los datos de los restaurantes.")]
    
    return [html.P("No se encontraron restaurantes.")]



# Callback para manejar el modal
@callback(
    [Output("modal", "className"),
    Output("modal-title", "children"),
    Output("modal-content", "children")],
    [Input({"type": "restaurant-button", "index": ALL}, "n_clicks"),
    Input("close-modal", "n_clicks")],
    [State({"type": "restaurant-button", "index": ALL}, "id")],
    prevent_initial_call=True
)
def toggle_modal(n_clicks_list, close_click, button_ids):
    # Detectar qué botón fue presionado
    triggered = ctx.triggered_id

    if triggered is None:
        return "fixed inset-0 flex items-center justify-center bg-gray-800 bg-opacity-50 hidden", "", ""

    # Si se presionó el botón de cerrar, ocultar el modal
    if triggered == "close-modal":
        return "fixed inset-0 flex items-center justify-center bg-gray-800 bg-opacity-50 hidden", "", ""

    # Si uno de los botones de restaurante fue presionado, mostrar el modal
    for idx, n_clicks in enumerate(n_clicks_list):
        if n_clicks:
            # Obtener el ID y el nombre del restaurante desde el atributo `id`
            restaurant_id = button_ids[idx].get('index')
            restaurant_name = button_ids[idx].get('name')

            # Aquí puedes obtener detalles adicionales del restaurante si es necesario
            return (
                "fixed inset-0 flex items-center justify-center bg-gray-800 bg-opacity-50",
                f"Detalles del Restaurante {restaurant_id} - {restaurant_name}",
                f"Información adicional sobre el restaurante {restaurant_name} (ID: {restaurant_id})."
            )

    return "fixed inset-0 flex items-center justify-center bg-gray-800 bg-opacity-50 hidden", "", ""