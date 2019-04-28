from pony import orm
from uuid import uuid4

from . import DB

class Explanation(DB.Entity):
    id = orm.PrimaryKey(str, default=lambda: str(uuid4()))
    explanation = orm.Required(str)
    amount = orm.Required(float)
    reimbursement = orm.Required('CostReimbursement')
