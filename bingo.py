import random
from typing import List, Set


class SorteadorBingo:
    def __init__(self, numero_maximo: int = 75):
        self.numero_maximo = numero_maximo
        self.numeros_disponiveis = list(range(1, numero_maximo + 1))
        self.numeros_sorteados: List[int] = []
        
    def sortear_numero(self) -> int:
        if not self.numeros_disponiveis:
            raise ValueError("Todos os números já foram sorteados!")
        
        numero = random.choice(self.numeros_disponiveis)
        self.numeros_disponiveis.remove(numero)
        self.numeros_sorteados.append(numero)
        
        return numero
    
    def exibir_numero_sorteado(self, numero: int) -> None:
        letra = self.obter_letra_coluna(numero)
        print("\n" + "=" * 40)
        print(f"NÚMERO SORTEADO: {letra}-{numero}")
        print("=" * 40)
        print(f"Total de números sorteados: {len(self.numeros_sorteados)}")
        print(f"Números restantes: {len(self.numeros_disponiveis)}")
        
    def obter_letra_coluna(self, numero: int) -> str:
        if 1 <= numero <= 15:
            return "B"
        elif 16 <= numero <= 30:
            return "I"
        elif 31 <= numero <= 45:
            return "N"
        elif 46 <= numero <= 60:
            return "G"
        elif 61 <= numero <= 75:
            return "O"
        else:
            return "?"
    
    def mostrar_historico(self) -> None:
        if not self.numeros_sorteados:
            print("Nenhum número foi sorteado ainda.")
            return
        
        print("\n HISTÓRICO DE NÚMEROS SORTEADOS:")
        print("-" * 40)
        for i, num in enumerate(self.numeros_sorteados, 1):
            letra = self.obter_letra_coluna(num)
            print(f"{i}. {letra}-{num}", end="  ")
            if i % 5 == 0:
                print()
        print("\n")


class CartelaBingo:
    
    def __init__(self):
        """Inicializa uma nova cartela com números aleatórios."""
        self.numeros = self._gerar_cartela()
        self.marcados: Set[int] = set()
        self.espaco_livre = True
        
    def _gerar_cartela(self) -> List[List[int]]:
        cartela = []
        intervalos = [
            (1, 15),   
            (16, 30),
            (31, 45),
            (46, 60),
            (61, 75)
        ]
        
        for inicio, fim in intervalos:
            numeros_possiveis = list(range(inicio, fim + 1))
            numeros_coluna = random.sample(numeros_possiveis, 5)
            numeros_coluna.sort()
            cartela.append(numeros_coluna)
        
        cartela_transposta = [[cartela[col][linha] for col in range(5)] for linha in range(5)]
        
        return cartela_transposta
    
    def marcar_numero(self, numero: int) -> bool:
        for linha in self.numeros:
            if numero in linha:
                self.marcados.add(numero)
                return True
        return False
    
    def verificar_vitoria(self) -> bool:

        total_numeros = 24 
        return len(self.marcados) == total_numeros
    
    def exibir_cartela(self) -> None:
        print("\n" + "=" * 50)
        print(" " * 15 + "CARTELA DE BINGO")
        print("=" * 50)
        
        # Cabeçalho
        print("   B     I     N     G     O  ")
        print("-" * 50)
        
        for i, linha in enumerate(self.numeros):
            linha_str = ""
            for j, numero in enumerate(linha):

                if i == 2 and j == 2:
                    if self.espaco_livre:
                        linha_str += " [**] "
                    else:
                        linha_str += "  **  "
                else:
                    if numero in self.marcados:
                        linha_str += f" [{numero:2d}] "
                    else:
                        linha_str += f"  {numero:2d}  "
            
            print(linha_str)
        
        print("-" * 50)
        print(f"Números marcados: {len(self.marcados)}/24")
        print(f"Progresso: {(len(self.marcados)/24)*100:.1f}%")
        print("=" * 50 + "\n")
    
    def obter_numeros_cartela(self) -> List[int]:

        numeros = []
        for linha in self.numeros:
            numeros.extend(linha)
        return numeros


class JogoBingo:
    
    def __init__(self):
        self.sorteador = SorteadorBingo()
        self.cartela = CartelaBingo()
        self.rodadas = 0
        
    def jogar_rodada(self) -> dict:
        self.rodadas += 1
        
        numero = self.sorteador.sortear_numero()

        self.sorteador.exibir_numero_sorteado(numero)
        
        estava_na_cartela = self.cartela.marcar_numero(numero)
        
        if estava_na_cartela:
            print(f"O número {numero} ESTÁ na sua cartela!")
        else:
            print(f"O número {numero} NÃO está na sua cartela.")
        
        ganhou = self.cartela.verificar_vitoria()
        
        return {
            'rodada': self.rodadas,
            'numero_sorteado': numero,
            'estava_na_cartela': estava_na_cartela,
            'ganhou': ganhou
        }
    
    def simular_jogo_completo(self, mostrar_cartela_sempre: bool = False) -> int:
        print("\n")
        print("INICIANDO SIMULAÇÃO DE JOGO DE BINGO")
        print("\n")

        print("Sua cartela inicial:")
        self.cartela.exibir_cartela()
        
        input("Pressione ENTER para começar o sorteio...")
        
        while not self.cartela.verificar_vitoria():
            resultado = self.jogar_rodada()
            
            if mostrar_cartela_sempre:
                self.cartela.exibir_cartela()
            
            if not resultado['ganhou']:
                input("\nPressione ENTER para sortear o próximo número...")
        
        print("\n")
        print("BINGO!!! VOCÊ GANHOU!")
        print("\n")
        
        self.cartela.exibir_cartela()
        
        print(f"\n ESTATÍSTICAS DA PARTIDA:")
        print(f"   • Rodadas jogadas: {self.rodadas}")
        print(f"   • Números sorteados: {len(self.sorteador.numeros_sorteados)}")
        print(f"   • Taxa de acerto: {(len(self.cartela.marcados)/self.rodadas)*100:.1f}%")
        
        return self.rodadas


def main():
    print("\n" + "=" * 60)
    print(" " * 15 + "SIMULADOR DE BINGO")
    print("\n" + " " * 15 + "Projeto Lean")
    print("=" * 60)
    print("\n FACULDADE BELAS ARTES")
    print("\n ANÁLISE E DESENVOLVIMENTO DE SISTEMAS")
    print("\n PROCESSOS DE DESIGN ÁGIL DE SOFTWARE")
    print("\n ALUNA: NATHALIE GIULIANI DE OLIVEIRA")
    print("=" * 60 + "\n")
    
    jogo = JogoBingo()
    jogo.simular_jogo_completo(mostrar_cartela_sempre=False)
    
    print("\nQuer ver o histórico completo de números sorteados?")
    ver_historico = input("(s/n): ").lower().strip()
    
    if ver_historico == 's':
        jogo.sorteador.mostrar_historico()
    
    print("\n Simulação concluída com sucesso!")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
