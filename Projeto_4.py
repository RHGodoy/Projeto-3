class RedeSocial:
    def __init__(self):
        self.adjacencia = {}
        self.usuarios = {}

    def adiciona(self, usuario, nome):
        self.adjacencia[usuario] = {}
        self.usuarios[usuario] = nome

    def conecta(self, origem, destino, peso):
        self.adjacencia[origem][destino] = peso

    def exibir_matriz(self):
        primeira_linha = '    '
        for i in self.adjacencia:
            primeira_linha += str(i) + ' '
        print(primeira_linha)
        print('   ' + ('-' * len(primeira_linha)))

        for i in self.adjacencia:
            linha = str(i) + ' | '
            for j in self.adjacencia:
                linha += str(self.adjacencia[i].get(j, 0)) + ' '
            print(linha)

    def quantidade_seguidores(self, usuario):
        contador = 0
        for k, v in self.adjacencia.items():
            for key, value in v.items():
                if key == usuario:
                    contador += 1
        return self.usuarios[usuario], contador

    def quantidade_seguindo(self, usuario):
        return self.usuarios[usuario], len(self.adjacencia[usuario])

    def ordena_stories(self, usuario):
        # cria a lista dos stories por usuario
        stories_ordenados = []
        melhores_amigos = []
        usuarios_que_segue = []

        # seleciona primeiramente os melhores amigos
        for k, v in self.adjacencia[usuario].items():
            if v == '2':
                melhores_amigos.append(k)
        
        # seleciona os demais seguidores:
        for k, v in self.adjacencia[usuario].items():
            if v == '1':
                usuarios_que_segue.append(k)
        
        # organiza as duas listas e adiciona a principal
        melhores_amigos = sorted(melhores_amigos)
        usuarios_que_segue = sorted(usuarios_que_segue)

        for item in melhores_amigos:
            stories_ordenados.append(item)

        for item in usuarios_que_segue:
            stories_ordenados.append(item)

        return self.usuarios[usuario], stories_ordenados

    def top_influencers(self, k):
        # cria dict usuario: número de seguidores
        seguidores_por_usuario = {}
        for key, value in self.adjacencia.items():
            seguidores_por_usuario[key] = self.quantidade_seguidores(key)[1]

        # ordena usuários por número de seguidores
        influencers_sorted = dict(sorted(seguidores_por_usuario.items(), key=lambda x: x[1], reverse=True))

        # retorna dict com top influencers
        top_influencers = {}
        for key in list(influencers_sorted)[0:k]:
            top_influencers[key] = influencers_sorted[key]

        return top_influencers

    def caminho_entre_usuarios(self, origem, destino):
        caminho = {origem: [origem]}
        fila = [origem]
        while len(fila):
            primeiro_elemento = fila[0]
            fila = fila[1:]
            for adjacencia in self.adjacencia[primeiro_elemento]:
                if adjacencia not in caminho:
                    caminho[adjacencia] = [caminho[primeiro_elemento], adjacencia]
                    fila.append(adjacencia)

        return caminho.get(destino)
    
# Aqui começa o Main

import csv


def imprime_quantidade_seguidores(usuario):
    nome, quantidade_seguidores = redeSocial.quantidade_seguidores(usuario='helena42')
    print(f'Seguidores da {nome}: {quantidade_seguidores}')


def imprime_quantidade_seguindo(usuario):
    nome, quantidade_seguindo = redeSocial.quantidade_seguindo(usuario='helena42')
    print(f'Pessoas que {nome} segue: {quantidade_seguindo}')


def imprime_top_influencers(k=10):
    print(f'Top influences: {redeSocial.top_influencers(k)}')

    
def imprime_stories_ordenados(usuario):
    nome, stories_usuario = redeSocial.ordena_stories(usuario)
    print(f'Ordem dos stories de {nome}: {stories_usuario}')


def imprime_caminho_entre_usuarios(origem, destino):
    lista_caminho = redeSocial.caminho_entre_usuarios(origem='helena42', destino='isadora45')
    caminho = []
    while lista_caminho:
        caminho.append(lista_caminho.pop(-1))
        if len(lista_caminho):
            lista_caminho = lista_caminho[0]
    caminho.reverse()
    print(' -> '.join(caminho))    
    

if __name__ == '__main__':                        
    redeSocial = RedeSocial()

    # cadastra usuários na rede social
    with open('usuarios.csv') as csv_file:
        csv_read = csv.reader(csv_file, delimiter=',')
        for row in csv_read:
            redeSocial.adiciona(usuario=row[1], nome=row[0])

    # cadastra conexões
    with open('conexoes.csv') as csv_file:
        csv_read = csv.reader(csv_file, delimiter=',')
        for row in csv_read:
            redeSocial.conecta(origem=row[0], destino=row[1], peso=row[2])

    imprime_quantidade_seguidores(usuario='helena42')
    imprime_quantidade_seguindo(usuario='helena42')
    imprime_top_influencers(6)
    imprime_stories_ordenados(usuario = 'helena42')
    imprime_caminho_entre_usuarios(origem='helena42', destino='isadora45')