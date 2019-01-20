from pony import orm
from pony.orm import serialization, desc

from bottle import abort
from datetime import date

from math import ceil

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
    def getAll(
        self,
        reimbursement_type='all',
        name=None,
        applied_after=None,
        applied_before=None,
        status=None,
        page=0,
        count=None,
    ):
        if reimbursement_type == 'all':
            query = orm.select(r for r in Reimbursement)
        else:
            query = {
                'travel': lambda: orm.select(r for r in TravelReimbursement),
                'cost': lambda: orm.select(r for r in CostReimbursement),
            }[reimbursement_type]()

        query = query.order_by(Reimbursement.applied, Reimbursement.name)

        if name:
            query = query.filter(lambda r: name.lower() in r.name.lower())
        if status and int(status):
            query = query.filter(lambda r: r.status == int(status))
        if applied_after:
            query = query.filter(
                lambda r: r.applied > date.fromisoformat(applied_after)
            )
        if applied_before:
            query = query.filter(
                lambda r: r.applied < date.fromisoformat(applied_before)
            )

        total = query.count()
        if count is not None:
            query = query.page(int(page)+1, int(count))

        return {
            'pages': ceil(total / int(count)) if count else 1,
            'data': [r.dictify() for r in query[:]],
        }

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
