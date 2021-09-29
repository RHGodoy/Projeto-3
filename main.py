import redeSocial
import csv


def imprime_quantidade_seguidores(usuario):
    nome, quantidade_seguidores = redeSocial.quantidade_seguidores(usuario)
    print(f'Seguidores da {nome}: {quantidade_seguidores}')


def imprime_quantidade_seguindo(usuario):
    nome, quantidade_seguindo = redeSocial.quantidade_seguindo(usuario)
    print(f'Pessoas que {nome} segue: {quantidade_seguindo}')


def imprime_top_influencers(k=10):
    print(f'Top influences: {redeSocial.top_influencers(k)}')


def imprime_stories_ordenados(usuario):
    nome, stories_usuario = redeSocial.ordena_stories(usuario)
    print(f'Ordem dos stories de {nome}: {stories_usuario}')


if __name__ == '__main__':
    redeSocial = redeSocial.RedeSocial()

    # cadastra usuários na rede social
    with open('c:/Users/Márcio Pacheco/Downloads/usuarios.csv') as csv_file:
        csv_read = csv.reader(csv_file, delimiter=',')
        for row in csv_read:
            redeSocial.adiciona(usuario=row[1], nome=row[0])

    # cadastra conexões
    with open('c:/Users/Márcio Pacheco/Downloads/conexoes.csv') as csv_file:
        csv_read = csv.reader(csv_file, delimiter=',')
        for row in csv_read:
            redeSocial.conecta(origem=row[0], destino=row[1], peso=row[2])

    imprime_quantidade_seguidores(usuario='helena42')
    imprime_quantidade_seguindo(usuario='helena42')
    imprime_top_influencers(6)
    imprime_stories_ordenados(usuario = 'helena42')
