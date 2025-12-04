def criando_nome (string, index_inicial):
    nome = ""
    if index_inicial == 0:
        j = 0
        letra = string[j]
        while letra != " ":
            letra = string[j]
            if letra != " ":
                nome += string[j]
                j += 1
        return nome
    else:
        nome_inverso = ""
        j = len(string) - 1
        letra = string[j]
        while letra != " ":
            letra = string[j]
            if letra != " ":
                nome_inverso += letra
                j -= 1

        nome_str = ""
        k = len(nome_inverso) - 1
        while k >= 0:
            nome_str += nome_inverso[k]
            k -= 1
        return nome_str
        

print(criando_nome("Sabrina Carpenter", -1))

def criando_nome_sem_listas(string_completa, index_inicial):
    string_limpa = string_completa.strip()
    
    nome_str = ""

    if index_inicial == 0:
        
        j = 0 
        
        while j < len(string_limpa) and string_limpa[j] != " ":

            nome_str += string_limpa[j]
            j += 1
            
        return nome_str

    elif index_inicial == -1:

        nome_inverso = ""
        
        j = len(string_limpa) - 1
        
        while j >= 0 and string_limpa[j] != " ":

            nome_inverso += string_limpa[j]
            j -= 1
            
        tamanho_inverso = len(nome_inverso)

        nome_str = ""
        
        k = tamanho_inverso - 1
        while k >= 0:
            nome_str += nome_inverso[k]
            k -= 1
            
        return nome_str
    