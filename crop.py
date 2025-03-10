from astropy.io import fits
import numpy as np

co = fits.open("file.fits")[0]
codata = co.data
cohdr = co.header

shape_out = (cohdr['NAXIS2'],cohdr['NAXIS1'])


newsize = (64,64)

start_x = np.abs((newsize[0] - shape_out[0]) // 2)
start_y = np.abs((newsize[1] - shape_out[1]) // 2)

# Ensure indices are within bounds
start_x = max(start_x, 0)
start_y = max(start_y, 0)

endx = startx + newsize[0]
endy = starty + newsize[1]

cropped_codata = codata[start_x:end_x, start_y:end_y]

cohdr['NAXIS2'],cohdr['NAXIS1'] = 64, 64   #x, y dimensions

cohdr["CRPIX1"] = cohdr["CRPIX1"] - start_x     # ref pixel x axis
cohdr["CRPIX2"] = cohdr["CRPIX2"] - start_y     # ref y axis
