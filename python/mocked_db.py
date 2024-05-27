class MockedDb(object):

	associacoes = {
	"duna": ["best seller", "ficção",  "religioso", "promoção"]
	}

	def busca_associacoes_existentes(self, livro):
		return self.associacoes[livro]
	
	def cria_associacoes(self, livro, tags_para_associar):
		self.associacoes[livro].extend(tags_para_associar)

	def deleta_associacoes(self, livro, tags_para_deletar):
		associacoes_livro = self.associacoes[livro]
		self.associacoes[livro] = [tag for tag in associacoes_livro if tag not in tags_para_deletar]
