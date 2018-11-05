import kuluserver.services as services
import kuluserver.controllers as controllers
import kuluserver.plugins as plugins

import bottle
bottle.BaseRequest.MEMFILE_MAX = 1024 * 1024

user_service = services.UserService()
reimbursement_service = services.ReimbursementService()
pdf_service = services.PDFService(reimbursement_service)

user_plugin = plugins.UserPlugin(user_service)

bottle.install(user_plugin)

controllers.ReimbursementController(reimbursement_service, pdf_service)
controllers.UserController(user_service)

if __name__ == '__main__':
    bottle.run(debug=True, port=8000, server='auto')
