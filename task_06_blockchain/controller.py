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
    """Get blockchain route
    """

    chain_data = []
    for block in blockchain.chain:
        chain_data.append(block.__dict__)

    data = json.dumps({"length": len(chain_data),
                       "chain": chain_data})

    return templates.TemplateResponse('chain.html', {'request': request, 'data': data})


@app.post('/new_transaction', response_class=HTMLResponse)
def new_transaction(request: Request, sender: str = Form(...), recipient: str = Form(...), amount: str = Form(...)):
    """New transaction post

    :param sender: Person sending the money
    :param recipient: Person getting the money
    :param amount: Amount of money sent
    """

    transaction = {
        'sender': sender,
        'recipient': recipient,
        'amount': amount
    }

    blockchain.add_new_transaction(transaction)
    return templates.TemplateResponse('new_transaction.html', {'request': request, 'last_block': blockchain.last_block})


@app.get('/new_transaction')
def get_new_transaction(request: Request):
    """New transaction route
    """

    return templates.TemplateResponse('new_transaction.html', {'request': request})


@app.get('/mine', response_class=HTMLResponse)
def mine(request: Request):
    """Mining route (mining happens when routing)
    """

    ret = blockchain.mine()

    last_index = blockchain.last_block.index

    if not ret:
        ret = 'No blocks mined :('
    else:
        ret = 'Blocks mined! :D'

    return templates.TemplateResponse('mine.html',
                                      {'request': request, 'nr_of_mined': ret, 'index_of_last': last_index})


@app.get('/')
def home(request: Request):
    """Home page route
    """

    return templates.TemplateResponse('home.html', {'request': request})


# run server
asyncio.run(serve(app, Config()))
