import json
import random
import textwrap

import plotly
import plotly.express as px
import plotly.graph_objects as go

bookList = {'Singin’ Swingin’ and Gettin’ Merry like Christmas','The Handmaid’s Tale','The Vanishing Half',
            'Girl, Woman, Other','The Poisonwood Bible','To Kill a Mockingbird','The Song of Achilles','Half of a Yellow Sun',
            'Frankenstein','The Goldfinch','The Colour Purple','Oryx and Crake','The Penelopiad','Regeneration',
            'We Had To Remove This Post','Villette','Dawn','Possession','Nights at the Circus','Cherí','The Outline Trilogy',
            'The Terrible','Magpie','Don’t Look Now: Selected stories','Rule Britannia','The Candy House','Middlemarch','Mr Loverman','Homegoing','The Treatment','A Thousand Ships','When I Hit You','Small Things Like These',
            'After Midnight','The Left Hand of Darkness','The Bluest Eye','The Sea The Sea','My Phantoms','The God of Small Things',
            'Bonjour Tristesse','Gaudy Night','Ten Minutes, 38 Seconds in This Strange World','The Stone Diaries','The Tale of Genji',
            'Great Circle','We Need to Talk About Kevin','The Last Widow','Companion Piece','Reasons to be Cheerful','The Burgess Boys',
            'Olive Kitteridge','Flights','The Secret Diary of Adrian Mole, Aged 13 ¾','The Road Home','Becoming Unbecoming',
            'Today a Woman Went Mad in the Supermarket','Mrs Dalloway','Orlando','How Much of These Hills is Gold','Song of Soloman'}



def generateBookChoices(bookList):
    bookChoicesWrapped = []

    item = random.sample(bookList, k=5)

    for i in item:
        #print(i)
        split_text = textwrap.wrap(i, width=15)
        bookChoicesWrapped.append('<br>'.join(split_text))

    return bookChoicesWrapped



def graphBubbles():
    fig = go.Figure(data=[go.Scatter(
        x=[3.64, 5, 6.35, 4.35,5.75], y=[10, 10, 10, 16.5,16.5],
        mode='markers+text',
        marker_size=150,
        text = generateBookChoices(bookList),
        marker=dict(
            color=['rgb(193, 164, 214)', #middle leftleft
                   'rgb(255, 128, 183)', #middle, pink
                   'rgb(217, 179, 155)', # middle right
                   'rgb(255, 206, 153)', #bottom
                   'rgb(255, 204, 110)']   ) #top
    )
    ])

    fig.update_layout(yaxis=dict(range=[4,25]),
                      xaxis=dict(range=[2.9,7.1]),
                      plot_bgcolor='rgba(0,0,0,0)',
                      width=450, height=350,
                      margin=dict(l=0, r=0, t=0, b=0, pad=0),
                      autosize=False
                     )

    #https://stackoverflow.com/questions/54826436/how-to-remove-axes-and-numbers-from-plotly
    fig.update_xaxes(visible=False)
    fig.update_yaxes(visible=False)

    return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
