from uuid import uuid4
from pony import orm
from datetime import date

from . import DB, Explanation

STATUS_OK = 0
STATUS_NOK = 1
STATUS_PENDING = 2

class Reimbursement(DB.Entity):
    id = orm.PrimaryKey(str, default=lambda: str(uuid4()))
    name = orm.Required(str)
    iban = orm.Required(str)
    description = orm.Required(str)
    explanations = orm.Set(Explanation)
    applied = orm.Required(date, default=date.today)
    status = orm.Required(int, default=2)
    processed = orm.Optional(str)
    hidden = orm.Required(bool, default=False)

    @property
    def status_text(self):
        return {
            0: 'Hyväksytty raadin kokouksessa {}.',
            1: 'Hylätty raadin kokouksessa {}.',
            2: 'Odottaa käsittelyä.',
        }[self.status].format(self.processed)
