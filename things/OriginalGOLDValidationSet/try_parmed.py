import parmed as pmd
import pytraj as pt

# x = pmd.load_file('ligand_with_h.mol2', structure=True)
x = pmd.load_file('ligand_with_h.mol2', structure=False)
print(x)
# x = pt.load('ligand_with_h.mol2')
