# hemoglobin_analysis.py
# Este script analiza la proteína hemoglobina beta humana.
# El programa hace lo siguiente:
# 1. Guarda la secuencia de aminoácidos
# 2. Muestra información básica de la proteína
# 3. Cuenta cuántas veces aparece cada aminoácido
# 4. Calcula el peso molecular de la proteína
# 5. Calcula el porcentaje de aminoácidos hidrofóbicos
# 6. Guarda los resultados en un archivo JSON

# Importamos la librería json
# Esta librería nos permite guardar resultados en formato JSON
import json


# Guardamos el nombre de la proteína en una variable
protein_name = "Hemoglobin beta"


# Guardamos la secuencia limpia de aminoácidos
# Cada letra representa un aminoácido
# La secuencia tiene 147 aminoácidos
sequence = "MVHLTPEEKSAVTALWGKVNVDEVGGEALGRLLVVYPWTQRFFESFGDLSTPDAVMGNPKVKAHGKKVLGAFSDGLAHLDNLKGTFATLSELHCDKLHVDPENFRLLGNVLVCVLAHHFGKEFTPPVQAAYQKVVAGVANALAHKYH"


# Mostramos información básica en pantalla
print("Proteína:", protein_name)

# Mostramos la secuencia completa
print("Secuencia:", sequence)

# Calculamos la longitud de la secuencia usando len()
print("Longitud de la secuencia:", len(sequence))


# Creamos una lista con los 20 aminoácidos estándar
amino_acids = [
    "A", "R", "N", "D", "C",
    "Q", "E", "G", "H", "I",
    "L", "K", "M", "F", "P",
    "S", "T", "W", "Y", "V"
]


# Creamos un diccionario vacío
# Aquí guardaremos cuántas veces aparece cada aminoácido
aa_counts = {}


# Recorremos la lista de aminoácidos
for aa in amino_acids:

    # Contamos cuántas veces aparece ese aminoácido en la secuencia
    aa_counts[aa] = sequence.count(aa)


# Mostramos el conteo de aminoácidos
print("\nConteo de aminoácidos:")

# Recorremos el diccionario y mostramos los resultados
for aa, count in aa_counts.items():
    print(aa, ":", count)


# Creamos un diccionario con el peso molecular de cada aminoácido
# Estos valores son pesos promedio usados en bioinformática
amino_acid_weights = {
    "A": 89.09,
    "R": 174.20,
    "N": 132.12,
    "D": 133.10,
    "C": 121.15,
    "Q": 146.15,
    "E": 147.13,
    "G": 75.07,
    "H": 155.16,
    "I": 131.17,
    "L": 131.17,
    "K": 146.19,
    "M": 149.21,
    "F": 165.19,
    "P": 115.13,
    "S": 105.09,
    "T": 119.12,
    "W": 204.23,
    "Y": 181.19,
    "V": 117.15
}


# Creamos una función para calcular el peso molecular de la proteína
# Esto hace que el código sea reutilizable
def calculate_molecular_weight(sequence, weights):

    # Variable donde acumularemos el peso total
    total_weight = 0

    # Recorremos cada aminoácido de la secuencia
    for aa in sequence:

        # Sumamos el peso correspondiente de ese aminoácido
        total_weight += weights[aa]

    # Devolvemos el peso total calculado
    return total_weight


# Llamamos la función y guardamos el resultado
molecular_weight = calculate_molecular_weight(sequence, amino_acid_weights)


# Mostramos el peso molecular calculado
print("\nPeso molecular:", molecular_weight)


# Definimos los aminoácidos hidrofóbicos
# Estos aminoácidos tienden a evitar el agua
hydrophobic_amino_acids = ["A", "V", "I", "L", "M", "F", "W", "Y"]


# Contador para los aminoácidos hidrofóbicos
hydrophobic_count = 0


# Recorremos la secuencia
for aa in sequence:

    # Si el aminoácido está en la lista de hidrofóbicos
    if aa in hydrophobic_amino_acids:

        # Aumentamos el contador
        hydrophobic_count += 1


# Calculamos el porcentaje hidrofóbico
hydrophobic_percentage = (hydrophobic_count / len(sequence)) * 100


# Mostramos el porcentaje
print("\nPorcentaje de aminoácidos hidrofóbicos:", round(hydrophobic_percentage, 2))


# Creamos un diccionario con todos los resultados
results = {
    "protein_name": protein_name,
    "sequence_length": len(sequence),
    "amino_acid_counts": aa_counts,
    "molecular_weight": molecular_weight,
    "hydrophobic_percentage": hydrophobic_percentage
}


# Abrimos el archivo JSON en modo escritura
with open("hemoglobin_results.json", "w") as file:

    # Guardamos el diccionario en formato JSON
    json.dump(results, file, indent=4)


# Mensaje final indicando que el archivo fue creado
print("\nResultados guardados en hemoglobin_results.json")