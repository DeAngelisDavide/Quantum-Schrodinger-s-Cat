from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
from qiskit_aer import AerSimulator
from qiskit_ibm_runtime import Session, SamplerV2 as Sampler
from utility import initializeCircuit
from matplotlib import pyplot as plt

def simulate_schrodinger_cat():
    qregs, cregs, circuit = initializeCircuit(['cat'], 'c', [1], [1])
    #Superposition: Hadamard Gate
    circuit.h(qregs[0][0])
    #We can manipulate the probability rotating the axes
    circuit.ry(-0.3, qregs[0][0])
    circuit.measure(qregs[0][0], cregs[0][0])
    return circuit

def plot_results(counts):
    labels = list(counts.keys())
    values = list(counts.values())
    plt.close()
    plt.bar(labels, values)
    plt.xlabel('Cat State')
    plt.ylabel('Number of Measurements')
    plt.title('Schrödinger’s Cat Simulation')
    plt.xticks(labels, ['Alive (|0⟩)', 'Dead (|1⟩)'])
    plt.savefig('Cat State')

# Main
if __name__ == "__main__":
    # Let's simulate the circuit
    schrodinger_cat_circuit = simulate_schrodinger_cat()
    schrodinger_cat_circuit.draw("mpl").savefig('cat.png')
    aer_sim = AerSimulator()
    pm = generate_preset_pass_manager(backend=aer_sim, optimization_level=1)
    run_qc = pm.run(schrodinger_cat_circuit)
    with Session(backend=aer_sim) as session:
        sampler = Sampler(mode=session)
        result = sampler.run([run_qc]).result()
        pub_result = result[0]

    # Check the result
    counts = pub_result.data.c.get_counts()
    plot_results(counts)
