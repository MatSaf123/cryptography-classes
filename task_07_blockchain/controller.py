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
    message = 'Transaction added!'
    return templates.TemplateResponse('new_transaction.html', {'request': request, 'last_block': blockchain.last_block, 'new_transaction_added_message': message})


@app.get('/new_transaction')
def get_new_transaction(request: Request):
    """New transaction route
    """

    return templates.TemplateResponse('new_transaction.html', {'request': request, 'new_transaction_added_message': ''})


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


@app.get('/block', response_class=HTMLResponse)
def block(request: Request):
    """Get block info page route
    """

    return templates.TemplateResponse('block_info.html', {'request': request, 'block_info': 'Enter block id!'})


@app.post('/block')
def block(request: Request, block_id: str = Form(...)):
    """Get block info page route
    """

    try:
        block_info = ''.join(['Info for block with id ', block_id, ': ', str(blockchain.chain[int(block_id)])])
    except IndexError:
        block_info = ''.join(['No block with id: ', block_id])

    return templates.TemplateResponse('block_info.html', {'request': request, 'block_info': block_info})


# run server
asyncio.run(serve(app, Config()))
