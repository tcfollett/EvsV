import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('Fe3C_mp-510623_222_fixed_EvsV.out', skiprows=3)
vol, energy = data[:,1], data[:,2]

plt.plot(vol, energy, 'o-')
plt.xlabel('Volume per atom (Å³)')
plt.ylabel('Energy per atom (eV)')
plt.title('Fe3C EvsV — MTP potential')
plt.tight_layout()
plt.savefig('Fe3C_EvsV.png', dpi=150)
