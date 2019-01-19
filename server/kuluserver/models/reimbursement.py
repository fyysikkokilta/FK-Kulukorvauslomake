from bottle import abort
from uuid import uuid4
from pony import orm
from datetime import date

from . import DB, Explanation

STATUS_PAID = 1
STATUS_OK = 2
STATUS_NOK = 3
STATUS_PENDING = 4


class Reimbursement(DB.Entity):
    id = orm.PrimaryKey(str, default=lambda: str(uuid4()))
    name = orm.Required(str)
    iban = orm.Required(str)
    description = orm.Required(str)
    explanations = orm.Set(Explanation)
    applied = orm.Required(date, default=date.today)
    status = orm.Required(int, default=4)
    processed = orm.Optional(str)
    hidden = orm.Required(bool, default=False)

    def edit(self, status=None, processed=None, hidden=None):
        if (status is None or processed is None) and hidden is None:
            abort(400, 'Invalid arguments.')

        if not status is None and not processed is None:
            if status not in [
                STATUS_PAID,
                STATUS_OK,
                STATUS_NOK,
                STATUS_PENDING,
            ]:
                abort(400, 'Invalid status value.')
            self.status = status
            self.processed = processed

        if not hidden is None:
            self.hidden = hidden

    @property
    def status_text(self):
        return {
            STATUS_PAID: 'Maksettu. Hyväksytty raadin kokouksessa {processed}.',
            STATUS_OK: 'Hyväksytty raadin kokouksessa {processed}.',
            STATUS_NOK: 'Hylätty raadin kokouksessa {processed}.',
            STATUS_PENDING: 'Odottaa käsittelyä.',
        }[self.status].format(processed=self.processed)
