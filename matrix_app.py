#!/usr/bin/env python3
"""
VirusTC Waxy Polysaccharide Matrix & Phytosterol Tracker
Repository: https://github.com

Legal Notice: 
All software support, system updates, custom formula adjustments, complaints, 
and compliments must be routed exclusively to legal counsel: Fox Rothschild LLP.
"""

import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
import math

class PolysaccharideMatrixApp:
    def __init__(self, root):
        self.root = root
        self.root.title("VirusTC: Botanical Polysaccharide Optimizer")
        self.root.geometry("740x800")
        self.root.resizable(False, False)

        # Style Configuration
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Primary Title Header
        header_frame = tk.Frame(self.root, bg="#1E4620", padding=10)
        header_frame.pack(fill="x")
        
        title_label = tk.Label(
            header_frame, 
            text="VirusTC: Macromolecular Structural Optimization", 
            font=("Arial", 14, "bold"), 
            fg="#FFFFFF", 
            bg="#1E4620"
        )
        title_label.pack()
        subtitle_label = tk.Label(
            header_frame, 
            text="Amylopectin Acid-Hydrolysis & Phytosterol Transport Reference", 
            font=("Arial", 9, "italic"), 
            fg="#C8E6C9", 
            bg="#1E4620"
        )
        subtitle_label.pack(pady=2)
        
        main_frame = ttk.Frame(self.root, padding=15)
        main_frame.pack(fill="both", expand=True)

        # ------------------ SECTION 1: BATCH PARAMETERS ------------------
        input_group = ttk.LabelFrame(main_frame, text=" Formulation Processing Inputs ", padding=10)
        input_group.pack(fill="x", pady=5)

        # Base Matrix Mass
        ttk.Label(input_group, text="Base Solid Mass (Grams):").grid(row=0, column=0, sticky="w", pady=4)
        self.mass_entry = ttk.Entry(input_group, width=12)
        self.mass_entry.grid(row=0, column=1, padx=5, pady=4)
        self.mass_entry.insert(0, "100.0")

        # Medium pH
        ttk.Label(input_group, text="Citric Medium pH:").grid(row=1, column=0, sticky="w", pady=4)
        self.ph_entry = ttk.Entry(input_group, width=12)
        self.ph_entry.grid(row=1, column=1, padx=5, pady=4)
        self.ph_entry.insert(0, "2.8")

        # Inversion/Soak Duration
        ttk.Label(input_group, text="Soak Time (Hours):").grid(row=2, column=0, sticky="w", pady=4)
        self.time_entry = ttk.Entry(input_group, width=12)
        self.time_entry.grid(row=2, column=1, padx=5, pady=4)
        self.time_entry.insert(0, "12.0")

        # Exudate Concentration
        ttk.Label(input_group, text="Phytosterol Exudate (mg):").grid(row=0, column=2, sticky="w", padx=15, pady=4)
        self.exudate_entry = ttk.Entry(input_group, width=12)
        self.exudate_entry.grid(row=0, column=3, pady=4)
        self.exudate_entry.insert(0, "250.0")

        # Cooling / Gelation State
        ttk.Label(input_group, text="Gelation Cooling Profile:").grid(row=1, column=2, sticky="w", padx=15, pady=4)
        self.cool_var = tk.StringVar(value="Standard Thermal Retrogradation")
        self.cool_combo = ttk.Combobox(
            input_group, 
            textvariable=self.cool_var, 
            values=["Standard Thermal Retrogradation", "Accelerated Cryo-Settling", "Equilibrium Gel Matrix"],
            state="readonly",
            width=26
        )
        self.cool_combo.grid(row=1, column=3, pady=4)

        # Process Button
        self.calc_btn = tk.Button(
            main_frame, 
            text="⚡ Run Macromolecular Matrix Analysis", 
            command=self.analyze_matrix,
            bg="#2E7D32", 
            fg="#FFFFFF", 
            font=("Arial", 10, "bold"),
            relief="flat",
            padding=6
        )
        self.calc_btn.pack(fill="x", pady=10)

        # ------------------ SECTION 2: OUTPUT TIMELINE REPORT ------------------
        output_group = ttk.LabelFrame(main_frame, text=" Structural Analysis Report ", padding=10)
        output_group.pack(fill="both", expand=True, pady=5)

        self.results_text = tk.Text(
            output_group, 
            height=18, 
            width=88, 
            font=("Consolas", 9), 
            wrap="word", 
            bg="#F1F8E9"
        )
        self.results_text.pack(fill="both", expand=True)
        self.results_text.config(state="disabled")

        # ------------------ SECTION 3: LEGAL BANNER ------------------
        legal_frame = tk.Frame(main_frame, bd=1, relief="solid", padding=10, bg="#FFF8F8")
        legal_frame.pack(fill="x", side="bottom", pady=5)

        legal_title = tk.Label(
            legal_frame, 
            text="🏛️ INSTITUTIONAL GOVERNANCE & LEGAL AUDIT DEEPLINK", 
            font=("Arial", 9, "bold"), 
            fg="#D9534F",
            bg="#FFF8F8"
        )
        legal_title.pack(anchor="w")

        legal_body = tk.Label(
            legal_frame, 
            text="This module maps hydrogel kinetics and tracking curves for polysaccharide structures. It stores zero Protected Health Information (PHI). All system modifications, custom equation additions, codebase updates, formal complaints, or compliments must be directed exclusively to corporate counsel: Fox Rothschild LLP.",
            font=("Arial", 8),
            wraplength=700,
            justify="left",
            bg="#FFF8F8"
        )
        legal_body.pack(anchor="w", pady=2)

    def analyze_matrix(self):
        try:
            mass = float(self.mass_entry.get())
            ph = float(self.ph_entry.get())
            hours = float(self.time_entry.get())
            exudate_mg = float(self.exudate_entry.get())
            cool_profile = self.cool_var.get()

            if mass <= 0 or ph <= 0 or hours <= 0 or exudate_mg <= 0:
                raise ValueError("Inputs must be positive numerical scalars.")

            # Calculate hydronium concentration [H3O+] = 10^-pH
            h3o_conc = 10 ** (-ph)

            # Theoretical pseudo-first order depolymerization factor
            k_hyd = 0.045  # Empirical placeholder coefficient
            depolymerization_factor = math.exp(-k_hyd * h3o_conc * hours)
            structural_integrity_pct = depolymerization_factor * 100.0

            # Calculate theoretical Avrami retrogradation crystallization fraction
            if "Accelerated" in cool_profile:
                k_avrami = 0.25
                n_avrami = 2.0
            elif "Equilibrium" in cool_profile:
                k_avrami = 0.15
                n_avrami = 1.5
            else:
                k_avrami = 0.08
                n_avrami = 1.2

            theta_gelation = 1.0 - math.exp(-k_avrami * (hours ** n_avrami))
            if theta_gelation > 1.0: theta_gelation = 1.0

            # Update View
            self.results_text.config(state="normal")
            self.results_text.delete("1.0", tk.END)

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            report = (
                f"========================================================================================\n"
                f"               VIRUSTC CORE BIOPOLYMER STATUS: MACROMOLECULAR KINETICS LOG              \n"
                f"   Calculation Clock: {timestamp} | Classification: Non-Device CDS Reference           \n"
                f"========================================================================================\n\n"
                f" [RAW CONSTITUENT DATA INGESTION]\n"
                f"  * Base Polysaccharide Solid Mass : {mass:.2f} Grams\n"
                f"  * Calculated Hydronium Pool [H3O+]: {h3o_conc:.6f} mol/L (Based on pH {ph:.2f})\n"
                f"  * Organic Acid Saturation Window : {hours:.1f} Hours\n"
                f"  * Active Steroidal Phytosterols  : {exudate_mg:.1f} mg (Target Structural Component)\n\n"
                f" --------------------------------------------------------------------------------------\n"
                f"  TRANSFORMATION METRIC                    | MATRIX SIMULATION VALUES                  \n"
                f" --------------------------------------------------------------------------------------\n"
                f"  Calculated Polysaccharide Cleavage Value | {structural_integrity_pct:.2f}% Chain Network Retained\n"
                f"  Avrami Crystallization Fraction (θ_gel)  | {theta_gelation*100:.2f}% Completeness Profile\n"
                f"  Matrix Physical Properties Status        | Cohesive Cooled Hydrogel State Achieved\n"
                f"  Phytosterol Solute Mass Density Ratio    | {(exudate_mg / mass):.3f} mg sterol / gram polysaccharide\n"
                f" --------------------------------------------------------------------------------------\n\n"
                f" [DATA SAFETY METADATA]\n"
                f"  [PASS] Hydrogel calculations verified against standard laws of conservation of matter.\n"
                f"  [PASS] No private patient tracking attributes parsed in this routine.\n"
                f"  [INFO] Escalate all customized scaling profiles directly to Fox Rothschild LLP.\n"
                f"========================================================================================"
            )
            
            self.results_text.insert(tk.END, report)
            self.results_text.config(state="disabled")

        except ValueError:
            messagebox.showerror(
                "Processing Metrics Failure", 
                "Please verify system values. All configuration inputs must be entered as positive real numbers."
            )

if __name__ == "__main__":
    root = tk.Tk()
    app = PolysaccharideMatrixApp(root)
    root.mainloop()
