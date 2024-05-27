from caso_usando_for import atualiza_tags_associadas_com_for
from caso_usando_set import atualiza_tags_associadas_com_set
from mocked_db import MockedDb
import timeit

# Função de teste para o método com for
def teste_for():
    database = MockedDb()
    atualiza_tags_associadas_com_for("duna", ["deserto", "frank herbert", "ficção", "jornada do héroi", "best seller"], database)

# Função de teste para o método com set
def teste_set():
    database = MockedDb()
    atualiza_tags_associadas_com_set("duna", ["deserto", "frank herbert", "ficção", "jornada do héroi", "best seller"], database)

# Medição do tempo de execução para o método com for
tempo_for = timeit.timeit(teste_for, number=1000000)

# Medição do tempo de execução para o método com set
tempo_set = timeit.timeit(teste_set, number=1000000)

print("Tempo com for:", tempo_for)
print("Tempo com set:", tempo_set)