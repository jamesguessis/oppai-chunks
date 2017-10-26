# oppai-chunks
Originally forked from [here](https://github.com/derekxwu/oppai-chunks) to use pyoppai for a massive speed boost. 
Now I've rewritten it to use pyttanko with strains instead of difficulty.

Runs on Python 3 and uses [pyttanko](https://github.com/Francesco149/pyttanko)

## Usage:

### From the command line
`./oppai_chunks.py beatmap [mod bitwise]`

`beatmap` is the .osu file you want to analyze.

`mod bitwise` is the bitwise for the mod combination(s) you want to apply.

For example, `./oppai_chunks.py "haitai.osu" 24` will calculate the strains for the map with HDHR.

### As a python module
```
from oppai_chunks import get_strains
...
get_strains(beatmap, mods=24)
```
The arguments are the same as above. Here, the beatmap can be given as a path (`oppai('/path/to/beatmap.osu')`). The output is a list of `(time, overall stars, aim stars, speed stars)` tuples.
