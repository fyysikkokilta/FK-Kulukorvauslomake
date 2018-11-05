'''Module containing database models'''

import os
from pony.orm import Database, db_session, perm

DB = Database()

# pylint: disable=C0413
from .user import User
from .receipt import Receipt
from .explanation import Explanation
from .cost_reimbursement import CostReimbursement
from .travel_reimbursement import TravelReimbursement
# pylint: enable=C0413

if os.environ.get('KULU_ENV') == 'production':
    raise Exception
else:
    DB.bind(provider='sqlite', filename=':memory:')

DB.generate_mapping(create_tables=True)
