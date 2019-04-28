from bottle import request, static_file
import json
import kuluserver.plugins as plugins
from .controller import Controller

class ReimbursementController(Controller):
    def __init__(self, reimbursement_service, pdf_service):
        routes = [
            {
                'path': '/reimbursements',
                'callback': self.get_reimbursements,
                'apply': [
                    plugins.AuthorizationPlugin('user'),
                ],
            },
            {
                'path': '/reimbursements/pdfs',
                'callback': self.get_reimbursement_pdfs,
                'apply': [
                    plugins.AuthorizationPlugin('user'),
                ],
            },
            {
                'path': '/reimbursements/<uuid>',
                'callback': self.get_reimbursement,
                'apply': [
                    plugins.AuthorizationPlugin('user'),
                ],
            },
            {
                'path': '/reimbursements/<uuid>/preview',
                'callback': self.preview_reimbursement_pdf,
                'apply': [
                    plugins.AuthorizationPlugin('user'),
                ],
            },
            {
                'path': '/reimbursements/<uuid>/pdf',
                'callback': self.get_reimbursement_pdf,
                'apply': [
                    plugins.AuthorizationPlugin('user'),
                ],
            },
            {
                'path': '/reimbursements/<reimbursement_type>',
                'method': ['POST'],
                'callback': self.create_reimbursement,
            },
            {
                'path': '/reimbursements/<uuid>',
                'method': ['PUT'],
                'callback': self.edit_reimbursement,
                'apply': [
                    plugins.AuthorizationPlugin('user'),
                ],
            },
        ]
        self._reimbursement_service = reimbursement_service
        self._pdf_service = pdf_service

        super(ReimbursementController, self).__init__(routes)

    def get_reimbursements(self):
        search_params = {
            'name': request.query.get('name'),
            'reimbursement_type': request.query.get('reimbursement_type'),
            'applied_before': request.query.get('applied_before'),
            'applied_after': request.query.get('applied_after'),
            'status': request.query.get('status'),
            'page': request.query.get('page'),
            'count': request.query.get('count'),
            'hidden': request.query.get('hidden'),
        }
        return json.dumps(self._reimbursement_service.getAll(**search_params))

    def get_reimbursement(self, uuid):
        return json.dumps(self._reimbursement_service.get(uuid))

    def create_reimbursement(self, reimbursement_type):
        return json.dumps(
            self._reimbursement_service.add(reimbursement_type, request.json)
        )

    def edit_reimbursement(self, uuid):
        return self._reimbursement_service.edit(uuid, request.json)

    def get_reimbursement_pdf(self, uuid):
        # return self._pdf_service.getPDF(uuid)
        fn = self._pdf_service.getPDF(uuid)
        return static_file(fn, root='rendered', download=fn)

    def preview_reimbursement_pdf(self, uuid):
        fn = self._pdf_service.getPDF(uuid)
        return static_file(fn, root='rendered')

    def get_reimbursement_pdfs(self):
        search_params = {
            'name': request.query.get('name'),
            'reimbursement_type': request.query.get('reimbursement_type'),
            'applied_before': request.query.get('applied_before'),
            'applied_after': request.query.get('applied_after'),
            'status': request.query.get('status'),
            'hidden': request.query.get('hidden'),
        }
        fn = self._pdf_service.getAllPdfs(search_params)
        return static_file(fn, root='rendered', download=fn)
