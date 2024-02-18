# LNPackager

### By Genius_um / [MazeGroup](http://mazegroup.rf.gd/) - 2023

`Version 0.0.1`

---

LNPackager is a Python Module for make Neuronnal Nodes

and make Package for train they.

---
# Import in your code lnpackager
```py
import lnpackager as lnp
# Put lnpackager.py in Python Libs files or in the same folder your program
```

And make a package instance, train it and save it :

Exemple :

```py
package = lnp.LNPackage("package_file", "ctr", lnp.MultiplesNodes(), 5, 500) # Init Package Class
package.train() # Train Nodes
package.make() # Save Package File
```

---

Functions and Classes Docs : 

- Package class.

  Learning types :

  - ctr (Check To Result)

  More your attemps and nodes numbers

  is big, more is your waiting time.*

- A node as a value and a marge value.

    At a generation, this value change

    for a random value between the marge.

- At a generation, the value change

  for a random value between the marge.
  
- You can make multiples nodes

    with this function and choose
    
    there values and marges.
- Training : you can log the

  advencement of your train but

  it's more low.

  CTR Method Training :

  - For attemps:
      - For nodes:
          - Generate nodes values

          - Choose random operator

          - Result calculated with operator*

- Make .lnp package file

    Syntax :
    ```text
    l-type-<training type>;valid-result:<valid result>;attemps:<attemps>;
    (!<node initial value>;~<node marge>;)<...>
    [[!<node value generated>;#<random operator>;?<result>;]<... * Nodes numbers>]<...>
    ```
