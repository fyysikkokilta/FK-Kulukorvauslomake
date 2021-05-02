'''Module containing database models'''

import os
from pony.orm import Database, db_session, perm

DB = Database()

# pylint: disable=C0413
from .users import Users
from .receipt import Receipt
from .explanation import Explanation
from .cost_reimbursement import CostReimbursement
from .travel_reimbursement import TravelReimbursement

# pylint: enable=C0413

if os.environ.get('KULU_ENV') == 'production':
    raise Exception
else:
    DB.bind(
        provider='postgres',
        user=os.environ['PG_USER'],
        password=os.environ['PG_PASSWORD'],
        database=os.environ['PG_USER'],
        host=os.environ['PG_HOST'],
    )

DB.generate_mapping(create_tables=True)
