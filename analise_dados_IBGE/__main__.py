from limpeza_geracao import *
from rich import print
from rich.panel import Panel
# Caminho "G:\Meu Drive\SPSP2507.csv"


def main():
    while True:
        # Tiratndo erros de entrada
        try:
            # Exibindo menu de opções
            print(Panel("[ 1 ] Gráfico1\n[ 2 ] Gráfico2\n[ 3 ] Sair", title="Opçães de Gráficos", border_style="blue", width=28))

            # Escolha de usuario
            escolha = int(input("Escolha uma opção\n").strip())

        except ValueError:
            print('[red]Valor inválido detectado. Vamos tentar de novo?[/]')

        except KeyboardInterrupt:
            print('[red]Execução interrompida pelo usuário. Encerrando com segurança...[/]')
            break

        else:
            # Instanciando classes
            a = Analise()
            b = Grafico()
            if escolha == 1:
                resultado = (a.limp(r"C:\TAB415\dados\POP25.csv"))
                b.grafico1(resultado)
            elif escolha == 2:
                result = (a.limpeza(r"C:\TAB415\dados\POP25.csv"))
                b.grafico2(result)

            elif escolha == 3:
                print("Sessão encerrada com sucesso!")
                print("Até Breve!")
                break


if __name__ == "__main__":
    main()