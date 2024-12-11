# Los siguientes algoritmos determinan si un número requiredSum puede formarse usando la suma de dos elementos de un array nums.

### Algoritmo 1: Fuerza Bruta ###
def sum_brute_force(nums, requiredSum):
    """
    Comlejidad temporal: O(n^2)
    Memoria: Baja
    Comentario: Compara cada par de números en el arreglo, ineficiente para arreglos grandes.
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == requiredSum:
                return True
    return False

# Ejemplo de pruebas para fuerza bruta
print(sum_brute_force([1, 4, 3, 9], 8))  # Output: False
print(sum_brute_force([1, 2, 4, 4], 8))  # Output: True


### Algoritmo 2: Optimizado ###
def sum_optimized(nums, requiredSum):
    """
    Comlejidad temporal: O(n)
    Memoria: Moderada
    Comentario: Utiliza un conjunto para almacenar los complementos de los números en el arreglo, eficiente para arreglos grandes.
    """
    complements = set()
    for num in nums:
        if requiredSum - num in complements:
            return True
        complements.add(num)
    return False

# Ejemplo de pruebas para optimizado
print(sum_optimized([1, 4, 3, 9], 8))  # Output: False
print(sum_optimized([1, 2, 4, 4], 8))  # Output: True

# Pruebas adicionales
print(sum_optimized([], 5))  # Output: False (Array vacío)
print(sum_optimized([5], 5))  # Output: False (Un solo elemento)
print(sum_optimized([-1, -2, 3, 5], 3))  # Output: True (Con números negativos)
print(sum_optimized([0, 4, 4], 0))  # Output: False (Suma requerida es 0)