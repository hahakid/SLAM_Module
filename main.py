import os
import glob
import time
import numpy as np
import KITTIReader as reader
import utils
import preProcessor
from mayavi import mlab

infile_path = os.path.join("00", "velodyne", "*.bin")
file_list = sorted(glob.glob(infile_path))
#print(file_list)

#for raw_data in reader.yield_velo_scans(file_list[0]):
raw_data = reader.load_velo_scan(file_list[0])
#print(raw_data.shape[0])
preProcess = preProcessor.preProcessor()

#utils.plot_pointClouds(preProcess.get_rawPointCloud())
#utils.plot_pointClouds(preProcess.ground_filter_linefit(raw_data, 15))
utils.plot_pointClouds(preProcess.ground_filter_heightDiff(raw_data, 400, 400, 0.3, 0.5))