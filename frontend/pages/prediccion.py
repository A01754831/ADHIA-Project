import io
import os

import base64
import dash
import dash_svg
#import dash_ag_grid as dag
import pandas as pd
import plotly.express as px
from dotenv import load_dotenv, find_dotenv
from pydantic import BaseModel
import requests
#import openai
#import tavily
from dash import dcc, html, callback, Output, Input, State

#from langchain_openai import ChatOpenAI

# Página de predicción
dash.register_page(__name__, 
                    path="/prediccion", 
                    name="Predicción", 
                    title="Chatbot"
                )
# URL del backend
#backend_url = "http://localhost:8000"


# Layout de la página
layout = html.Div(
    html.Main(
        className="mx-auto px-4 py-10 max-w-7xl min-h-screen text-gray-700",
        children=[
            

            # Sección para formulario de predicción
            html.Section(
                className="flex flex-col bg-white shadow-lg mb-10 p-6 rounded-lg text-gray-700",
                children=[
                    html.H2(
                        className="mb-4 font-semibold text-4xl",
                        children=["Predicción para un restaurante"],
                    ),
                    html.P(
                        className="mb-4 text-xl",
                        children=["Ingresa los datos del restaurante para obtener la predicción de clasificación de propinas"],
                    ),
                    html.Div(
                        #action="3",  # Assuming this is a placeholder, adjust as needed
                        
                        className="space-y-6",
                        children=[
                            html.Div(
                                children=[
                                    html.Label(
                                        className="block font-medium text-gray-700 text-lg",
                                        children=["Número de estrellas"],
                                    ),
                                    dcc.Input(
                                        id="stars",
                                        type="number",
                                        className="mt-2 w-full rounded-md border border-gray-300 p-3 shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500",
                                    ),
                                ]
                            ),
                            html.Div(
                                children=[
                                    html.Label(
                                        className="block font-medium text-gray-700 text-lg",
                                        children=["Cuenta total"],
                                    ),
                                    dcc.Input(
                                        id="total",
                                        type="number",
                                        className="mt-2 w-full rounded-md border border-gray-300 p-3 shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500",
                                    ),
                                ]
                            ),
                            html.Div(
                                children=[
                                    html.Label(
                                        className="block font-medium text-gray-700 text-lg",
                                        children=["Wi-Fi"],
                                    ),
                                    dcc.RadioItems(
                                        id="wifi",
                                        options=[
                                            {"label": "Sí", "value": "Yes"},
                                            {"label": "No", "value": "No"},
                                        ],
                                        inline=True,
                                        inputClassName="focus:ring-blue-500 text-blue-600 border-gray-300 mr-2",
                                        labelClassName="ml-2 text-gray-700",
                                    ),
                                ]
                            ),
                            html.Div(
                                children=[
                                    html.Label(
                                        className="block font-medium text-gray-700 text-lg",
                                        children=["Alcohol"],
                                    ),
                                    dcc.RadioItems(
                                        id="alcohol",  # Corrected to "alcohol"
                                        options=[
                                            {"label": "Sí", "value": "Yes"},
                                            {"label": "No", "value": "No"},
                                        ],
                                        inline=True,
                                        inputClassName="focus:ring-blue-500 text-blue-600 border-gray-300 mr-2",
                                        labelClassName="ml-2 text-gray-700",
                                    ),
                                ]
                            ),
                            html.Div(
                                children=[
                                    html.Label(
                                        className="block font-medium text-gray-700 text-lg",
                                        children=["Valet Parking"],
                                    ),
                                    dcc.RadioItems(
                                        id="valet",
                                        options=[
                                            {"label": "Sí", "value": "Yes"},
                                            {"label": "No", "value": "No"},
                                        ],
                                        inline=True,
                                        inputClassName="focus:ring-blue-500 text-blue-600 border-gray-300 mr-2",
                                        labelClassName="ml-2 text-gray-700",
                                    ),
                                ]
                            ),
                            html.Div(
                                className="flex justify-center",
                                children=[
                                    html.Button(
                                        id="submit-single-prediction",
                                        n_clicks=0,
                                        className="inline-block bg-gradient-to-br from-teal-400 hover:from-gray-300 to-blue-500 hover:to-cyan-300 shadow-lg px-6 py-3 rounded-lg font-semibold text-white",
                                        children=["Enviar"],
                                        )
                                    ],
                                ),
                                html.Div(
                                    className="flex justify-center font-semibold text-2xl text-blue-700",
                                    id="single-prediction-result",
                                        
                                    ),
                            ],
                        ),   
                ],
            ),
        ]
    )
)

@callback(
    Output("single-prediction-result", "children"),
    Input("submit-single-prediction", "n_clicks"),
    State("stars", "value"),
    State("total", "value"),
    State("wifi", "value"),
    State("alcohol", "value"),
    State("valet", "value"),
)
def submit_prediction(n_clicks, stars, total, wifi, alcohol, valet):
    if n_clicks > 0:
        # Construir el payload
        payload = {
            "stars": stars,
            "total": total,
            "wifi": wifi,
            "alcohol": alcohol,
            "valet": valet
        }

        # Hacer una solicitud POST al backend
        backend_url = "http://localhost:8000/predict"  # Asegúrate de que esta URL sea correcta para tu configuración
        response = requests.post(backend_url, json=payload)
        print(response)
        # Procesar la respuesta
        if response.status_code == 200:
            prediction_result = response.json()
            classification = prediction_result['classification']

            # Lógica condicional para cambiar el mensaje basado en la clasificación
            if classification == 0:
                return "Predicción de Clasificación de Propinas: Baja"
            elif classification == 1:
                return "Predicción de Clasificación de Propinas: Media"
            elif classification == 2:
                return "Predicción de Clasificación de Propinas: Alta"
            else:
                return "Predicción: Clasificación desconocida"
        else:
            return f"Error: {response.json().get('error', 'Error desconocido')}"

    return dash.no_update