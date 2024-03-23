import os
import xmlrpc.client


url = '<insert server URL>'
db = '<insert database name>'
username = 'admin'
password = os.getenv('API_KEY')

# login endpoint
common = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common')

uid = common.authenticate(db, username, password, {})
print("Logged in as %s (uid: %d)" % (username, uid))

# method call endpoint
models = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object')

# execute_kw()
# param: database, user_id, password/api_key, model_name, method_name, [], kwarg**

is_read_access = models.execute_kw(db, uid, password, 'res.partner', 'check_access_rights', ['read'], {'raise_exception': False})

partner_companies = models.execute_kw(db, uid, password, 'res.partner', 'search', [[('is_company', '=', True)]])
