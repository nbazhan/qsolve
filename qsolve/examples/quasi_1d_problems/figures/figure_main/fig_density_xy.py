import numpy as np


class fig_density_xy(object):

    def __init__(self, ax, settings):
        
        Jx = settings.Jx
        Jy = settings.Jy

        ax.set_xlabel(settings.label_x)
        ax.set_ylabel(settings.label_y)
        
        ax.set_xticks(settings.y_ticks)
        ax.set_yticks(settings.x_ticks)
        
        ax.set_anchor('W')

        density_xy = np.zeros((Jx, Jy))
        
        self.image_density_xy = ax.imshow(density_xy,
                                          extent=[settings.y_min, settings.y_max, settings.x_min, settings.x_max],
                                          cmap=settings.colormap_density,
                                          aspect='equal',
                                          interpolation='bilinear',
                                          vmin=0,
                                          vmax=1,
                                          origin='lower')

    def update(self, density_xy):

        self.image_density_xy.set_data(density_xy)
