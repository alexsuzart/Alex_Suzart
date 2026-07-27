import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.font_manager import weight_dict


class Analise:
    def __init__(self):
        pass

    # Filtragem de tratamento de dados
    @staticmethod
    def limpeza(limp):
        # encoding = latin1
        df = pd.read_csv(f"{limp}", encoding='latin1')

        # Removendo linha sem valor na coluna sexo
        df_cleaned = df.dropna(subset=['sexo'])

        # Convertendo sexo para numérico valores inválido viram NaN
        df_cleaned['sexo'] = pd.to_numeric(df_cleaned['sexo'], errors='coerce')

        # Subistutuido valores numéricos por categorias
        df_cleaned['sexo'] = df_cleaned['sexo'].replace({1: "Masculino", 2: "Feminino"})

        # Agrupando por sexo e calculando a média da população
        df_grouped = df_cleaned.groupby('sexo')['pop'].mean().reset_index()

        # Exibindo as primeras linhas para conferência
        print(df_cleaned.head(8))
        return df_grouped

    @staticmethod
    def limp(limp):
        # encoding = ISO-8859-1
        df = pd.read_csv(f"{limp}", encoding="ISO-8859-1")

        # Removendo linha sem idade
        df_cleaned = df.dropna(subset=['idade'])

        # Convertendo idade para numérico valores inválidos viram NaN
        df_cleaned['idade'] = pd.to_numeric(df_cleaned['idade'], errors='coerce')

        # Agrupando por idade e calculando a média da população
        df_grouped = df_cleaned.groupby('idade')['pop'].mean().reset_index()

        # Exibindo as primeras linha para conferência
        print(df_cleaned.head(8))
        return df_grouped




class Grafico:
    @staticmethod
    def grafico1(resultado):

        # Criando figuras com tamanho maior para melhor visualização
        plt.figure(figsize=(14,8))
        sns.barplot(data=resultado, x="idade", y="pop", hue="idade", palette="Blues")

        # Titulo e rótulo
        plt.title("Base Populacional por Idade no Brasil\nEm 2025", fontsize=12, weight='bold')
        plt.xlabel('Idade', fontsize=12, weight='bold')
        plt.ylabel('População', fontsize=12)

        # Melhorando a legibilidade
        plt.xticks(rotation=45)
        plt.tight_layout()

        # Salvando o gráfico em arquivo para consulta posterior
        plt.savefig('Grafico1.png')
        plt.show()
        plt.close()


    @staticmethod
    def grafico2(resultado):
        # Criando cores para diferenciar categorias
        cores = ["lightpink", "skyblue"]

        # Criando figuras com tamanho maior para melhor visualização
        plt.subplots(figsize=(10, 5.7))

        # Criando gráfico de pizza com a soma da população por sexo
        # Mostra porcentagem com uma casa décimal
        resultado.groupby("sexo")["pop"].sum().plot(kind='pie', autopct="%1.1f%%", startangle=90, colors=cores)

        # Adicionado titulo ao gráfico
        plt.title("Porcentagem Populacional entre mulher e homem no Brasil\nEm 2025", fontsize=14, weight='bold')

        # Ajustando layout para evitar cortes
        plt.tight_layout()

        # Exibindo legenda
        plt.legend()
        # Salvando o gráfico em arquivo
        plt.savefig('Grafico2.png')
        plt.show()
        plt.close()