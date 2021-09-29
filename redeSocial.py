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

    def caminho_entre_usuarios(self, usuario1, usuario2):
        pass