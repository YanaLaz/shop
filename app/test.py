from flask_admin import AdminIndexView
from flask_admin import Admin

admin.add_view(AdminView(User, db.session))
admin.add_view(AdminView(Post, db.session))
admin.add_view(AdminView(Thing, db.session))