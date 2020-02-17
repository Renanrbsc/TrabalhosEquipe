from Model.model_txt import ModelAmigo

class AmigoDao:
	def get_txt(self):
		dados_amigo = []
		with open(r'C:\Users\900159\Documents\GitHub\TrabalhosEquipe\Exercicio_Projeto Bruna, Vitor e Renan\Dao\dados_txt_amigo.txt', 'r') as arquivo:
			for dados in arquivo:
				dado_tratado = dados.strip()
				dado_tratado = dado_tratado.split(';')
				Model_txt = ModelAmigo(dado_tratado)
				Model_txt.tratar_dados()
				Model = Model_txt.serialize()
				dados_amigo.append(Model)
		return dados_amigo

