from landlab import RasterModelGrid
from landlab.io import esri_ascii
from landlab.utils.add_halo import add_halo
import numpy as np
import rasterio
import rasterio.features
import rasterio.warp



#     mg = esri_ascii.load(fp, name="topographic__elevation", at="node")
# z = mg.at_node["topographic__elevation"]

# mg.imshow("topographic__elevation")


# min_z = np.min(z[np.where(z > 0)]) 
# max_z = np.max(z[np.where(z > 0)])

# mg.imshow("topographic__elevation", limits=(min_z, max_z)) #basically heatmaps it. the color mapping stuff is limtis