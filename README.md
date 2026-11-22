# Reverzibilni polni seštevalniki v QCA

Seminarska naloga pri predmetu Nekonvencionalne platforme in metode procesiranja (2026/27), skupina 19: Denis Balant, Domen Breznik.

Primerjava disipacije energije polnih seštevalnikov v QCA: zasnovi Wanga in sod. (2003) ter Pudija in Sridharana (2012), vsaka s klasičnimi majoritetnimi vrati in z vrati Torresa in sod. (2019), ter objavljeni vezji Ahmada in sod. (2018) in Seyedija in Jafarija Navimipourja (2022).

## Vsebina

```
implementacije/       postavitve za QCADesigner-E (.qca, izvoz v .pdf in .ps)
  pudi/
    pudi_irr.qca        Pudi, klasična vrata
    pudi_torres.qca     Pudi, vrata Torresa in sod.
  wang/
    wang_irr.qca        Wang, klasična vrata
    wang_torres.qca     Wang, vrata Torresa in sod.
  primerjava/
    ahmad2018.qca       Ahmad in sod. (2018)
    seyedi.qca          Seyedi in J. N. (2022)
rezultati/
  rezultati.csv         Avg_Ebath pri 4, 40 in 400 ps
  plot.py               graf energije iz CSV
  rezultati.pdf         izrisan graf
porocila/
  NPMP_sem1_predlog.pdf
  porocilo/             poročilo (LaTeX)
  slides/               predstavitev (LaTeX)
```

V vseh datotekah `.qca` so celice vhodnih vodil, izhodnih vodil in dodatnih izhodov že označene z `ignore_energy`, zato jih simulator pri energiji ne šteje.

## Ponovitev simulacij

Potrebujemo [QCADesigner-E](https://github.com/FSillT/QCADesigner-E).

1. Odpremo postavitev iz `implementacije/`.
2. *Simulation → Simulation Engine Setup*: izberemo koherenčni simulator z izračunom energije in nastavimo parametre iz tabele.
3. *Simulation Type*: *Exhaustive Verification*.
4. Zaženemo simulacijo in odčitamo `Avg_Ebath` v izpisu.

| Parameter | Vrednost |
|---|---|
| Temperatura | 1 K |
| Čas relaksacije | 1e-15 s |
| Časovni korak | 1e-16 s |
| Ura: visoka / nizka raven | 9,8e-22 J / 3,8e-23 J |
| Relativna dielektričnost | 12,9 |
| Polmer interakcije | 80 nm |
| Razmik med plastmi | 11,5 nm |

Od periode ure so odvisni štirje parametri:

| Perioda ure = perioda vhodov | Strmina ure | Skupni čas simulacije |
|---|---|---|
| 4e-12 s | 1e-12 s | 5e-11 s |
| 4e-11 s | 1e-11 s | 5e-10 s |
| 4e-10 s | 1e-10 s | 5e-9 s |

## Graf

```
pip install matplotlib
python3 rezultati/plot.py rezultati/rezultati.csv
```

Skripta prebere podani CSV in graf shrani kot PDF z enakim imenom v isto mapo (tu `rezultati/rezultati.pdf`). Če simulacije ponovimo, vrednosti `Avg_Ebath` (v meV) vpišemo v stolpce `E_4ps_meV`, `E_40ps_meV` in `E_400ps_meV` ter skripto zaženemo znova.

## Pričakovani rezultati (Avg_Ebath, meV)

| Vezje | 4 ps | 40 ps | 400 ps |
|---|---|---|---|
| Pudi, klasična | 3,40 | 1,16 | 0,94 |
| Pudi, Torres | 2,87 | 0,34 | 0,093 |
| Wang, klasična | 4,49 | 1,85 | 1,59 |
| Wang, Torres | 3,33 | 0,37 | 0,080 |
| Ahmad in sod. | 3,29 | 1,79 | 1,66 |
| Seyedi in J. N. | 0,76 | 0,64 | 0,62 |

Ker simulator celice obdeluje v naključnem vrstnem redu, se lahko ponovljene vrednosti nekoliko razlikujejo.

## Viri

- W. Wang, K. Walus, G. A. Jullien. *Quantum-dot cellular automata adders.* IEEE-NANO 2003, vol. 2, str. 461–464. [doi:10.1109/NANO.2003.1231818](https://doi.org/10.1109/NANO.2003.1231818)
- V. Pudi, K. Sridharan. *Low complexity design of ripple carry and Brent–Kung adders in QCA.* IEEE Transactions on Nanotechnology 11(1), 105–119, 2012. [doi:10.1109/TNANO.2011.2158006](https://doi.org/10.1109/TNANO.2011.2158006)
- F. Sill Torres, P. Niemann, R. Wille, R. Drechsler. *Near zero-energy computation using quantum-dot cellular automata.* ACM Journal on Emerging Technologies in Computing Systems 16(1), čl. 11, 2019. [doi:10.1145/3365394](https://doi.org/10.1145/3365394)
- F. Ahmad, S. Ahmed, V. Kakkar, G. M. Bhat, A. N. Bahar, S. Wani. *Modular design of ultra-efficient reversible full adder-subtractor in QCA with power dissipation analysis.* International Journal of Theoretical Physics 57(9), 2863–2880, 2018. [doi:10.1007/s10773-018-3806-3](https://doi.org/10.1007/s10773-018-3806-3)
- S. Seyedi, N. Jafari Navimipour. *Designing a multi-layer full-adder using a new three-input majority gate based on quantum computing.* Concurrency and Computation: Practice and Experience 34(4), e6653, 2022. [doi:10.1002/cpe.6653](https://doi.org/10.1002/cpe.6653)
- F. Sill Torres, R. Wille, P. Niemann, R. Drechsler. *An energy-aware model for the logic synthesis of quantum-dot cellular automata.* IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems 37(12), 3031–3041, 2018. [doi:10.1109/TCAD.2018.2789782](https://doi.org/10.1109/TCAD.2018.2789782) (QCADesigner-E)
