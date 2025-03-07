import numpy as np
from astropy.io import fits

co = fits.open("location.fits")[0]
codata = co.data
cohdr = co.header

# resizing the co data

shape_out = (cohdr['NAXIS2'],cohdr['NAXIS1'])

newsize = (250, 250)
padded_co = np.zeros(newsize)

offset_x = (newsize[0] - shape_out[0]) // 2
offset_y = (newsize[1] - shape_out[1]) // 2

padded_co[offset_x:offset_x+shape_out[0], offset_y:offset_y+shape_out[1]] = codata

cohdr['NAXIS2'],cohdr['NAXIS1'] = 250, 250    #x, y dimensions

cohdr["CRPIX1"] = cohdr["CRPIX1"] + offset_x     # ref pixel x axis
cohdr["CRPIX2"] = cohdr["CRPIX2"] + offset_y     # ref y axis
