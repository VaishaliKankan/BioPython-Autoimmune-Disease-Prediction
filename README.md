# Autoimmune Disease Risk Prediction from Human DNA Sequences Using SNP Markers and Biopython

**Vaishali Kankan**  
B.Sc. in Bioinformatics, Statistics, and Computer Science  

## Overview:
This project develops a **Python-based computational tool** that analyzes human DNA sequences to predict the **risk of autoimmune diseases**.  

The tool leverages known **Single Nucleotide Polymorphism (SNP) markers** associated with various autoimmune conditions. By scanning input DNA sequences, it detects these variants and provides a risk prediction for diseases such as:  
- Rheumatoid Arthritis  
- Psoriasis  
- Type 1 Diabetes  
- (and other autoimmune conditions)  

## Features:
- Accepts input DNA sequences in **FASTA format**  
- Scans for SNP markers using a **curated JSON database**  
- Predicts disease susceptibility based on detected SNPs  
- Generates **two outputs**:  
  1. Textual report of predicted risks  
  2. **Horizontal bar chart** showing risk scores  
- Combines **Biopython** for DNA processing and **Matplotlib** for visualization  

## Tech Stack:
- **Python** (Core programming)  
- **Biopython** (DNA sequence processing)  
- **JSON** (SNP marker database)  
- **Matplotlib** (Data visualization)  

## Workflow:
1. **Input**: DNA sequence in FASTA format  
2. **Processing**:  
   - Parse DNA using Biopython  
   - Match SNP markers against curated database  
   - Assign risk scores for autoimmune diseases  
3. **Output**:  
   - Text report of predictions  
   - Horizontal bar chart with likelihood percentages  

## Objective:
This project demonstrates:  
- **Bioinformatics data processing**  
- **Genetic risk analysis**  
- **Data visualization**  
- Building a tool to assist in **early prediction of autoimmune disease susceptibility**  

