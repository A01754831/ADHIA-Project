html.Div(
    className="bg-gray-100",
    children=[
        html.Main(
            className="mx-auto px-4 py-10 max-w-7xl min-h-screen",
            children=[
                html.Section(
                    className="flex flex-col bg-white shadow-lg p-6 rounded-lg text-gray-700",
                    children=[
                        html.H2(
                            className="mb-4 font-semibold text-4xl",
                            children=[
                                "Análisis descriptivo de variables que más contribuyen a la propina"
                            ],
                        ),
                        html.P(
                            className="text-justify",
                            children=[
                                "En este tablero se muestran las variables que mas contribuyen a la propina"
                            ],
                        ),
                        html.P(
                            className="mb-8 text-justify",
                            children=[
                                "Lorem ipsum dolor sit amet consectetur adipisicing elit. Perferendis delectus quos culpa distinctio minima. Doloribus, vitae. Autem debitis ipsam aspernatur ipsa quo, ducimus ullam nobis praesentium dolores dolor, reprehenderit laudantium?"
                            ],
                        ),
                        html.Iframe(
                            className="h-[800px]",
                            src="https://public.tableau.com/views/exploracion_17288854872030/Anlisisexploratorio?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link?:showVizHome=no&:embed=true",
                        ),
                    ],
                )
            ],
        )
    ],
)
