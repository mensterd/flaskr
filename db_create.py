# project/db_create.py

from project import db
from project.models import Adres

# Create the database and the table
db.create_all()


# Insert dummy-data into the table
db.session.add(
    Adres(naam='Dimitrie', adres='Anjelierstraat 15')
)




# Commit the changes
db.session.commit()
