
import time


class Glossario:
    def __init__(self, arquivo):
        self.palavras = []

        with open(arquivo, "r", encoding="utf-8") as texto:
            for linha in texto:
                self.palavras.extend(linha.split())

    def bubble_sort(self, lista):
        for i in range(len(lista)):
            for j in range(0, len(lista) - i - 1):
                if lista[j] > lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
        return lista

    def selection_sort(self, lista):
        for i in range(len(lista)):
            menor = i

            for j in range(i + 1, len(lista)):
                if lista[j] < lista[menor]:
                    menor = j

            lista[i], lista[menor] = lista[menor], lista[i]

        return lista

    def comparar_algoritmos(self):
        resultados = {}

        algoritmos = {
            "Bubble Sort": self.bubble_sort,
            "Selection Sort": self.selection_sort,
            "Sort nativo": lambda lista: sorted(lista)
        }

        for nome, algoritmo in algoritmos.items():
            copia = self.palavras.copy()

            inicio = time.perf_counter()
            ordenadas = algoritmo(copia)
            fim = time.perf_counter()

            resultados[nome] = fim - inicio

            print(f"\n{nome}:")
            print(ordenadas)
            print(f"Tempo: {resultados[nome]:.6f} segundos")

        return resultados

    def salvar_ordenadas(self):
        palavras = self.palavras.copy()
        palavras.sort()

        with open("palavras_ordenadas.txt", "w", encoding="utf-8") as arquivo:
            for palavra in palavras:
                arquivo.write(palavra + "\n")

        print("\nArquivo de palavras ordenadas criado!")


glossario = Glossario("entrada.txt")

print("Palavras lidas:", glossario.palavras)
print("Quantidade de palavras:", len(glossario.palavras))

glossario.comparar_algoritmos()
glossario.salvar_ordenadas()
