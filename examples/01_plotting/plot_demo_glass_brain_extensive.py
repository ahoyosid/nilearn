"""
Glass brain plotting in nilearn (all options)
=============================================

This example goes through different options of the :func:`nilearn.plotting.plot_glass_brain` function
(including plotting negative values). 
See :ref:`plotting` for more plotting functionalities.
"""


###############################################################################
# Retrieve the data
from nilearn import datasets

localizer_dataset = datasets.fetch_localizer_contrasts(
    ["left vs right button press"],
    n_subjects=2,
    get_tmaps=True)
localizer_tmap_filename = localizer_dataset.tmaps[1]

###############################################################################
# demo glass brain plotting.
from nilearn import plotting

# Whole brain sagittal cuts
plotting.plot_glass_brain(localizer_tmap_filename, threshold=3)

plotting.plot_glass_brain(localizer_tmap_filename, threshold=3, colorbar=True)

plotting.plot_glass_brain(localizer_tmap_filename, title='plot_glass_brain',
                          black_bg=True, display_mode='xz', threshold=3)

plotting.plot_glass_brain(localizer_tmap_filename, threshold=0, colorbar=True,
                          plot_abs=False)

plotting.plot_glass_brain(localizer_tmap_filename, threshold=3,
                          colorbar=True, plot_abs=False)

###############################################################################
# Hemispheric sagittal cuts

title = 'plot_glass_brain with display_mode="lzr"'
plotting.plot_glass_brain(localizer_tmap_filename, title=title,
                          black_bg=True, display_mode='lzr', threshold=3)

title = 'plot_glass_brain with display_mode="lyrz"'
plotting.plot_glass_brain(localizer_tmap_filename, threshold=0, colorbar=True,
                          title=title, plot_abs=False, display_mode='lyrz')

plotting.show()
