def atualiza_tags_associadas_com_for(livro, tags, database):
    #Transforma os valores informados pelo usuário em um conjunto para excluir possiveis duplicatas
    conjunto_tags = []
    for tag in tags:
        if tag not in conjunto_tags:
            conjunto_tags.append(tag)

    #Busca no banco de dados pela associações existentes
    associacoes_existentes = database.busca_associacoes_existentes(livro)

    #Define quais associações devem ser criadas
    associacoes_para_criar = []
    for tag in tags:
        if tag not in associacoes_existentes:
            associacoes_para_criar.append(tag)

    #Cria as associações no banco de dados
    database.cria_associacoes(livro, associacoes_para_criar)

    #Define quais associações devem ser excluidas
    associacoes_para_deletar = []
    for tag in associacoes_existentes:
        if tag not in tags:
            associacoes_para_deletar.append(tag)

    #Exclui as associações no banco de dados
    database.deleta_associacoes(livro, associacoes_para_deletar)

    #Retorna o resultado da operação
    return database.busca_associacoes_existentes(livro)
