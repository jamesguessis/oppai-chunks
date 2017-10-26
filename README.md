# osu-strain
Originally forked from [oppai-chunks](https://github.com/derekxwu/oppai-chunks) to use pyoppai for a massive speed boost. 
Now I've rewritten it to use pyttanko with strains instead of difficulty.

Runs on Python 3 and uses [pyttanko](https://github.com/Francesco149/pyttanko)

## Usage:

### From the command line
`./osustrain.py beatmap [mod bitwise]`

`beatmap` is the .osu file you want to analyze.

`mod bitwise` is the bitwise for the mod combination(s) you want to apply.

For example, `./osustrain.py "haitai.osu" 24` will provide the strains for the map with HDHR.

Output are each chunks strain values for speed and aim with the sum of the two.

### As a python module
```
from osustrain import get_strains
...
get_strains(beatmap, mods=24)
```

You can also graph the strains instead.
```
from osustrain import get_strains
...
graph(beatmap, mods=24)
```

The arguments are the same as above. Here, the beatmap should be given as a path (`osustrain('/path/to/beatmap.osu')`). The outputs are four lists for the seperate strains for speed, aim, the sum of the two, and the time in milliseconds of which the chunk starts.