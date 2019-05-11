import kuluserver.services as services
import kuluserver.controllers as controllers
import kuluserver.plugins as plugins

import os
import bottle

bottle.BaseRequest.MEMFILE_MAX = 1024 * 1024

print('Populating services...')

user_service = services.UserService()
reimbursement_service = services.ReimbursementService()
pdf_service = services.PDFService(reimbursement_service)

print('Done.')
print('Initiating plugins...')

user_plugin = plugins.UserPlugin(user_service)

bottle.install(user_plugin)

print('Done.')
print('Generating controllers...')

controllers.ReimbursementController(reimbursement_service, pdf_service)
controllers.UserController(user_service)

print('Done.')

if __name__ == '__main__':
    print('Starting server...')
    bottle.run(debug=os.environ['DEBUG'],
               host=None if os.environ['DEBUG'] else '0.0.0.0',
               port=8000,
               server='twisted')
