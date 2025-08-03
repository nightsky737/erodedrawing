from landlab import RasterModelGrid
from scipy.ndimage import gaussian_filter
import numpy as np
import random
from landlab.components import FlowAccumulator, FastscapeEroder
def make_gradient(np_array, diff):
    #diff is the difference between the highest and lowest point.
    #So we have like uh 
    scale_factor = diff / (np_array.shape[1] + np_array.shape[0] - 1) 
    for i in range(np_array.shape[0]):
        for j in range(np_array.shape[1]):
            # np_array[i][j] -= (i + j + random.randint(0, int((np_array.shape[0] + np_array.shape[1]) / 1000))) * dz
            np_array[i][j] -= ((i + j)) *  scale_factor * random.randint(95, 105) / 100

def overlay_img(np_img, diff=50):
    terrain = np.zeros(np_img.shape[:2])
    make_gradient(terrain, diff)
    
    grayscale = np_img[:,:,0]
    blacks = grayscale < 255
    carved_idxs = np.zeros_like(terrain)
    for i in range(1, grayscale.shape[0]- 1):
        for j in range(1, grayscale.shape[1] - 1):
            if blacks[i, j]:
                scale = (1 + (i + j) / ( 1.5 * (terrain.shape[0] + terrain.shape[1])))
                # terrain[i-2 : i + 2, j - 2 : j + 2] -=  scale * diff * 0.8
                carved_idxs[i-1 : i + 1, j - 1 : j + 1] =  -scale * diff * 0.8 + terrain[i, j] 
                carved_idxs[i, j] =  -scale * diff * 0.2+ terrain[i, j] 
    terrain = terrain + carved_idxs
    terrain = gaussian_filter(terrain, sigma=5)

    return terrain#[::-1, :]

def make_simulation(overlayed_img):
    raster_grid = RasterModelGrid(overlayed_img.shape, 1)
    raster_grid.add_field("topographic__elevation", overlayed_img.flatten(), at="node") #can also get spacial coords of the r,c dataset by .index(x, y)
    flow_accumulator = FlowAccumulator(raster_grid, "topographic__elevation", flow_director="D8") #flow accumulator basically sets all of the nodes in the grid to point somewhere it is going to drain down.
    eroder = FastscapeEroder(raster_grid, K_sp=0.001, m_sp=0.55, n_sp=1.1)
    return raster_grid, flow_accumulator, eroder
    
def run_simulation(flow_accumulator, eroder):
    for _ in range(20):
        flow_accumulator.run_one_step() #apparently landlab tried to make everything similar (ie all run one step)
        eroder.run_one_step(100) #the param is how many years it runs at once.
