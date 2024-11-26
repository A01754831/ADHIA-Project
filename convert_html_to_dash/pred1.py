html.Div(
    children=[
        html.Meta(charSet="UTF-8"),
        html.Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
        html.Title(children=["TipOn"]),
        html.Script(src="https://cdn.tailwindcss.com"),
        html.Nav(
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
                                    src="/images/logoTipOn.png",
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
                            href="/index.html",
                            className="hover:text-blue-200 hover:underline",
                            children=["Inicio"],
                        ),
                        html.A(
                            href="/negocios.html",
                            className="hover:text-blue-200 hover:underline",
                            children=["Negocios"],
                        ),
                        html.A(
                            href="/dashboard.html",
                            className="hover:text-blue-200 hover:underline",
                            children=["Dashboard"],
                        ),
                        html.A(
                            href="/prediccion.html",
                            className="hover:text-blue-200 hover:underline",
                            children=["Predicción"],
                        ),
                    ],
                ),
            ],
        ),
        html.Main(
            className="mx-auto px-4 py-10 max-w-7xl min-h-screen text-gray-700",
            children=[
                html.Section(
                    className="flex flex-col bg-white shadow-lg mb-10 p-6 rounded-lg text-gray-700",
                    children=[
                        html.H2(
                            className="mb-4 font-semibold text-4xl",
                            children=["Predicción para un restaurante"],
                        ),
                        html.Form(
                            action="3",
                            method="post",
                            className="space-y-6",
                            children=[
                                html.Div(
                                    children=[
                                        html.Label(
                                            className="block font-medium text-gray-700 text-lg",
                                            children=["Número de estrellas"],
                                        )
                                    ]
                                ),
                                html.Div(
                                    children=[
                                        html.Label(
                                            className="block font-medium text-gray-700 text-lg",
                                            children=["Cuenta total"],
                                        )
                                    ]
                                ),
                                html.Div(
                                    children=[
                                        html.Label(
                                            className="block font-medium text-gray-700 text-lg",
                                            children=["Wi-Fi"],
                                        ),
                                        html.Div(
                                            className="flex items-center space-x-4",
                                            children=[
                                                html.Div(
                                                    children=[
                                                        html.Label(
                                                            className="ml-2 text-gray-700",
                                                            children=["Sí"],
                                                        )
                                                    ]
                                                ),
                                                html.Div(
                                                    children=[
                                                        html.Label(
                                                            className="ml-2 text-gray-700",
                                                            children=["No"],
                                                        )
                                                    ]
                                                ),
                                            ],
                                        ),
                                    ]
                                ),
                                html.Div(
                                    children=[
                                        html.Label(
                                            className="block font-medium text-gray-700 text-lg",
                                            children=["Alcohol"],
                                        ),
                                        html.Div(
                                            className="flex items-center space-x-4",
                                            children=[
                                                html.Div(
                                                    children=[
                                                        html.Label(
                                                            className="ml-2 text-gray-700",
                                                            children=["Sí"],
                                                        )
                                                    ]
                                                ),
                                                html.Div(
                                                    children=[
                                                        html.Label(
                                                            className="ml-2 text-gray-700",
                                                            children=["No"],
                                                        )
                                                    ]
                                                ),
                                            ],
                                        ),
                                    ]
                                ),
                                html.Div(
                                    children=[
                                        html.Label(
                                            className="block font-medium text-gray-700 text-lg",
                                            children=["Valet Parking"],
                                        ),
                                        html.Div(
                                            className="flex items-center space-x-4",
                                            children=[
                                                html.Div(
                                                    children=[
                                                        html.Label(
                                                            className="ml-2 text-gray-700",
                                                            children=["Sí"],
                                                        )
                                                    ]
                                                ),
                                                html.Div(
                                                    children=[
                                                        html.Label(
                                                            className="ml-2 text-gray-700",
                                                            children=["No"],
                                                        )
                                                    ]
                                                ),
                                            ],
                                        ),
                                    ]
                                ),
                                html.Div(
                                    className="flex justify-center",
                                    children=[
                                        html.Button(
                                            type="submit",
                                            className="inline-block bg-gradient-to-br from-teal-400 hover:from-pink-300 to-blue-500 hover:to-orange-600 shadow-lg px-6 py-3 rounded-lg font-semibold text-white",
                                            children=["Enviar"],
                                        )
                                    ],
                                ),
                            ],
                        ),
                    ],
                )
            ],
        ),
        html.Footer(
            className="bg-gray-600 py-10 text-center text-white md:text-lg",
            children=[
                html.P(children=["© 2024 TipOn. Todos los derechos reservados."])
            ],
        ),
    ]
)
