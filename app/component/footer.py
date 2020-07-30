# -*- coding: utf-8 -*-
"""
Footer docs:
dbc.Container, dbc.Row, dbc.Col: https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
html.P: https://dash.plot.ly/dash-html-components
fa (font awesome) : https://fontawesome.com/icons/github-square?style=brands
mr (margin right) : https://getbootstrap.com/docs/4.3/utilities/spacing/
className='lead' : https://getbootstrap.com/docs/4.3/content/typography/#lead
"""
import dash_html_components as html
import dash_bootstrap_components as dbc


content = dbc.Container(
    dbc.Row(
        dbc.Col(
            html.P(
                [
                    html.Span("Shahnam Khabiri", className="mr-2"),
                    html.A(
                        html.I(className="fas fa-envelope-square mr-1"),
                        href="mailto:shahnam.khabiri@gmail.com",
                    ),
                    html.A(
                        html.I(className="fab fa-github-square mr-1"),
                        href="https://github.com/skhabiri",
                    ),
                    html.A(
                        html.I(className="fab fa-linkedin mr-1"),
                        href="https://www.linkedin.com/in/brianthomasross/",
                    ),
                    html.A(
                        html.I(className="fab fa-twitter-square mr-1"),
                        href="https://twitter.com/brianthomasross",
                    ),
                ],
                className="lead",
            )
        )
    )
)
