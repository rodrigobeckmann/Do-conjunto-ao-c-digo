from caso_usando_for import atualiza_tags_associadas_com_for
from caso_usando_set import atualiza_tags_associadas_com_set
from mocked_db import MockedDb

database_set = MockedDb()
database_for = MockedDb()

def testa_assercao_set(livro, tags):

	resultado_esperado = list(set(tags))

	resultado_obtido = atualiza_tags_associadas_com_set(livro, tags, database_set)

	if sorted(resultado_obtido) != sorted(resultado_esperado):
		print("ERRO: A função com set não retornou o resultado esperado")
	else:
		print("A função com set retornou o resultado esperado")

def testa_assercao_for(livro, tags):

	resultado_esperado = list(set(tags))

	resultado_obtido = atualiza_tags_associadas_com_for(livro, tags, database_for)

	if sorted(resultado_obtido) != sorted(resultado_esperado):
		print("ERRO: A função com for não retornou o resultado esperado")
	else:
		print("A função com for retornou o resultado esperado")

def testa_todos_casos(livro, tags):
	testa_assercao_set(livro, tags)
	testa_assercao_for(livro, tags)	

testa_todos_casos("duna", ["deserto", "frank herbert", "ficção", "jornada do héroi", "best seller", "deserto"])
