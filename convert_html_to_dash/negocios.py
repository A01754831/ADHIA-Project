html.Div(
    className="bg-gray-50",
    children=[
        html.Main(
            className="mx-auto px-4 py-10 max-w-7xl min-h-screen text-gray-700",
            children=[
                html.Section(
                    className="flex flex-col bg-white shadow-lg p-6 rounded-lg",
                    children=[
                        html.Div(className="flex justify-end mb-4"),
                        html.Div(
                            className="text-center",
                            children=[
                                html.H2(
                                    className="mb-4 font-bold text-6xl",
                                    children=["Restaurante"],
                                )
                            ],
                        ),
                        html.P(
                            className="mb-4 text-justify",
                            children=[
                                """
                                Lorem ipsum dolor sit amet consectetur adipisicing elit. Minus obcaecati assumenda fugit corporis exercitationem mollitia, quibusdam delectus, modi asperiores explicabo vel dolores adipisci maxime, placeat tenetur culpa vero est ullam?
                                Eligendi eius illum alias et, blanditiis sunt beatae praesentium porro reprehenderit, voluptate laborum explicabo delectus odit quasi repudiandae aliquid a, consequatur saepe fugiat inventore? Ratione veniam dolore sed! Sed, recusandae.
                                Suscipit cum quibusdam culpa nihil odit praesentium quia animi numquam, nulla quis eaque voluptatibus repellat porro, magni mollitia rem ipsam! Delectus cum non libero corrupti reiciendis officia optio eos ipsa.
                                Voluptatibus amet possimus ducimus in dolorem sunt ex maxime, libero, qui culpa id rerum quam. Doloribus, deleniti dignissimos. Doloribus illo odit pariatur reprehenderit voluptates. Beatae dolorem quasi praesentium impedit provident.
                                Hic repellendus iste cupiditate. Totam commodi quod veniam, earum asperiores velit obcaecati libero quos consequuntur sed ad eius nostrum officia exercitationem quia. Eligendi ratione eaque iste delectus praesentium, ad quas?
                                """
                            ],
                        ),
                        html.H1(children=["Restaurantes con los que trabajamos"]),
                        html.Ul(
                            children=[
                                html.Li(
                                    children=[
                                        html.H2(children=["Restaurante La Parrilla"]),
                                        html.P(
                                            children=[
                                                "Cocina tradicional argentina. Especialidades en carnes a la parrilla."
                                            ]
                                        ),
                                        html.Img(
                                            src="./images/La_Parrilla_Mexican_Restaurant_logo_.jpg",
                                            alt="Imagen del Restaurante La Parrilla",
                                        ),
                                    ]
                                ),
                                html.Li(
                                    children=[
                                        html.H2(children=["Pizzeria Roma"]),
                                        html.P(
                                            children=[
                                                "Las mejores pizzas napolitanas de la ciudad. Masa artesanal y ingredientes frescos."
                                            ]
                                        ),
                                        html.Img(
                                            src="./images/pizzaroma_4x.jpg",
                                            alt="Imagen de la Pizzeria Roma",
                                        ),
                                    ]
                                ),
                                html.Li(
                                    children=[
                                        html.H2(children=["Sushi Bar Tokio"]),
                                        html.P(
                                            children=[
                                                "Auténtica cocina japonesa. Sushi fresco y variado."
                                            ]
                                        ),
                                        html.Img(
                                            src="./images/logo-tokyosushibar-01.jpg",
                                            alt="alt=",
                                        ),
                                    ]
                                ),
                            ]
                        ),
                    ],
                )
            ],
        )
    ],
)
