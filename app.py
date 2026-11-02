from flask import Flask
from flask_restful import Resource, Api
from resources.hotel import Hoteis, Hotel
from con_sql import bd
from resources.user import user, UserRegister, UserLogin, UserLogout
from flask_jwt_extended import JWTManager
from blocklist import BLOCKLIST

#variavel representar a minha aplicação
app = Flask(__name__)
api = Api(app)
jwt = JWTManager(app)

#configuraçoes
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///hoteis.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = "a_minha_palavra_secreta_para_a_minha_api_vai_ser_forte"
app.config["JWT_BLACKLIST_ENABLED"]= True

@jwt.token_in_blacklist_loader
def verificar_blacklist(jwt_header,jwt_payload):
    jti = jwt_payload["jti"]
    return jti in BLOCKLIST

@jwt.revoked_token_loader
def token_revogado(jwt_header,jwt_payload):
    return{"message": "You have no acess to this resource. Login please"}






# rotas
api.add_resource(Hoteis, "/hoteis")
api.add_resource(Hotel,"/hoteis/<string:id_hotel>")
api.add_resource(user,"/users/<string:username>")
api.add_resource(UserRegister,"/registar/")
api.add_resource(UserLogin,"/login/")
api.add_resource(UserLogout,"/logout/")

if __name__ == "__main__":
    bd.init_app(app)
    with app.app_context():
        bd.create_all()
    app.run(debug=True)