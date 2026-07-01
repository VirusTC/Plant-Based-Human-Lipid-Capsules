🔬 Extended Biochemical Extraction & Gelation Models (LaTeX)

To evaluate the molecular structural transition of waxy maize amylopectin grids treated with organic fruit-acid carriers and reinforced with botanical triterpenoid/phytosterol exudates, the system utilizes standardized fluid mechanics and macromolecular retrogradation equations.

1\. Low-pH Acid Hydrolysis of Polysaccharide Chains

When waxy corn components are subjected to a prolonged aqueous soak in an organic acid medium (such as citric acid from lime juice), hydronium ions (\(\text{H}_3\text{O}^+\)) cleave the internal \(\alpha\text{-(1}\rightarrow\text{4)}\) and \(\alpha\text{-(1}\rightarrow\text{6)}\) glucosidic linkages. The rate of depolymerization is modeled as a pseudo-first-order kinetic step:

\(\ln \left(\frac{DP_{t}-DP_{\infty }}{DP_{0}-DP_{\infty }}\right)=-k_{\text{hyd}}\cdot [\text{H}_{3}\text{O}^{+}]\cdot t\)

Where:

-   \(DP_{0}\), \(DP_{t}\), and \(DP_{\infty }\) represent the Degree of Polymerization at times \(0\), \(t\), and equilibrium, respectively.
-   \(k_{\text{hyd}}\) is the specific acid-hydrolysis rate constant (\(\text{L}\cdot\text{mol}^{-1}\cdot\text{hr}^{-1}\)).
-   \([\text{H}_3\text{O}^+]\) is the hydronium ion concentration determined by the medium's pH profile.

2\. Thermal Retrogradation & Viscoelastic Gelation (The "Cold Leftover" Phase)

Upon cooling, the linearized amylopectin fragments re-associate via hydrogen bonding to form a highly structured, cohesive three-dimensional gel network. The crystallization kinetics are quantified using the Avrami macromolecular transformation model:

\(\theta (t)=1-e^{-K\cdot t^{n}}\)

Where:

-   \(\theta(t)\) is the fraction of the polysaccharide matrix that has successfully transformed into a crystalline gel at time \(t\).
-   \(K\) is the temperature-dependent crystallization rate constant.
-   \(n\) is the Avrami exponent, dictating the geometric mechanism of crystal nucleation and growth.

3\. Phytosterol Homology and Mass Balance Integration

The addition of the surface exudate ("bamboo pith shakedown") introduces plant sterols (phytosterols), which exhibit structural homology to endogenous steroidal frameworks due to their classic cyclopentanoperhydrophenanthrene ring core. The retention matrix within the final formulation fluid volume (\(V_{f}\)) follows a conservation of mass relationship:

\(M_{\text{total}}=\rho _{\text{gel}}\cdot V_{\text{gel}}+\int _{0}^{V_{\text{water}}}C_{\text{sterol}}(\nu )\,d\nu \)

Where:

-   \(\rho _{\text{gel}}\) is the mass density of the structural polysaccharide gel framework.
-   \(C_{\text{sterol}}(\nu)\) is the spatial concentration distribution of dissolved phytosterols within the aqueous dilution volume.
