"""
SWORD2 Python Client blurb
"""
from sword2.service_document import ServiceDocument
from sword2.collection import SDCollection, Collection_Feed
from sword2.statement import Atom_Sword_Statement, Ore_Sword_Statement
from sword2.error_document import Error_Document
from sword2.connection import Connection
from sword2.transaction_history import Transaction_History
from sword2.exceptions import *
from sword2.server_errors import SWORD2ERRORSBYIRI, SWORD2ERRORSBYNAME
from sword2.utils import Timer, NS, get_md5, create_multipart_related
from sword2.implementation_info import *
from sword2.atom_objects import Entry, Category
from sword2.http_layer import HttpLayer, HttpResponse, HttpLib2Layer, UrlLib2Layer
from sword2.auto_discovery import AutoDiscovery
from sword2.deposit_receipt import Deposit_Receipt
