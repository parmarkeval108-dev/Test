# Kwality Pharmaceuticals - DCF engine. All figures INR crore. Valuation date 22-Sep-2026.
SHARES = 1.0372          # crore shares
NET_DEBT = 110.0         # INR cr, central estimate (range 95-130)
PRICE = 3773.95          # INR/share, close 21-Sep-2026

def dcf(growth, ebitda_margin, wc_pct_of_delta_rev, wacc, g_term,
        tax=0.2517, da_pct=0.035, capex=None, rev0=503.1, verbose=False):
    """growth: list of yoy growth rates FY27..FY36; ebitda_margin: list same length;
       capex: list of absolute capex, else % of revenue schedule."""
    rev = rev0
    rows = []
    pv = 0.0
    for i, (g, m) in enumerate(zip(growth, ebitda_margin), start=1):
        prev_rev = rev
        rev = rev * (1 + g)
        ebitda = rev * m
        da = rev * da_pct
        ebit = ebitda - da
        nopat = ebit * (1 - tax)
        cpx = capex[i-1] if capex else rev * 0.05
        dwc = (rev - prev_rev) * wc_pct_of_delta_rev
        fcf = nopat + da - cpx - dwc
        disc = (1 + wacc) ** (i - 0.5)     # mid-year
        pv += fcf / disc
        rows.append((i, rev, ebitda, m, nopat, da, cpx, dwc, fcf, fcf/disc))
    # terminal: normalised FCF from final year, capex = D&A * 1.15, wc at terminal growth
    rev_t = rev * (1 + g_term)
    ebitda_t = rev_t * ebitda_margin[-1]
    da_t = rev_t * da_pct
    ebit_t = ebitda_t - da_t
    nopat_t = ebit_t * (1 - tax)
    capex_t = da_t * 1.15
    dwc_t = (rev_t - rev) * wc_pct_of_delta_rev
    fcf_t = nopat_t + da_t - capex_t - dwc_t
    tv = fcf_t / (wacc - g_term)
    pv_tv = tv / ((1 + wacc) ** (len(growth) - 0.5))
    ev = pv + pv_tv
    eq = ev - NET_DEBT
    vps = eq / SHARES
    if verbose:
        print(f"{'Yr':>3}{'Rev':>9}{'EBITDA':>9}{'mgn':>7}{'NOPAT':>8}{'D&A':>7}{'Capex':>8}{'dNWC':>8}{'FCF':>9}{'PV':>9}")
        for r in rows:
            print(f"{r[0]:>3}{r[1]:>9.0f}{r[2]:>9.0f}{r[3]*100:>6.1f}%{r[4]:>8.0f}{r[5]:>7.0f}{r[6]:>8.0f}{r[7]:>8.0f}{r[8]:>9.0f}{r[9]:>9.0f}")
        print(f"PV explicit {pv:,.0f} | PV TV {pv_tv:,.0f} ({pv_tv/ev*100:.0f}% of EV) | EV {ev:,.0f} | Eq {eq:,.0f} | Rs/sh {vps:,.0f}")
        print(f"Terminal FCF {fcf_t:,.0f} | implied exit EV/EBITDA {tv/ebitda_t:.1f}x | EV/FY27E EBITDA {ev/rows[0][2]:.1f}x")
    return dict(ev=ev, eq=eq, vps=vps, pv_tv_share=pv_tv/ev, rows=rows,
                exit_mult=tv/ebitda_t, ev_fy27=ev/rows[0][2])

# ---------------- BASE ----------------
g_base  = [0.372, 0.25, 0.20, 0.18, 0.14, 0.12, 0.10, 0.08, 0.07, 0.06]
m_base  = [0.26, 0.255, 0.25, 0.245, 0.24, 0.24, 0.24, 0.235, 0.235, 0.235]
cap_base= [120, 95, 80, 70, 65, 62, 62, 62, 64, 66]
print("=== BASE ===")
base = dcf(g_base, m_base, 0.45, 0.155, 0.05, capex=cap_base, verbose=True)

print("\n=== BEAR ===")
g_bear = [0.25, 0.15, 0.12, 0.10, 0.08, 0.07, 0.06, 0.06, 0.05, 0.05]
m_bear = [0.235, 0.225, 0.215, 0.21, 0.205, 0.20, 0.20, 0.20, 0.20, 0.20]
cap_bear=[120, 90, 70, 55, 50, 48, 48, 50, 52, 54]
bear = dcf(g_bear, m_bear, 0.55, 0.17, 0.045, capex=cap_bear, verbose=True)

print("\n=== BULL ===")
g_bull = [0.45, 0.32, 0.27, 0.22, 0.18, 0.15, 0.12, 0.10, 0.08, 0.07]
m_bull = [0.275, 0.28, 0.285, 0.29, 0.29, 0.285, 0.28, 0.275, 0.27, 0.27]
cap_bull=[140, 120, 105, 95, 90, 88, 88, 90, 92, 95]
bull = dcf(g_bull, m_bull, 0.35, 0.14, 0.055, capex=cap_bull, verbose=True)

print("\n=== WACC x terminal g sensitivity (base operating case), Rs/share ===")
print(f"{'':>8}" + "".join(f"{gt*100:>9.1f}%" for gt in [0.04,0.045,0.05,0.055,0.06]))
for w in [0.135,0.145,0.155,0.165,0.175]:
    line = f"{w*100:>7.1f}%"
    for gt in [0.04,0.045,0.05,0.055,0.06]:
        line += f"{dcf(g_base,m_base,0.45,w,gt,capex=cap_base)['vps']:>10,.0f}"
    print(line)

print("\n=== Working-capital intensity sensitivity (base, WACC 15.5%, g 5%) ===")
for wc in [0.25,0.35,0.45,0.55,0.65]:
    r = dcf(g_base, m_base, wc, 0.155, 0.05, capex=cap_base)
    print(f"  dNWC = {wc*100:.0f}% of incremental revenue -> Rs {r['vps']:,.0f}/sh  (EV {r['ev']:,.0f})")

print(f"\nMarket: price Rs {PRICE:,.2f} (21-Sep-2026), shares {SHARES} cr -> mkt cap Rs {PRICE*SHARES:,.0f} cr, EV Rs {PRICE*SHARES+NET_DEBT:,.0f} cr")

# ---- Reverse DCF: discount rate implied by the traded price ----
TARGET_EV = PRICE * SHARES + NET_DEBT
def solve_wacc(g, m, cap, wc, gt=0.05):
    lo, hi = 0.055, 0.30
    for _ in range(200):
        mid = (lo + hi) / 2
        if dcf(g, m, wc, mid, gt, capex=cap)['ev'] > TARGET_EV: lo = mid
        else: hi = mid
    return (lo + hi) / 2

print(f"\n=== Reverse DCF: EV to justify Rs {PRICE:,.2f}/share = {TARGET_EV:,.0f} cr ===")
for label, (g, m, cap) in {"base op case": (g_base, m_base, cap_base),
                           "bull op case": (g_bull, m_bull, cap_bull)}.items():
    for wc in [0.45, 0.35, 0.25]:
        print(f"  {label}, dNWC {wc*100:.0f}% of incremental revenue -> implied WACC {solve_wacc(g,m,cap,wc)*100:5.2f}%")
