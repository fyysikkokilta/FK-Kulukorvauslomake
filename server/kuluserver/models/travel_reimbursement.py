'''Module for class representing travel reimbursements'''
from pony import orm
from pony.orm import serialization

from . import Explanation
from .reimbursement import Reimbursement

FORBIDDEN_RECEIPTS_EXPLANATIONS = ['id', 'reimbursement']
FORBIDDEN_REIMBURSEMENT = ['id', 'applied', 'status', 'processed']

class TravelReimbursement(Reimbursement):
    '''Class representing travel reimbursements'''

    @staticmethod
    def create(explanations, **reimbursement):
        for e in explanations:
            for k in FORBIDDEN_RECEIPTS_EXPLANATIONS:
                if k in e:
                    del e[k]
        for k in FORBIDDEN_REIMBURSEMENT:
            if k in reimbursement:
                del reimbursement[k]

        c = TravelReimbursement(**reimbursement)
        c.explanations = [
            Explanation(**exp, reimbursement=c) for exp in explanations
        ]
        return c

    def dictify(self):
        r_data = serialization.to_dict(self)
        reimbursement = r_data['TravelReimbursement'][self.id]
        explanations = r_data['Explanation']

        reimbursement['explanations'] = [
            explanations[uuid] for uuid in reimbursement['explanations']
        ]
        reimbursement['status_text'] = self.status_text
        reimbursement['applied'] = reimbursement['applied'].isoformat()

        reimbursement['amount'] = sum(
            e['amount'] for e in reimbursement['explanations']
        )

        return reimbursement
