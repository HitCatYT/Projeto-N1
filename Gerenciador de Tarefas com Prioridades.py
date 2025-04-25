filmes = []

def cadastrar_filme():
    titulo = input("Título do filme: ").strip().title()
    genero = input("Gênero: ").strip().title()

    try:
        ano = int(input("Ano de lançamento: "))
    except ValueError:
        print("Ano inválido.\n")
        return

    filme = {
        "titulo": titulo,
        "genero": genero,
        "ano": ano
    }

    filmes.append(filme)
    print("Filme cadastrado com sucesso!\n")


def listar_filmes():
    if not filmes:
        print("Nenhum filme cadastrado.\n")
        return

    print("\nCatálogo de Filmes:")
    for i, f in enumerate(filmes, 1):
        print(f"{i}. {f['titulo']} ({f['ano']}) - {f['genero']}")
    print()


def buscar_por_titulo():
    termo = input("Título a buscar: ").strip().title()
    encontrados = [f for f in filmes if termo in f["titulo"]]

    if encontrados:
        print("\nFilmes encontrados:")
        for f in encontrados:
            print(f"- {f['titulo']} ({f['ano']}) - {f['genero']}")
    else:
        print("Nenhum filme encontrado com esse título.\n")

    print()


def buscar_por_genero():
    termo = input("Gênero a buscar: ").strip().title()
    encontrados = [f for f in filmes if termo == f["genero"]]

    if encontrados:
        print("\nFilmes encontrados:")
        for f in encontrados:
            print(f"- {f['titulo']} ({f['ano']})")
    else:
        print("Nenhum filme encontrado com esse gênero.\n")

    print()


def menu():
    while True:
        print("1. Cadastrar filme")
        print("2. Listar todos os filmes")
        print("3. Buscar por título")
        print("4. Buscar por gênero")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_filme()
        elif opcao == "2":
            listar_filmes()
        elif opcao == "3":
            buscar_por_titulo()
        elif opcao == "4":
            buscar_por_genero()
        elif opcao == "5":
            print("Encerrando o catálogo.")
            break
        else:
            print("Opção inválida.\n")


if __name__ == "__main__":
    menu()
