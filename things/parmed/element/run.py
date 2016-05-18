import parmed as pmd

print(pmd.__version__)

parm = pmd.load_file("08Z.mol2", structure=True)
print(parm.atoms[0])
print(parm.atoms[0].element)
