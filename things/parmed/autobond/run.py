import pytraj as pt, parmed as pmd

fn = '2pia_2pia1423_0001.pdb'

traj = pt.load(fn)
parm = pmd.load_file(fn)

print("parmed")
print(len(parm.bonds))

print("cpptraj")
traj.top.summary()
