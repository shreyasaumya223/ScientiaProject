from flask_table import Table, Col, LinkCol
 
class Results(Table):
    Name = Col('Name', show=False)
    Designation = Col('Designation', show=False)
    Address = Col('Address', show=False)
    Phone = Col('Phone', show=False)