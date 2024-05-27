from mocked_db import MockedDb
from caso_usando_for import atualiza_tags_associadas_com_for

database = MockedDb()

print("Tags atuais: ",database.busca_associacoes_existentes("duna"))

resultado = atualiza_tags_associadas_com_for("duna", ["deserto", "frank herbert", "ficção", "jornada do héroi", "best seller", "deserto"], database)
print("Resultado: ",resultado)
