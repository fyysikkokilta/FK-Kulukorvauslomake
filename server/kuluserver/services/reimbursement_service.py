from pony import orm
from pony.orm import serialization

from bottle import abort
from datetime import date

from kuluserver.models import TravelReimbursement, CostReimbursement
from kuluserver.models.reimbursement import Reimbursement

class ReimbursementService:
    @orm.db_session
    def get(self, uuid):
        r = Reimbursement.get(id=uuid)
        if not r:
            abort(404, 'Not found.')
        return r.dictify()

    @orm.db_session
    def getAll(self, reimbursement_type=None, name=None, applied_after=None,
            applied_before=None, status=None):
        if not reimbursement_type:
            query = orm.select(r for r in Reimbursement)
        else:
            query = {
                'travel': lambda: orm.select(r for r in TravelReimbursement),
                'cost': lambda: orm.select(r for r in CostReimbursement),
            }[reimbursement_type]()

        if name:
            query = query.filter(lambda r: name.lower() in r.name.lower())
        if status:
            query = query.filter(lambda r: r.status == status)
        if applied_after:
            query = query.filter(lambda r: r.applied > date.fromisoformat(applied_after))
        if applied_before:
            query = query.filter(lambda r: r.applied < date.fromisoformat(applied_before))

        return [r.dictify() for r in query[:]]

    @orm.db_session
    def add(self, reimbursement_type, json):
        # Apparently only creating new instance within db_session saves it
        return {
            'travel': TravelReimbursement.create,
            'cost': CostReimbursement.create,
        }[reimbursement_type](**json).dictify()

    @orm.db_session
    def edit(self, uuid, json):
        r = Reimbursement.get(id=uuid)
        r.edit(**json)

        return r.dictify()
