import json
import random
import textwrap

import plotly
import plotly.graph_objects as go


with open("assets/books.json") as books:
    book_list = json.load(books)


def generate_book_choices():
    item = random.sample(book_list, k=5)
    return ["<br>".join(textwrap.wrap(book, width=15)) for book in item]


def graph_bubbles():
    fig = go.Figure(
        data=[
            go.Scatter(
                x=[3.64, 5, 6.35, 4.35, 5.75],
                y=[10, 10, 10, 16.5, 16.5],
                mode="markers+text",
                marker_size=150,
                text=generate_book_choices(),
                marker=dict(
                    color=[
                        "rgb(193, 164, 214)",
                        "rgb(255, 128, 183)",
                        "rgb(217, 179, 155)",
                        "rgb(255, 206, 153)",
                        "rgb(255, 204, 110)",
                    ]
                ),
            )
        ]
    )

    fig.update_layout(
        yaxis=dict(range=[4, 25]),
        xaxis=dict(range=[2.9, 7.1]),
        plot_bgcolor="rgba(0,0,0,0)",
        width=450,
        height=350,
        margin=dict(l=0, r=0, t=0, b=0, pad=0),
        autosize=False,
    )

    fig.update_xaxes(visible=False)
    fig.update_yaxes(visible=False)

    return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
