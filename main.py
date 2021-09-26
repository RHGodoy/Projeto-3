import redeSocial
import csv


def imprime_quantidade_seguidores(usuario):
    nome, quantidade_seguidores = redeSocial.quantidade_seguidores(usuario='helena42')
    print(f'Seguidores da {nome}: {quantidade_seguidores}')


def imprime_quantidade_seguindo(usuario):
    nome, quantidade_seguindo = redeSocial.quantidade_seguindo(usuario='helena42')
    print(f'Pessoas que {nome}: {quantidade_seguindo}')


def imprime_top_influencers(k=10):
    print(f'Top influences: {redeSocial.top_influencers(k)}')


if __name__ == '__main__':
    redeSocial = redeSocial.RedeSocial()

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
    imprime_top_influencers(k=6)
