import parmed as pmd
import sanderles
from random import shuffle


pme_input = sanderles.pme_input()

def get_energy(tn, rst7):
    parm = pmd.load_file(tn, rst7)
    print(parm)
    with sanderles.setup(parm, parm.coordinates,
            box=parm.box, mm_options=pme_input) as context:
        ene, _ = context.energy_forces()
        print(ene.tot)

tn, rst7 = "4lztab.parm7", "4lztabH.rst7"
get_energy(tn, rst7)

# reorder atoms
parm = pmd.load_file(tn, rst7)
indices = list(range(len(parm.atoms)))
print(len(parm.atoms))
print(len(indices))
shuffle(indices)
print(indices[:10])

nparm = parm[indices]
nparm.save('new.parm7', overwrite=True)
nparm.save('new.rst7', overwrite=True)

tn, rst7 = 'new.parm7', 'new.rst7'
get_energy(tn, rst7)
