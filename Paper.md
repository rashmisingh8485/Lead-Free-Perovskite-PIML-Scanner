---
title: 'Lead-Free-Perovskite-PIML-Scanner: A Python package for rapid screening of Sn-Ge halide perovskites'
tags:
  - Python
  - Physics-Informed Machine Learning
  - Perovskites
  - Solar Energy
  - Materials Science
authors:
  - name: Rashmi Singh
    orcid: 0000-0002-4521-6820
    affiliation: 1
affiliations:
  - name: Department of Physics, Institute of Applied Sciences & Humanities, GLA University, Mathura, India
    index: 1
date: 2 March 2026
bibliography: paper.bib
---

# Summary
This software is a Python-based tool designed to evaluate the stability of lead-free (Sn-Ge) perovskites. Lead-based solar cells are highly toxic; therefore, Sn-Ge mixed cations are explored as sustainable alternatives. This tool combines Machine Learning with the rules of Physics, specifically the Goldschmidt Tolerance Factor, to predict compositional combinations that are likely to be stable, reducing the need for thousands of lab experiments.

# Statement of Need
While there is extensive research on lead-free perovskites, their chemical space is enormous. Synthesizing every combination or evaluating them via Density Functional Theory (DFT) would take years. Many existing machine learning tools depend solely on data without incorporating physical principles. Our PIML (Physics-Informed ML) scanner bridges this gap by using a Random Forest Regressor integrated with geometric stability descriptors, enabling researchers to quickly identify stable candidates with optimal bandgaps.

# Implementation and Performance
The scanner is trained on a dataset of over 1,000 lead-free compositions. It achieves an $R^2$ score of 0.96 and a Mean Absolute Error (MAE) of 28.2 meV. The tool uses a modular architecture where `utils.py` handles the physics calculations and `model_engine.py` manages the machine learning pipeline.

# Illustrative Example
The tool features an interactive interface where users can input chemical fractions. For instance, a user input of `Cs_Fraction = 0.81` and `Sn_Fraction = 0.16` produces a predicted Bandgap of 1.82 eV with a 'STABLE' status. This demonstrates the tool's ability to rapidly screen and identify high-efficiency solar candidates.

# Acknowledgements
The author thanks GLA University for providing the research facilities and computational resources.

# References
