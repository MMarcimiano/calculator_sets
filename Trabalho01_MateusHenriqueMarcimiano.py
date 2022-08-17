# MATEUS HENRIQUE MARCIMIANO BATISTA

# Trabalho consistente na resolução de operações realizadas baseadas nos conjuntos de dados, onde a aplicação irá ler o arquivo txt contendo os dados e exibirá o resultado formatado no console

# Versão final defini as funções antes do código para melhor leitura

# função da formatação de saída conforme solicitado
def formatacao_resultado(tipo, linha1, linha2, fim):
    linha1 = "{" + "".join(map(str, linha1)).strip() + "}"
    linha2 = "{" + "".join(map(str, linha2)).strip() + "}"
    fim = "{" + " ,".join(map(str, fim)).strip() + "}"
    print(tipo + " 1° conjunto " + linha1 + " 2° conjunto " + linha2 + " Resultado: " + fim)


# funções das operações
def modeloUniao(linha1, linha2):
    fim = linha1 + linha2
    tipo = "união"
    formatacao_resultado(tipo, linha1, linha2, fim)
    return fim


def modeloIntersecao(linha1, linha2):
    fim = [value for value in linha1 if value in linha2]
    tipo = "interseção"
    formatacao_resultado(tipo, linha1, linha2, fim)
    return fim


def modoDiferenca(linha1, linha2):
    fim = [value for value in linha1 if value not in linha2]
    tipo = "diferença"
    formatacao_resultado(tipo, linha1, linha2, fim)
    return fim


def modeloCartesiano(linha1, linha2):
    fim = [a + (b) for a in linha1 for b in linha2]
    tipo = "cartesiano"
    formatacao_resultado(tipo, linha1, linha2, fim)
    return fim


# abertura e leitura do arquivo
arquivo_txt = open("tremb.txt", "r")
operacoes = arquivo_txt.readlines()
# jogando dentro de um array
ary = [l.rstrip('\n').split(',') for l in operacoes]
comando_remove_elemt = ary.pop(0)
array_operacoes = []
tam_ary = len(ary)
# lendo as operações
for y in range(0, tam_ary, 3):
    array_operacoes.append(ary[y:y + 3])
# colocando dentro de um dicionário,para manipulação com a chave
chave = {}
for i, il in enumerate(array_operacoes):
    chave[i] = il

# loop da resolução com a leitura, identificação e chamada das seguintes funções correspondentes
for key in chave:
    leituraInicialDaLinha = chave[key][0][0]

    if leituraInicialDaLinha == "U":
        modeloUniao(chave[key][1], chave[key][2])
    elif leituraInicialDaLinha == "D":
        modoDiferenca(chave[key][1], chave[key][2])
    elif leituraInicialDaLinha == "I":
        modeloIntersecao(chave[key][1], chave[key][2])
    elif leituraInicialDaLinha == "C":
        modeloCartesiano(chave[key][1], chave[key][2])



