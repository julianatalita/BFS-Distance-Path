class GridGrafo():
    def __init__(self, l, c):
        self.matriz = [None] * l
        self.linhas = l
        self.colunas = c
        self.inicio = ''
        self.fila_vertices = Fila()
        self.contador = 0
        self.vertices_explorar = 1
        self.proximos_vertices = 0

    def adicionar(self, lista, posicao):
        linha = [None] * self.colunas
        for x in range(self.colunas):
            no_adicionado = No(int(lista[x]), posicao, x)
            if no_adicionado.num == 2:
                self.inicio = no_adicionado
            linha[x] = no_adicionado
            
        self.matriz[posicao] = linha


    def bfs(self):
        if self.inicio != '':
            self.fila_vertices.adicionar(self.inicio)
            self.inicio.visitado = True

            while self.fila_vertices.tamanho > 0:
                vert = self.fila_vertices.andar()

                achado = self.explorar(vert)
                if achado:
                    return (self.contador)
                self.vertices_explorar -= 1
                if self.vertices_explorar == 0:
                    self.vertices_explorar = self.proximos_vertices
                    self.proximos_vertices = 0
                    self.contador += 1
            
            return ('Labirinto Impossivel')
        
        return ('Labirinto Impossivel')


    def explorar(self, vertice):
        andar_vertical = [-1, 1, 0, 0]
        andar_horizontal = [0, 0, 1, -1]

        for i in range(4):
            linha = vertice.l + andar_vertical[i]
            coluna = vertice.c + andar_horizontal[i]

            if 0 <= linha < self.linhas and 0 <= coluna < self.colunas:
                adjacente = self.matriz[linha][coluna]
                if not adjacente.visitado and adjacente.num != 1:
                    self.fila_vertices.adicionar(adjacente)
                    adjacente.visitado =  True
                    self.proximos_vertices += 1
                    if adjacente.num == 3:
                        self.contador += 1
                        return True
        return False

        
class Fila():
    def __init__(self):
        self.tamanho = 0
        self.primeiro = None
        self.ultimo = None

    def adicionar(self, vertice):
        if self.primeiro == None:
            self.primeiro = vertice
            self.ultimo = vertice
        else:
            self.ultimo.proximo = vertice
            self.ultimo = vertice
        self.tamanho += 1
        
    def andar(self):
        removido = self.primeiro
        if self.primeiro == self.ultimo:
            self.primeiro = None
            self.ultimo = None
        else:
            self.primeiro = self.primeiro.proximo

        self.tamanho -= 1  
        return removido 


class No():
    def __init__(self, num, linha, coluna):
        self.visitado = False
        self.num = int(num)
        self.proximo = None
        self.l = linha
        self.c = coluna

def main():
    linhas, colunas = input().split()
    grafo = GridGrafo(int(linhas), int(colunas))

    l = 0
    while l < int(linhas):
        lista_linha = input().split()
        grafo.adicionar(lista_linha, l)

        l += 1
    print(grafo.bfs())

if __name__ == '__main__':
    main()
