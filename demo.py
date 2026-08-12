import os, numpy as np, matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
os.makedirs("figures", exist_ok=True); os.makedirs("results", exist_ok=True)
rng = np.random.default_rng(0)
PANEL_MB = 35.0                                   # sequenced megabases
n = 400
hyper = rng.random(n) < 0.12                      # ~12% hypermutators (MSI/POLE)
muts = np.where(hyper, rng.poisson(700, n), rng.poisson(120, n))
tmb = muts / PANEL_MB
HIGH = 10.0                                        # mut/Mb, common high-TMB cutoff
frac_high = np.mean(tmb >= HIGH)
fig, ax = plt.subplots(1, 2, figsize=(12, 5))
ax[0].hist(np.log10(tmb), bins=40, color="#4C72B0")
ax[0].axvline(np.log10(HIGH), c="#C44E52", ls="--", label=f"high-TMB cutoff = {HIGH:.0f} mut/Mb")
ax[0].set_xlabel("log10 TMB (mut/Mb)"); ax[0].set_ylabel("samples"); ax[0].set_title("TMB distribution across a cohort"); ax[0].legend(fontsize=8)
ax[1].bar(["TMB-low","TMB-high"], [1-frac_high, frac_high], color=["#B0B0B0","#C44E52"])
ax[1].set_ylabel("fraction of cohort"); ax[1].set_title(f"{frac_high*100:.1f}% are TMB-high")
for i,v in enumerate([1-frac_high, frac_high]): ax[1].text(i, v+0.01, f"{v*100:.1f}%", ha="center")
fig.suptitle("Tumour mutational burden (demo data)"); fig.tight_layout(); fig.savefig("figures/demo.png", dpi=140)
open("results/summary.csv","w").write(f"median_tmb,{np.median(tmb):.2f}\nfraction_high_tmb,{frac_high:.3f}\n")
print(f"median TMB={np.median(tmb):.1f} high={frac_high*100:.1f}%"); print("ok")
