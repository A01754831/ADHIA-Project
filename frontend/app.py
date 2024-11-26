import dash
import dash_svg
from dash import html, dcc, callback, Input, Output, State
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os

# Cargar variables de entorno
load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")
tavily_key = os.getenv("TAVILY_API_KEY")

# Verificar si las claves se cargaron correctamente
if not openai_key or not tavily_key:
    raise EnvironmentError("Las claves de API no se cargaron correctamente. Verifica tu archivo .env")

if not openai_key or not tavily_key:
    raise EnvironmentError("Las claves de API no se cargaron correctamente. Verifica tu archivo .env")


# Inicializa el modelo de OpenAI

"""
llm = ChatOpenAI(
    model="gpt-4",
    temperature=0.7,
    openai_api_key=os.getenv("OPENAI_API_KEY")  # Asegúrate de setear tu clave aquí
)
"""

router_llm = ChatOpenAI(api_key=openai_key,
    model="gpt-3.5-turbo",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,

)

external_stylesheets = []
external_scripts = [
    {"src": "https://cdn.tailwindcss.com"}
]

app = dash.Dash(__name__, 
                external_stylesheets=external_stylesheets, 
                external_scripts=external_scripts, use_pages=True,
                title="TipOn", 
                update_title="Cargando...",
                suppress_callback_exceptions=True)

nav = html.Nav(
    className="flex md:flex-row flex-col justify-between items-center bg-gradient-to-b from-cyan-500 to-blue-600 px-6 py-8",
    children=[
        html.Div(
            className="flex",
            children=[
                html.A(
                    href="/index.html",
                    children=[
                        html.Img(
                            className="w-52",
                            src=dash.get_asset_url("images/logoTipOn.png"), #"/images/logoTipOn.png",
                            alt="Logo de TipOn",
                        )
                    ],
                )
            ],
        ),
        html.Div(
            className="flex space-x-4 font-semibold text-white text-xl",
            children=[
                html.A(
                    href="/",
                    className="hover:text-blue-200 hover:underline",
                    children=["Inicio"],
                ),
                html.A(
                    href="/negocios",
                    className="hover:text-blue-200 hover:underline",
                    children=["Negocios"],
                ),
                html.A(
                    href="/dashboard",
                    className="hover:text-blue-200 hover:underline",
                    children=["Dashboard"],
                ),
                html.A(
                    href="prediccion",
                    className="hover:text-blue-200 hover:underline",
                    children=["Predicción"],
                ),
            ],
        ),
    ],
)



footer = html.Footer(
    className="bg-gray-600 py-10 text-center text-white md:text-lg",
    children=[html.P(children=["© 2024 TipOn. Todos los derechos reservados."])],
)

chat_button = html.Div(
    id="chat-button-container",
    children=[
        html.Button(
            id="chat-button",
            className="fixed bottom-5 left-5 cursor-pointer rounded-full bg-gradient-to-br from-sky-300 to-blue-500 p-3 text-white shadow-lg hover:shadow-gray-700",
            children=[
                dash_svg.Svg(
                    xmlns="http://www.w3.org/2000/svg",
                    fill="none",
                    viewBox="0 0 24 24",
                    stroke="currentColor",
                    className="inline h-14 w-14",
                    children=[
                        dash_svg.Path(
                            strokeLinecap="round",
                            strokeLinejoin="round",
                            d="M7.5 8.25h9m-9 3H12m-9.75 1.51c0 1.6 1.123 2.994 2.707 3.227 1.129.166 2.27.293 3.423.379.35.026.67.21.865.501L12 21l2.755-4.133a1.14 1.14 0 0 1 .865-.501 48.172 48.172 0 0 0 3.423-.379c1.584-.233 2.707-1.626 2.707-3.228V6.741c0-1.602-1.123-2.995-2.707-3.228A48.394 48.394 0 0 0 12 3c-2.392 0-4.744.175-7.043.513C3.373 3.746 2.25 5.14 2.25 6.741v6.018Z",
                        )
                    ],
                )
            ],
        )
    ]
)

chat_window = html.Div(
    id="chat-window-container",
    className="hidden",
    children=[
        html.Div(
            className="fixed bottom-5 left-5 z-10 flex h-[36rem] w-96 flex-col rounded-lg border-2 bg-white text-gray-700 shadow-xl",
            children=[
                html.Div(
                    className="flex justify-between rounded-t-lg p-4",
                    children=[
                        html.Div(
                            children=[
                                html.H4(
                                    className="inline-block text-xl font-semibold",
                                    children=["Asistente virtual"],
                                ),
                                dash_svg.Svg(
                                    xmlns="http://www.w3.org/2000/svg",
                                    fill="none",
                                    viewBox="0 0 24 24",
                                    stroke="currentColor",
                                    className="-mt-6 inline h-8 w-8",
                                    children=[
                                        dash_svg.Path(
                                            strokeLinecap="round",
                                            strokeLinejoin="round",
                                            d="M8.625 9.75a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Zm0 0H8.25m4.125 0a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Zm0 0H12m4.125 0a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Zm0 0h-.375m-13.5 3.01c0 1.6 1.123 2.994 2.707 3.227 1.087.16 2.185.283 3.293.369V21l4.184-4.183a1.14 1.14 0 0 1 .778-.332 48.294 48.294 0 0 0 5.83-.498c1.585-.233 2.708-1.626 2.708-3.228V6.741c0-1.602-1.123-2.995-2.707-3.228A48.394 48.394 0 0 0 12 3c-2.392 0-4.744.175-7.043.513C3.373 3.746 2.25 5.14 2.25 6.741v6.018Z",
                                        )
                                    ],
                                ),
                            ]
                        ),
                        html.Button(
                            id="close-chat-button",
                            children=[
                                dash_svg.Svg(
                                    xmlns="http://www.w3.org/2000/svg",
                                    viewBox="0 0 24 24",
                                    fill="currentColor",
                                    className="inline h-8 w-8 rounded-full text-red-600 shadow-lg",
                                    children=[
                                        dash_svg.Path(
                                            fillRule="evenodd",
                                            d="M12 2.25c-5.385 0-9.75 4.365-9.75 9.75s4.365 9.75 9.75 9.75 9.75-4.365 9.75-9.75S17.385 2.25 12 2.25Zm-1.72 6.97a.75.75 0 1 0-1.06 1.06L10.94 12l-1.72 1.72a.75.75 0 1 0 1.06 1.06L12 13.06l1.72 1.72a.75.75 0 1 0 1.06-1.06L13.06 12l1.72-1.72a.75.75 0 1 0-1.06-1.06L12 10.94l-1.72-1.72Z",
                                            clipRule="evenodd",
                                        )
                                    ],
                                )
                            ]
                        ),
                    ],
                ),
                html.Div(
                    className="space-y-4 overflow-y-auto p-6",
                    children=[
                        dcc.Loading(
                            type="circle",
                            children=[html.Div(id="chat-history")]
                        )
                    ]
                ),
                html.Div(
                    className="rounded-b-lg p-4",
                    children=[
                        dcc.Input(
                            id="chat-input",
                            type="text",
                            className="w-full p-2 border-2 border-gray-300 rounded-lg",
                            placeholder="Escribe un mensaje...",
                            ),
                        ]
                    ),
                ],
            )
        ]
    )


app.layout = html.Div(children=[
    nav,
    chat_button,
    chat_window,
    dash.page_container,
    footer
])

@callback(
    Output("chat-window-container", "className",allow_duplicate=True),
    Output("chat-button-container", "className",allow_duplicate=True),
    Input("chat-button", "n_clicks"),
    prevent_initial_call=True
)
def open_chat_window(n_clicks):
    return "", "hidden"

@callback(
    Output("chat-history", "children"),
    Input("chat-input", "n_submit"),
    State("chat-input", "value"),
    State("chat-history", "children"),
    prevent_initial_call=True
)
def update_chat(n_submit, user_input, chat_history):
    if not user_input:
        raise dash.exceptions.PreventUpdate  # Previene si el input está vacío
    
    # Agrega el mensaje del usuario al historial
    user_message = html.Div(children=[html.P(f"Tú: {user_input}")])
    
    chat_history = chat_history or []
    chat_history.append(user_message)

    # Invoke the OpenAI model
    ai_response = router_llm.invoke([("user", user_input)])
    ai_message = html.Div(children=[html.P(f"Asistente: {ai_response.content}")])
    chat_history.append(ai_message)

    return chat_history

@callback(
    Output("chat-window-container", "className",allow_duplicate=True),
    Output("chat-button-container", "className",allow_duplicate=True),
    Input("close-chat-button", "n_clicks"),
    prevent_initial_call=True
)
def close_chat_window(n_clicks):
    return "hidden", ""


if __name__ == "__main__":
    app.run(debug=True)