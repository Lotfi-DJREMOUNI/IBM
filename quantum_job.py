import os
from qiskit import QuantumCircuit
from qiskit_ibm_runtime import QiskitRuntimeService

# Chargement du token depuis .env
API_TOKEN = ""


# Initialiser le service Qiskit Runtime
service = QiskitRuntimeService(channel="ibm_quantum", token=API_TOKEN)

# Lister les backends disponibles et en sélectionner un (ici, le premier)
available_backends = service.backends()
print("Backends disponibles :", available_backends)

backend_name = available_backends[0].name  
print("Utilisation du backend :", backend_name)

# Créer un circuit quantique simple : porte Hadamard sur 1 qubit et mesure
qc = QuantumCircuit(1, 1)
qc.h(0)
qc.measure(0, 0)

# Soumettre le job via le programme "sampler" en utilisant la méthode interne _run
job = service._run(
    program_id="sampler",
    options={"backend": backend_name},
    inputs={"circuits": [qc], "shots": 1}
)

# Afficher l'ID du job
print("Job ID:", job.job_id())
