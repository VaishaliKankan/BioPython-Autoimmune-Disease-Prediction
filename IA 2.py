import json
import matplotlib.pyplot as plt
from Bio import SeqIO

def load_markers_from_json(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    for gene in data:
        data[gene] = {key.lower(): value for key, value in data[gene].items()}
    return data

AUTOIMMUNE_MARKERS = load_markers_from_json("snp_markers.json")

def check_autoimmune_markers(sequence):
    detected_diseases = {}
    sequence = sequence.lower()

    for gene, mutations in AUTOIMMUNE_MARKERS.items():
        for mutation, (disease, risk_factor) in mutations.items():
            if mutation.lower() in sequence:  
                detected_diseases[disease] = detected_diseases.get(disease, 0) + risk_factor

    return detected_diseases

def plot_risk_scores(risk_scores):
  
    diseases = list(risk_scores.keys())
    scores = [min(100, round(score * 100)) for score in risk_scores.values()]  

    plt.figure(figsize=(10, 5))
    plt.barh(diseases, scores, color='skyblue')
    plt.xlabel("Risk Score (%)")
    plt.ylabel("Autoimmune Disease")
    plt.title("Predicted Risk Scores for Autoimmune Diseases")
    plt.xlim(0, 100)
    
    for index, value in enumerate(scores):
        plt.text(value + 1, index, f"{value}%", va='center', fontsize=10)

    plt.show()

def analyze_sequence(file_path):
  
    try:
        record = SeqIO.read(file_path, "fasta")
        sequence = str(record.seq)
        results = check_autoimmune_markers(sequence)
        
        if results:
            print("\nPotential autoimmune disease markers detected.\nPredicted Risk Scores for Autoimmune Diseases:")
            for disease, risk_score in results.items():
                percentage = min(100, round(risk_score * 100))  
                print(f"{disease}: {percentage}% risk")
            
            plot_risk_scores(results)
        else:
            print("\nNo known autoimmune disease markers detected.")
    
    except Exception as e:
        print(f"Error reading file: {e}")

analyze_sequence("sample_patient.fasta")


