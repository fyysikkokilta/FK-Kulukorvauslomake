from .user_service import UserService
from .reimbursement_service import ReimbursementService
from .pdf_service import PDFService

import sys

try:
    args = sys.argv
    if sys.argv[1] == 'test':
        from .test import verify, gen
        gen()
        verify()
except KeyError: 
    pass
