class ModelAmigo:
	def __init__(self, dado_txt):
		self.dado_txt = dado_txt
		self.pessoa_envia_id = None
		self.pessoa_aceite_id = None
		self.data_envio_convite = None
		self.data_aceite_convite = None
		self.data_recuse_convite = None


	def tratar_dados(self):
		self.pessoa_envia_id = self.dado_txt[0]
		self.pessoa_aceite_id = self.dado_txt[1]
		self.data_envio_convite = self.dado_txt[2]
		self.data_aceite_convite = self.dado_txt[3]
		self.data_recuse_convite = self.dado_txt[4]
		print(self.pessoa_aceite_id)

	def serialize(self):
		return {
				'pessoa_id': self.pessoa_envia_id,
				'pessoa_id_recebe': self.pessoa_aceite_id,
				'data_envio': str(self.data_envio_convite),
				'data_aceite': str(self.data_aceite_convite),
				'data_recuse': str(self.data_recuse_convite)
				}
