def atualiza_tags_associadas_com_set(livro, tags, database):
    #Transforma os valores informados pelo usuário em um conjunto para excluir possiveis duplicatas
    conjunto_tags = set(tags)

    #Busca no banco de dados pela associações existentes
    associacoes_existentes = set(database.busca_associacoes_existentes(livro))

    #Define quais associações devem ser criadas
    associacoes_para_criar = conjunto_tags - associacoes_existentes

    #Cria as associações no banco de dados
    database.cria_associacoes(livro, associacoes_para_criar)

    #Define quais associações devem ser excluidas
    associacoes_para_deletar = associacoes_existentes - conjunto_tags

    #Exclui as associações no banco de dados
    database.deleta_associacoes(livro, associacoes_para_deletar)

    #Retorna o resultado da operação
    return database.busca_associacoes_existentes(livro)
