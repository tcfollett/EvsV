# Fe3C Stress-Strain Extraction

- Source log: `/Users/bomilly/Downloads/Fe3C_mp-510623_222_fixed_min_elastic.log`
- Stress is plotted as `sigma = -P` because LAMMPS reports the pressure tensor.
- Normal-strain panels use `epsilon = +/-0.002` from the elastic script.
- Shear panels use `gamma = +/-0.004` so the slope matches the script's reported `C44`, `C55`, and `C66` values.

| Constant | Deformation | Response | Slope (GPa) |
|---|---|---|---:|
| C11 | xx | pxx | 483.574 |
| C22 | yy | pyy | 519.799 |
| C33 | zz | pzz | 398.597 |
| C12 | xx | pyy | 226.663 |
| C13 | xx | pzz | 207.895 |
| C23 | yy | pzz | 175.503 |
| C44 | yz | pyz | 59.983 |
| C55 | xz | pxz | 68.819 |
| C66 | xy | pxy | 77.862 |
