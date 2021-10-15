"""
Filhas e filas
Pilha (stak) - LIFO - last in, first out
    Exemplo: Pilha de livros que são adicionados um sobre o outro
Fila (queue) - FIFO - first in, first out
    Exemplo: Uma fila de banco (ou qualquer fila da vida real)
Filas podem ter efeitos colaterais em desempenho, porque a cada item
alterado, todo os índices serão modificados
"""
from collections import deque

fila = deque(maxlen=5)
fila.append('Juliano')
fila.append('Outro 1')
fila.append('Outro 2')
fila.append('Outro 3')

# remover primeiro elemento da fila
fila.popleft()

print(fila)