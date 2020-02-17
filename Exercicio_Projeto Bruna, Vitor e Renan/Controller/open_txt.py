from flask_restful import Resource
from Dao.Dao_txt import AmigoDao


class ControllerAmigo(Resource):
	def __init__(self):
		self.dao = AmigoDao()

	def get(self):

		return self.dao.get_txt()