'''Module for class representing travel reimbursements'''
from pony import orm
from pony.orm import serialization

from . import Explanation
from .reimbursement import Reimbursement

FORBIDDEN_REIMBURSEMENT = ['id', 'applied', 'status', 'processed']

class TravelReimbursement(Reimbursement):
    '''Class representing travel reimbursements'''

    licenseNumber = orm.Required(str)
    passengers = orm.Required(str)
    route = orm.Required(str)
    distance = orm.Required(float)

    @staticmethod
    def create(**reimbursement):
        for k in FORBIDDEN_REIMBURSEMENT:
            if k in reimbursement:
                del reimbursement[k]

        c = TravelReimbursement(**reimbursement)
        return c

    def dictify(self):
        r_data = serialization.to_dict(self)
        reimbursement = r_data['TravelReimbursement'][self.id]

        reimbursement['status_text'] = self.status_text
        reimbursement['applied'] = reimbursement['applied'].isoformat()

        reimbursement['amount'] = 0.25 * self.distance

        return reimbursement
