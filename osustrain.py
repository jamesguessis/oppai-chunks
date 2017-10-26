#!/usr/bin/python3.5
import sys
import pyttanko
import matplotlib.pyplot as plt

def get_strains(bmap_file, mods:int=0):
    """Uses strain values from each hitobject 
    to create lists of strains in a way 
    I see fit"""
    bmap = get_pyttanko(bmap_file, mods)
    speed, aim, total, times = [], [], [], []
    seek = 0
    while seek <= bmap.hitobjects[-1].time:
        window = []
        for obj in bmap.hitobjects:
            if (obj.time >= seek and obj.time <= seek + 30000):
                window.append(obj.strains)
        wspeed, waim, wtotal = [], [], []
        for strain in window:
            wspeed.append(strain[0])
            waim.append(strain[1])
            wtotal.append(sum(strain))
        speed.append(sum(wspeed) / max(len(window), 1))
        aim.append(sum(waim) / max(len(window), 1))
        total.append(sum(wtotal) / max(len(window), 1))
        times.append(seek)
        seek += 500
    return speed, aim, total, times

def graph(bmap_file, mods:int=0):
    """Creates a graph of the strains over time"""
    speed, aim, total, times = get_strains(bmap_file, mods)
    numobjs = len(speed)
    plt.plot(range(numobjs), speed)
    plt.plot(range(numobjs), aim)
    plt.plot(range(numobjs), total)
    plt.show()

def get_pyttanko(bmap_file, mods:int):
    """Uses pyttanko to parse the map 
    each hitobject contains the strain values. 
    Thanks Francesco"""
    bmap = pyttanko.parser().map(open(bmap_file))
    stars = pyttanko.diff_calc().calc(bmap, mods=mods)
    return bmap

if __name__ == '__main__':
    """Graphs the strains using matplotlib"""
    if len(sys.argv) < 2:
        sys.stderr.write("You need to provide a path to a .osu\n")
        sys.exit()
    mods = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    sys.stdout.write("Analyzing beatmap...\n")
    speed, aim, total, times = get_strains(sys.argv[1], mods)
    for i in range(len(speed)):
        sys.stdout.write('{:>8}: {:>8} |{:>8} |{:>8}\n'.format(times[i], 
                                                               round(speed[i], 2), 
                                                               round(aim[i], 2), 
                                                               round(total[i], 2)))

