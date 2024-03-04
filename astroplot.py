import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

def astroplot(data,percentiles=[1,99.5],cmap='viridis',ax=None,
              offset=0,norm=None,figsize=(5,5),title=None,set_bad='r'):
    if (data is None) or np.isnan(data).all():
        raise ValueError('Data is empty!')
    if ax is None:
        fig, ax = plt.subplots(1,1,figsize=figsize)

    # auto-normalize data in log scale 
    # (and take care of the negative values if needed)       
    if norm is None:
        vmin,vmax = np.nanpercentile(data,percentiles)
        if vmin <= 0:
            offset = -vmin + 1e-1 # never make it zero
        else:
            offset = 0
        vmin += offset 
        vmax += offset
        norm = LogNorm(vmin=vmin,vmax=vmax)
    else:
        assert offset is not None, 'offset has to be provided if norm is provided'

    # plot
    clipped_data = data.copy() + offset
    clipped_data[clipped_data<=norm.vmin] = norm.vmin
    clipped_data[clipped_data>=norm.vmax] = norm.vmax
    if isinstance(cmap, str):
        cmap = plt.get_cmap(cmap)
        cmap.set_bad(set_bad)
    ax.imshow(clipped_data,norm=norm,cmap=cmap,origin='lower')
    ax.set_yticks([])
    ax.set_xticks([])
    if title is not None:
        ax.set_title(title,fontsize=13)
    return norm,offset
