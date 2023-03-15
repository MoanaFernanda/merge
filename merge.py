import threading
from random import randint

def merge_sort(arr):
    # Verifica se o array precisa ser dividido
    if len(arr) > 1:
        # Divide o array ao meio
        mid = len(arr) // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:]

        # Cria duas threads para fazer o merge de cada metade
        left_thread = threading.Thread(target=merge_sort, args=(left_arr,))
        right_thread = threading.Thread(target=merge_sort, args=(right_arr,))
        left_thread.start()
        right_thread.start()

        # Aguarda as threads terminarem
        left_thread.join()
        right_thread.join()

        # Faz o merge das duas metades
        left_index = right_index = 0
        while left_index < len(left_arr) and right_index < len(right_arr):
            if left_arr[left_index] < right_arr[right_index]:
                arr[left_index+right_index] = left_arr[left_index]
                left_index += 1
            else:
                arr[left_index+right_index] = right_arr[right_index]
                right_index += 1

        # Adiciona os elementos restantes, se houver
        while left_index < len(left_arr):
            arr[left_index+right_index] = left_arr[left_index]
            left_index += 1
        while right_index < len(right_arr):
            arr[left_index+right_index] = right_arr[right_index]
            right_index += 1


# Teste com um array aleatório
lista = []
for c in range(100):
    num = randint(1, 2000)
    lista.append(num)

print("Array antes do merge sort: ", lista)

merge_sort(lista)

print("Array depois do merge sort: ", lista)