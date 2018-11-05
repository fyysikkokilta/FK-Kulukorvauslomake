'''Module for class representing receipt uploaded by user'''
from uuid import uuid4
from pony import orm
from bottle import abort
from binascii import a2b_base64
from hashlib import sha512
from . import DB

SUPPORTED_FILES = ['pdf', 'png', 'jpeg', 'jpg']

class Receipt(DB.Entity):
    '''Class representing receipt uploaded by user'''
    id = orm.PrimaryKey(str)
    original_name = orm.Required(str)
    reimbursement = orm.Required('CostReimbursement')
    filetype = orm.Required(str)

    @staticmethod
    def create(reimbursement, json):
        if 'content' not in json:
            abort(400, 'Missing content param.')
        header, content = json['content'].split(',')
        data = a2b_base64(content)
        typ = header.split('/')[1].split(';')[0]

        if typ not in SUPPORTED_FILES:
            abort(400, 'Wrong filetype "{}". Supported types are {}.'.format(
                typ, ', '.join(SUPPORTED_FILES)))

        filename = sha512(data).hexdigest() + '.' + typ

        r = Receipt(
            original_name=json['originalName'],
            reimbursement=reimbursement,
            id=filename,
            filetype=typ,
        )

        with open('receipts/' + filename, 'wb') as f:
            f.write(data)

        return r
