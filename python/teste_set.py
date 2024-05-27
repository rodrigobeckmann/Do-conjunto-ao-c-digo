from mocked_db import MockedDb
from caso_usando_set import atualiza_tags_associadas_com_set

database = MockedDb()

print("Tags atuais: ",database.busca_associacoes_existentes("duna"))

resultado = atualiza_tags_associadas_com_set("duna", ["deserto", "frank herbert", "ficção", "jornada do héroi", "best seller", "deserto"], database)
print("Resultado: ",resultado)
