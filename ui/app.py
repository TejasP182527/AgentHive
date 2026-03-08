import sys
import os
sys.path.append('../')
import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import requests

from config.conf_settings import API_URL

dash_app = dash.Dash(__name__, title="AgentHive Chat", description="Mobile-style chat interface for AgentHive")

# External stylesheets for better mobile look (optional, but recommended for production)
# dash_app.css.append_css({"external_url": "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"})

dash_app.layout = html.Div([
    html.Div([
        dcc.Input(id='user-id', type='text', placeholder='Enter your user ID...', style={
            'width': '100%', 'padding': '10px', 'border': '1px solid #ccc', 'borderRadius': '5px', 'marginBottom': '10px'
        })
    ], style={'padding': '10px'}),
    
    html.Div([
        html.Div([
            html.H2("AgentHive Chat", style={'margin': '0', 'color': '#333'})
        ], style={
            'backgroundColor': '#f8f9fa', 'padding': '10px', 'borderBottom': '1px solid #e9ecef', 'textAlign': 'center'
        }),        
        html.Div(id='chat-messages', style={
            'flex': '1', 'overflowY': 'auto', 'padding': '10px', 'height': '60vh', 'backgroundColor': '#f0f0f0'
        }),
        
        html.Div([
            dcc.Input(id='query-input', type='text', placeholder='Type your message...', style={
                'flex': '1', 'padding': '10px', 'border': '1px solid #ccc', 'borderRadius': '20px', 'marginRight': '10px'
            }),
            html.Button('Send', id='send-button', n_clicks=0, style={
                'padding': '10px 20px', 'backgroundColor': '#007bff', 'color': 'white', 'border': 'none', 'borderRadius': '20px'
            })
        ], style={'display': 'flex', 'padding': '10px', 'backgroundColor': '#fff', 'borderTop': '1px solid #e9ecef'})
    ], style={'display': 'flex', 'flexDirection': 'column', 'height': '90vh'}),
    
    dcc.Store(id='chat-store', data=[])
], style={'fontFamily': 'Arial, sans-serif', 'height': '100vh', 'margin': '0'})

@dash_app.callback(
    [Output('chat-messages', 'children'), Output('chat-store', 'data'), Output('query-input', 'value')],
    Input('send-button', 'n_clicks'),
    State('user-id', 'value'),
    State('query-input', 'value'),
    State('chat-store', 'data')
)
def update_chat(n_clicks, user_id, query, chat_history):
    if n_clicks > 0 and query and user_id:
        chat_history.append({'sender': 'user', 'text': query})
        
        try:
            response = requests.post(API_URL, json={"user_id": user_id, "query": query})
            if response.status_code == 200:
                agent_response = response.json().get('response', 'No response received.')
            else:
                agent_response = f"Error: Failed to get response. Status code: {response.status_code}"
        except Exception as e:
            agent_response = f"Error: {str(e)}"
        
        chat_history.append({'sender': 'agent', 'text': agent_response})
    
    messages = []
    for msg in chat_history:
        if msg['sender'] == 'user':
            style = {
                'backgroundColor': '#007bff', 'color': 'white', 'alignSelf': 'flex-end', 'margin': '5px', 'padding': '10px',
                'borderRadius': '10px', 'maxWidth': '70%', 'wordWrap': 'break-word'
            }
        else:
            style = {
                'backgroundColor': '#e9ecef', 'color': '#333', 'alignSelf': 'flex-start', 'margin': '5px', 'padding': '10px',
                'borderRadius': '10px', 'maxWidth': '70%', 'wordWrap': 'break-word'
            }
        messages.append(html.Div(msg['text'], style=style))
    
    chat_display = html.Div(messages, style={'display': 'flex', 'flexDirection': 'column'})
    
    return chat_display, chat_history, ''

if __name__ == '__main__':
    dash_app.run(debug=True)