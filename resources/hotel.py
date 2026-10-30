from flask_restful import Resource, reqparse
from models.hotel import HotelModel
from flask_jwt_extended import jwt_required



class Hoteis(Resource):
    def get(self,id_hotel):
        hotel_encontrado = HotelModel.find_hotel(id_hotel)
        if hotel_encontrado:
                return hotel_encontrado.json(),200
        return { "message": "Hotel not found"}, 404

    @jwt_required()

    def post(self,id_hotel): 
        dados = Hotel.argumentos.parse_args() # Dicionario
        hotel_encontrado = HotelModel.find_hotel(id_hotel)
        if hotel_encontrado:
                return { "message": "Hotel with this id arleady exists"}
        novo_hotel = HotelModel (id_hotel,**dados)
        novo_hotel.save_hotel()
        return novo_hotel.json(), 200
    

    @jwt_required
    def put(self,id_hotel): 
            dados = Hotel.argumentos.parse_args() # Dicionario
            hotel_encontrado = HotelModel.find_hotel(id_hotel)
            if hotel_encontrado:
                lista = [dado for dado in dados.value()]
                hotel_atualizado = HotelModel(id_hotel, **dados)
                hotel_atualizado.update_hotel(**dados)
                hotel_atualizado.save.hotel(**dados)
                return hotel_atualizado.json(), 200
            
            novo_hotel = HotelModel (id_hotel,**dados)
            novo_hotel.save_hotel()
            return novo_hotel.json(), 200
    
    @jwt_required
    def delete(self, id_hotel):
        hotel_encontrado = HotelModel.find_hotel(id_hotel)
        if hotel_encontrado:
            hotel_encontrado.delete_hotel() 
            return { "message": f"Hotel with id {id_hotel} deleted"}
        return{"message":"hotel not found"},404