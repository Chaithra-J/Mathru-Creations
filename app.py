from flask import Flask, render_template, request, redirect, jsonify, url_for
from flask import flash, make_response
from flask import session as login_session
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError

from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import DBAPIError


from pprint import pprint
import httplib2
import random
import string
import json
import requests



app = Flask(__name__)

CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']

engine = create_engine('sqlite:///mathru.db',
                       connect_args={'check_same_thread': False})

DBSession = sessionmaker(bind=engine)
session = DBSession()