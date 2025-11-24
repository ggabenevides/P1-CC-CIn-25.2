def encontrar_combinacoes(valor_restante, cedulas, indice_cedula, combinacao_atual):
    """
    Função recursiva para encontrar todas as combinações de cédulas que somam valor_restante.
    
    :param valor_restante: O valor que ainda precisa ser atingido.
    :param cedulas: A lista de cédulas disponíveis (deve estar em ordem decrescente).
    :param indice_cedula: O índice da cédula que está sendo considerada na chamada atual.
    :param combinacao_atual: A lista que registra quantas vezes cada cédula foi usada até agora.
    :return: Uma lista de listas, onde cada lista interna é uma combinação válida.
    """
    
    # 🛑 Caso Base 1: Solução Encontrada!
    if valor_restante == 0:
        # Retorna uma lista contendo a combinação atual. Usa uma cópia para evitar mutação.
        return [list(combinacao_atual)]
    
    # 🛑 Caso Base 2: Acabaram as cédulas ou o valor restante é negativo.
    if indice_cedula == len(cedulas) or valor_restante < 0:
        return []

    # ➡️ Opção 1: NÃO usar a cédula atual e passar para a PRÓXIMA cédula.
    # Isso garante que a ordem seja mantida (ex: 100, 50, 20...).
    # Não usar a cédula 100 e tentar cobrir o valor restante usando 50, 20, 10, 5.
    solucoes = encontrar_combinacoes(
        valor_restante, 
        cedulas, 
        indice_cedula + 1, 
        combinacao_atual
    )
    
    # ➡️ Opção 2: TENTAR usar a cédula atual.
    cedula_valor = cedulas[indice_cedula]
    
    if valor_restante >= cedula_valor:
        # Cria uma nova combinação com a cédula atual usada UMA VEZ a mais.
        nova_combinacao = list(combinacao_atual) # Cria uma CÓPIA
        nova_combinacao[indice_cedula] += 1
        
        # Chama a função recursivamente para o valor restante - valor da cédula, 
        # e *mantém* o mesmo indice_cedula para que possamos usar a mesma cédula novamente.
        solucoes_com_cedula_atual = encontrar_combinacoes(
            valor_restante - cedula_valor, 
            cedulas, 
            indice_cedula,  # Mantém o mesmo índice para permitir múltiplas cédulas
            nova_combinacao
        )
        
        # Adiciona as soluções encontradas nesta ramificação ao conjunto de soluções.
        solucoes.extend(solucoes_com_cedula_atual)
        
    return solucoes