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
This software is a Python-based tool designed to evaluate the stability of lead-free (Sn-Ge) perovskites. Lead-based solar cells are highly toxic; therefore, Sn-Ge mixed cations are explored as sustainable alternatives. This tool integrates Physics-Informed Machine Learning (PIML) by combining Random Forest Regressors with geometric descriptors like the Goldschmidt Tolerance Factor to predict stable compositional combinations.

# Statement of Need
The chemical space for lead-free perovskites is vast, with thousands of potential combinations. Evaluating each through experimental synthesis or high-level Density Functional Theory (DFT) calculations is computationally expensive and time-consuming. While general machine learning toolkits like `matminer` [@ward2018matminer] exist, they often require significant coding expertise. Our tool provides a streamlined, interactive interface specifically tuned for the Sn-Ge space, allowing researchers to perform rapid screening with a focus on structural stability.

# Implementation and Performance
The scanner utilizes a dataset of over 1,000 lead-free compositions. The model achieves an $R^2$ score of 0.96 and a Mean Absolute Error (MAE) of 28.2 meV. The core logic uses the tolerance factor ($t$) as a physics-based filter:
$$t = \frac{r_A + r_X}{\sqrt{2}(r_B + r_X)}$$
Where $r_A, r_B,$ and $r_X$ are the ionic radii. The tool classifies compounds as 'STABLE' if $0.8 \leq t \leq 1.0$.

# Illustrative Example
A user providing inputs of $Cs_{fraction} = 0.81$ and $Sn_{fraction} = 0.16$ receives a predicted Bandgap of 1.82 eV and a 'STABLE' status. This demonstrates the tool's utility in identifying candidates for high-efficiency, non-toxic solar cells.

# Acknowledgements
The author thanks GLA University for providing the research facilities and computational resources.

# References
