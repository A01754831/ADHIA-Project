html.Div(
    className="bg-gray-100",
    children=[
        html.Main(
            className="mx-auto px-4 py-10 max-w-7xl min-h-screen text-gray-700",
            children=[
                html.Section(
                    className="flex flex-col bg-gray-100 shadow-lg p-6 rounded-lg",
                    children=[
                        html.Div(className="flex justify-end mb-4"),
                        html.Div(
                            className="text-center",
                            children=[
                                html.H2(
                                    className="mb-4 font-bold text-6xl",
                                    children=["Predicciones"],
                                )
                            ],
                        ),
                        html.P(
                            className="mb-8 text-justify",
                            children=[
                                """
                                Lorem ipsum dolor sit amet consectetur adipisicing elit. Minus obcaecati assumenda fugit corporis exercitationem mollitia, quibusdam delectus, modi asperiores explicabo vel dolores adipisci maxime, placeat tenetur culpa vero est ullam?
                                Lorem ipsum dolor sit amet consectetur adipisicing elit. Minus obcaecati assumenda fugit corporis exercitationem mollitia, quibusdam delectus, modi asperiores explicabo vel dolores adipisci maxime, placeat tenetur culpa vero est ullam?
                                """
                            ],
                        ),
                        html.Div(
                            className="bg-gradient-to-r from-blue-300 to-blue-500 px-4 py-6 rounded font-bold text-white",
                            children=[
                                html.P(children=["."]),
                                html.Div(
                                    className="bg-gray-100 p-6 rounded-lg",
                                    children=[
                                        html.Div(
                                            id="chat",
                                            className="bg-white shadow-inner mb-4 p-4 rounded-lg h-80 overflow-y-auto chat-messages",
                                        ),
                                        html.Div(
                                            className="flex items-center space-x-2 chat-input",
                                            children=[
                                                html.Button(
                                                    id="send-button",
                                                    className="flex items-center bg-blue-500 hover:bg-blue-600 px-4 py-2 rounded-lg text-white",
                                                    children=[
                                                        dash_svg.Svg(
                                                            xmlns="http://www.w3.org/2000/svg",
                                                            fill="none",
                                                            viewBox="0 0 24 24",
                                                            stroke="currentColor",
                                                            className="size-6",
                                                            children=[
                                                                dash_svg.Path(
                                                                    strokeLinecap="round",
                                                                    strokeLinejoin="round",
                                                                    d="M6 12 3.269 3.125A59.769 59.769 0 0 1 21.485 12 59.768 59.768 0 0 1 3.27 20.875L5.999 12Zm0 0h7.5",
                                                                )
                                                            ],
                                                        )
                                                    ],
                                                )
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ],
                )
            ],
        )
    ],
)
