'''Module for test data generation'''
from pony.orm import db_session, select
import faker
import random
from kuluserver.models import Users
from . import UserService, ReimbursementService

user_service = UserService()
reimbursement_service = ReimbursementService()

FAKE = faker.Faker('fi_FI')


def gen():
    '''Generate test data'''
    user_service.register(email='swat@fk.fi', password='swat')
    user_service.register(email='user@fk.fi', password='user')

    with db_session():
        user = User.get(email='swat@fk.fi')
        user.groups = 'user admin'

    for _ in range(10):
        reimbursement_service.add(
            'travel',
            {
                'name': FAKE.name(),
                'iban': FAKE.iban(),
                'description': FAKE.text(),
                'licenseNumber': FAKE.license_plate(),
                'passengers': f'{FAKE.name()}, {FAKE.name()}, {FAKE.name()}',
                'route': f'{FAKE.city()} - {FAKE.city()} - {FAKE.city()}',
                'distance': 40 * random.random(),
            },
        )
        reimbursement_service.add(
            'cost',
            {
                'name': FAKE.name(),
                'iban': FAKE.iban(),
                'description': FAKE.text(),
                'receipts': [
                    # { 'original_name': FAKE.word() },
                    # { 'original_name': FAKE.word() },
                ],
                'explanations': [
                    {
                        'explanation': FAKE.text(max_nb_chars=50),
                        'amount': 30 * random.random(),
                    },
                    {
                        'explanation': FAKE.text(max_nb_chars=50),
                        'amount': 30 * random.random(),
                    },
                    {
                        'explanation': FAKE.text(max_nb_chars=50),
                        'amount': 30 * random.random(),
                    },
                ],
            },
        )


def verify():
    '''Verify test data'''
    print('Count of Users:', len(user_service.getAll()))
    print(
        'Count of Reimbursements', len(reimbursement_service.getAll()['data'])
    )
