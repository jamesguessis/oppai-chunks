import sys
import pyttanko
import matplotlib.pyplot as plt

def get_strains(objs, interval=500, length=3000):
    speed, aim, total = [], [], []
    seek = 0
    while seek <= objs[-1].time:
        window = [obj for obj in objs if (obj.time >= seek and obj.time <= seek + length)]
        wspeed, waim, wtotal = [], [], []
        for strain in [obj.strains for obj in window]:
            wspeed.append(strain[0])
            waim.append(strain[1])
            wtotal.append(sum(strain))
        speed.append(sum(wspeed) / max(len(window), 1))
        aim.append(sum(waim) / max(len(window), 1))
        total.append(sum(wtotal) / max(len(window), 1))
        seek += interval
    return speed, aim, total

def get_pyttanko(bmap_file, mods:int):
    bmap = pyttanko.parser().map(open(bmap_file))
    stars = pyttanko.diff_calc().calc(bmap, mods=mods)
    return bmap

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        mods = int(sys.argv[2]) if len(sys.argv) > 2 else 0
        bmap = get_pyttanko(sys.argv[1], mods)
    else:
        sys.stderr.write("You need to provide a path to a .osu\n")
        sys.exit()
    sys.stdout.write("Analyzing beatmap...\n")
    speed, aim, total = get_strains(bmap.hitobjects)
    numobjs = len(speed)
    plt.plot(range(numobjs), speed)
    plt.plot(range(numobjs), aim)
    plt.plot(range(numobjs), total)
    plt.show()
