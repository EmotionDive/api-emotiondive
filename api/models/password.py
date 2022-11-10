from .. import db, ma
from .user import User

class Password(db.Model):
    """ Password Model to store user's password """
    __tablename__ = "usuario_password"

    username_usuario = db.Column(
        db.String(512), 
        db.ForeignKey('usuario.username'), 
        nullable=False, 
        primary_key=True
    )
    usuario = db.relationship("User", backref=db.backref("usuario", uselist=False))
    user_password = db.Column(db.String(128), nullable=False)

    def __init__(self, username, user_password):
        self.username = username
        self.user_password = user_password
    
class PasswordSchema(ma.Schema):
    class Meta:
        fields = ('username', 'user_password')

password_schema = PasswordSchema()