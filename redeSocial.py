class RedeSocial:
    def __init__(self):
        self.adjacencia = {}
        self.usuarios = {}  # relaciona nome e usuário

    def adiciona(self, usuario, nome):
        self.adjacencia[usuario] = {}
        self.usuarios[usuario] = nome

    def conecta(self, origem, destino, peso):
        self.adjacencia[origem][destino] = peso

    def quantidade_seguidores(self, usuario):
        """
        Retorna quantidade de seguidores do usuário
        """
        contador = 0
        for k, v in self.adjacencia.items():
            for key, value in v.items():
                if key == usuario:
                    contador += 1
        return self.usuarios[usuario], contador

    def quantidade_seguindo(self, usuario):
        """
        Retorna quantidade de usuários que usuário está seguindo
        """
        return self.usuarios[usuario], len(self.adjacencia[usuario])

    def ordena_stories(self, usuario):
        """
        Ordena stories sendo exibido primeiro os melhores amigos em ordem alfabética e
        em seguida amigos em ordem alfabética
        """
        # cria a lista dos stories por usuario
        stories_ordenados = []
        melhores_amigos = []
        usuarios_que_segue = []

        # seleciona "melhores amigos"
        for k, v in self.adjacencia[usuario].items():
            if v == '2':
                melhores_amigos.append(k)

        # seleciona "amigos"
        for k, v in self.adjacencia[usuario].items():
            if v == '1':
                usuarios_que_segue.append(k)

        # ordena em ordem alfabética cada lista e junta as listas
        melhores_amigos = sorted(melhores_amigos)
        usuarios_que_segue = sorted(usuarios_que_segue)

        for item in melhores_amigos:
            stories_ordenados.append(item)

        for item in usuarios_que_segue:
            stories_ordenados.append(item)

        return self.usuarios[usuario], stories_ordenados

    def top_influencers(self, k):
        """
        Retorna os k usuários com mais seguidores
        """

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
        """
        Retorna menor caminho entre dois usuários
        """
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
