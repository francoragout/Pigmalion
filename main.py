# Los siguientes algoritmos determinan si un número requiredSum puede formarse usando la suma de dos elementos de un array nums.

### Algoritmo 1: Fuerza Bruta ###
def can_form_sum_brute_force(nums, requiredSum):
    """
    Ventaja: Es directo y simple de implementar. Adecuado para aprender el concepto.
    Desventaja: Ineficiente en tiempo y memoria para grandes números (O(n^2)).
    Descripción: El algoritmo recorre cada par de elementos en el arreglo y verifica si su suma es igual al valor deseado.
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == requiredSum:
                return True
    return False

# Ejemplo de pruebas para fuerza bruta
print(can_form_sum_brute_force([1, 4, 3, 9], 8))  # Output: False
print(can_form_sum_brute_force([1, 2, 4, 4], 8))  # Output: True


### Algoritmo 2: Optimizado ###
def can_form_sum_optimized(nums, requiredSum):
    """
    Ventaja: Este enfoque es más eficiente, con una complejidad temporal de O(n). Utiliza un conjunto (set) para almacenar los complementos de los elementos mientras recorre el arreglo.
    Desventaja: Requiere un poco más de memoria para almacenar los complementos, aunque esto es insignificante comparado con la mejora en velocidad.
    Descripción: El algoritmo recorre el arreglo y verifica si el complemento del elemento actual (requiredSum - num) ya está en el conjunto de complementos. Si es así, significa que se ha encontrado un par de elementos cuya suma es igual al valor deseado.
    """
    complements = set()
    for num in nums:
        if requiredSum - num in complements:
            return True
        complements.add(num)
    return False

# Ejemplo de pruebas para optimizado
print(can_form_sum_optimized([1, 4, 3, 9], 8))  # Output: False
print(can_form_sum_optimized([1, 2, 4, 4], 8))  # Output: True

# Pruebas adicionales
print(can_form_sum_optimized([], 5))  # Output: False (Array vacío)
print(can_form_sum_optimized([5], 5))  # Output: False (Un solo elemento)
print(can_form_sum_optimized([-1, -2, 3, 5], 3))  # Output: True (Con números negativos)
print(can_form_sum_optimized([0, 4, 4], 0))  # Output: False (Suma requerida es 0)