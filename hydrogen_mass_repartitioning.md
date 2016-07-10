- Update your topology file

```bash
parmed old.parm7 parm.in
```

```bash
$ cat parm.in
HMassRepartition
outparm new.4fs.parm7
```

- Use `dt=0.004`

md.in example
```bash
lengevin dynamics simulations
&cntrl
   ntx = 1, irest=0,
   imin = 0, nstlim = 5000000, dt = 0.004,
   ntt = 3, gamma_ln=1., temp0 = 300.0, tempi=300.,
   ntc= 2, ntf = 2,
   igb=8, ntb = 0,
   ntwx = 5000, ntwe = 0, ntwr = 5000, ntpr = 5000,
   cut = 999.0,
   nscm = 5000,
&end
```

- run md: Use **new.parm7**

```bash
pmemd -O -p new.parm7 -c rst7_file -i md.in
```
