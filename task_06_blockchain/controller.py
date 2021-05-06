import json

from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates

import asyncio
from hypercorn.config import Config
from hypercorn.asyncio import serve
from starlette.responses import HTMLResponse

from blockchain import Blockchain

app = FastAPI()
templates = Jinja2Templates(directory='templates')

blockchain = Blockchain()


@app.get('/chain', response_class=HTMLResponse)
def chain(request: Request):

    chain_data = []
    for block in blockchain.chain:
        chain_data.append(block.__dict__)

    data = json.dumps({"length": len(chain_data),
                       "chain": chain_data})

    return templates.TemplateResponse('chain.html', {'request': request, 'data': data})


@app.post('/new_transaction', response_class=HTMLResponse)
def new_transaction(request: Request, sender: str = Form(...), recipient: str = Form(...), amount: str = Form(...)):

    transaction = {
        'sender': sender,
        'recipient': recipient,
        'amount': amount
    }

    blockchain.add_new_transaction(transaction)
    return templates.TemplateResponse('new_transaction.html', {'request': request, 'last_block': blockchain.last_block})


@app.get('/new_transaction')
def get_new_transaction(request: Request):
    return templates.TemplateResponse('new_transaction.html', {'request': request})


@app.get('/mine', response_class=HTMLResponse)
def mine(request: Request):
    ret = blockchain.mine()

    if not ret:
        ret = 'Nothing to mine.'
    return templates.TemplateResponse('mine.html', {'request': request, 'new_block_index': ret})


@app.get('/')
def home(request: Request):
    return templates.TemplateResponse('home.html', {'request': request})


# run server
asyncio.run(serve(app, Config()))
