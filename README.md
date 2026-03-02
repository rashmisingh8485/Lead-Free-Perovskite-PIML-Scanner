# AI-Perov-Screen: Physics-Informed ML Tool for Screening Lead-Free Perovskites
# AI-Driven Discovery of Lead-Free Sn-Ge Perovskites

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18831726.svg)](https://doi.org/10.5281/zenodo.18831726)

**Author:** Rashmi Singh  
**ORCID:** [0000-0002-4521-6820](https://orcid.org/0000-0002-4521-6820)
### 🔬 Software Overview
Lead-Free-Perovskite-PIML-Scanner is a specialized Python tool designed for the rapid computational screening of toxicity-free halide perovskites. By integrating Physics-Informed Machine Learning (PIML), the tool allows researchers to predict the thermodynamic stability of over 1,000+ Sn-Ge mixed cation compositions in seconds, bypassing expensive DFT calculations.

### 🚀 Core Features
* **Predictive Engine:**  High-performance Random Forest model trained on lead-free datasets ($R^2=0.96$, **MAE=28.2 meV**).
* **Physics-Informed Filtering:**  Built-in modules to calculate and filter candidates based on **Goldschmidt’s Tolerance Factor (t)** and **Octahedral Factor (μ)**.
* **Automated Screening:** Batch-processing capability to scan large composition spaces (like the Sn-Ge cation space) for solar efficiency.
* **Eco-friendly Design:** Specifically optimized for identifying lead-free alternatives, promoting sustainable photovoltaic research.

### 📁 Repository Structure
main.py: Interactive screening tool.
utils.py & model_engine.py: Physics logic and ML training modules.
novel_perovskite_space.csv: Dataset of 1,000+ lead-free compositions.
requirements.txt: List of dependencies.

### 🛠️ How to Run
1. Clone the repo: `git clone https://github.com/rashmisingh8485/Lead-Free-Perovskite-PIML-Scanner.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the model: `python main.py`

### 📝 Status
*Currently under research/preparation for journal submission.*
## Testing
To verify the core physics-based filters (Goldschmidt Tolerance Factor and Octahedral Factor), an automated test script is provided.

### Prerequisites
- Python 3.x
- NumPy

### Running the Test
Execute the following command in the terminal from the root directory:
```bash
python test_script.py

###  Status
*This software is currently submitted to the **Journal of Open Source Software (JOSS)** and is undergoing peer review.*

###  Contributing
Contributions are welcome! If you'd like to improve the physics logic or ML models, please refer to our [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to submit a Pull Request.

### 📜 Citation
If you use this software in your research, please cite it as follows:

**Singh, R. (2026). Lead-Free-Perovskite-PIML-Scanner: A Python package for rapid screening of Sn-Ge halide perovskites. Journal of Open Source Software (Submitted).**
