import jinja2
from datetime import date, datetime
from .pdf_util import *
import zipfile
from bottle import abort

class PDFService:
    def __init__(self, reimbursement_service):
        self._reimbursement_service = reimbursement_service

    def getPDF(self, uuid):
        reimbursement = self._reimbursement_service.get(uuid)
        return self.__render_pdf(reimbursement)

    def getAllPdfs(self, search_params):
        reimbursements = self._reimbursement_service.getAll(**search_params)['data']

        if not reimbursements:
            abort(404, 'No reimbursements found.')

        filenames = []
        for r in reimbursements:
            filenames.append(self.__render_pdf(r))

        zipfn = '{}.zip'.format(date.today().strftime('%d-%m-%Y'))
        with zipfile.ZipFile('rendered/' + zipfn, 'w') as zipf:
            for fn in filenames:
                zipf.write('rendered/' + fn)

        return zipfn


    def __render_pdf(self, reimbursement):
        return {
            'CostReimbursement': self.__render_cost_reimbursement,
            'TravelReimbursement': self.__render_travel_reimbursement,
        }[reimbursement['classtype']](reimbursement)

    def __render_cost_reimbursement(self, reimbursement):
        r_esc = esc(reimbursement, exclude=['.applied'])
        applied = date.fromisoformat(r_esc['applied'])
        r_esc['applied'] = applied.strftime('%d.%m.%Y')

        dest = '{}-{}'.format(
            applied.strftime('%Y-%m-%d'), r_esc['name'].replace(' ', '_'))
        return render_tex('cost_template.tex', dest, r_esc)

    def __render_travel_reimbursement(self, reimbursement):
        r_esc = esc(reimbursement, exclude=['.applied'])
        applied = date.fromisoformat(r_esc['applied'])
        r_esc['applied'] = applied.strftime('%d.%m.%Y')

        dest = '{}-{}'.format(
            applied.strftime('%Y-%m-%d'), r_esc['name'].replace(' ', '_'))
        return render_tex('travel_template.tex', dest, r_esc)
