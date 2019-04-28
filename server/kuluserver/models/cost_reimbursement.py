'''Module constaining model for cost reimbursements'''
from pony import orm
from pony.orm import serialization

from . import Receipt, Explanation
from .reimbursement import Reimbursement

FORBIDDEN_RECEIPTS_EXPLANATIONS = ['id', 'reimbursement']
FORBIDDEN_REIMBURSEMENT = ['id', 'applied', 'status', 'processed']


class CostReimbursement(Reimbursement):
    '''Class representing cost reimbursements'''

    receipts = orm.Set(Receipt)
    explanations = orm.Set(Explanation)

    @staticmethod
    def create(explanations, receipts, **reimbursement):
        for e in explanations + receipts:
            for k in FORBIDDEN_RECEIPTS_EXPLANATIONS:
                if k in e:
                    del e[k]
        for k in FORBIDDEN_REIMBURSEMENT:
            if k in reimbursement:
                del reimbursement[k]

        c = CostReimbursement(**reimbursement)
        c.explanations = [
            Explanation(**exp, reimbursement=c) for exp in explanations
        ]
        c.receipts = [Receipt.create(c, r) for r in receipts]
        return c

    def dictify(self):
        r_data = serialization.to_dict(self)
        reimbursement = r_data['CostReimbursement'][self.id]
        explanations = r_data['Explanation']
        receipts = r_data.get('Receipt', [])

        reimbursement['receipts'] = [
            receipts[uuid] for uuid in reimbursement['receipts']
        ]
        reimbursement['explanations'] = [
            explanations[uuid] for uuid in reimbursement['explanations']
        ]
        reimbursement['status_text'] = self.status_text
        reimbursement['applied'] = reimbursement['applied'].isoformat()

        reimbursement['amount'] = sum(
            e['amount'] for e in reimbursement['explanations']
        )
        return reimbursement
