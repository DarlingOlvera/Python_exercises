def findErrorNums(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    ans = []
    hasOne = False
    nums = sorted(nums)
    for index, value in enumerate(nums):
        if index == 0 and value == 1:
            hasOne = True
        if index > 0:
            if nums[index] == nums[index - 1]:
                ans.append(value)
                if not hasOne:
                    ans.append(1)
                elif index + 1 < len(nums) and nums[index + 1] == (value + 1):
                    ans.append(value - 1)
                else:
                    ans.append(nums[index] + 1)
                break
    return ans


arr = [1, 3, 3]

print(findErrorNums(arr))


def find_duplicate_and_missing(nums):
    # n = tamaño del array. Ej: [1,2,2,4] → n = 4
    n = len(nums)

    # Crea lista de ceros de tamaño n+1.
    # El índice representa cada número del 1 al n.
    # El índice 0 se ignora para que los índices coincidan con los números.
    # Ej: [0, 0, 0, 0, 0] → índices 0,1,2,3,4
    count = [0] * (n + 1)

    # Recorre el array y por cada número suma 1 en su posición.
    # Ej: encuentra 2 → count[2] += 1
    #     encuentra 2 de nuevo → count[2] += 1
    #     resultado: [0, 1, 2, 0, 1] → el 2 aparece 2 veces, el 3 aparece 0 veces
    for num in nums:
        count[num] += 1

    # Inicializa ambas variables en -1 como valor por defecto
    duplicate = missing = -1

    # Recorre del 1 al n revisando el conteo de cada número:
    # - Si apareció 2 veces → es el duplicado
    # - Si apareció 0 veces → es el faltante
    for i in range(1, n + 1):
        if count[i] == 2:
            duplicate = i
        if count[i] == 0:
            missing = i

    # Devuelve ambos valores como tupla. Ej: [1,2,2,4] → (2, 3)
    return duplicate, missing


print(find_duplicate_and_missing([1, 2, 2, 4]))  # → (2, 3)
print(find_duplicate_and_missing([3, 1, 3]))     # → (3, 2)
print(find_duplicate_and_missing([2, 2, 3]))     # → (2, 1)
print(find_duplicate_and_missing([1, 3, 3]))     # → (3, 2)
