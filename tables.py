from flask_table import Table, Col, LinkCol
 
class Results(Table):
    user_name = Col('Name', show=False)
    user_designation = Col('Designation', show=False)
    user_address = Col('Address', show=False)
    user_phone = Col('Phone', show=False)