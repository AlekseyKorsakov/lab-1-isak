import cv2
import module1


C_1 = 42.26689294300924, 2.959098815917969, 'Figueres'
C_2 = 41.36031866306708, 2.1148681640625004, 'Barcelona'
C_3 = 42.53689200787317, 1.5710449218750002, 'Andorra'


PIC = cv2.imread('LE07_L1TP_197031_20000810_20170210_01_T1_B1.TIF')
MTL = 'LE07_L1TP_197031_20000810_20170210_01_T1_MTL.txt'
pixel_corners = [[1523,15],[7772,1237],[6294,7192],[49,5960]]


GEO_UL = module1.getFromMTL('CORNER_UL_LAT_PRODUCT',MTL), module1.getFromMTL('CORNER_UL_LON_PRODUCT',MTL)
GEO_UR = module1.getFromMTL('CORNER_UR_LAT_PRODUCT',MTL), module1.getFromMTL('CORNER_UR_LON_PRODUCT',MTL)
GEO_LL = module1.getFromMTL('CORNER_LL_LAT_PRODUCT',MTL), module1.getFromMTL('CORNER_LL_LON_PRODUCT',MTL)
GEO_LR = module1.getFromMTL('CORNER_LR_LAT_PRODUCT',MTL), module1.getFromMTL('CORNER_LR_LON_PRODUCT',MTL)


lat_d = abs((GEO_UL[0] + GEO_UR[0]) / 2 - (GEO_LL[0] + GEO_LR[0]) / 2)
lon_d = abs((GEO_UL[1] + GEO_LL[1]) / 2 - (GEO_UR[1] + GEO_LR[1]) / 2)


def draw(city,img):

    k1 = abs((abs((GEO_UL[1] + GEO_LL[1]) / 2) - abs(city[1])) / lon_d)

    k2 = abs((city[0] - (GEO_LL[0] + GEO_LR[0]) / 2) / lat_d)

    p = int(module1.get_p(pixel_corners[0], pixel_corners[1], k1)[0] -600), int(module1.get_p(pixel_corners[3], pixel_corners[0], k2)[1] + 550 )

    img = cv2.circle(img, p, 750, (255,255,255), 10)

    cv2.putText(img, city[2], (p[0] - 550, p[1]), cv2.FONT_HERSHEY_SIMPLEX, 8, (255, 255, 255), 10)

    return img

img = draw(C_1,PIC)
img = draw(C_2,PIC)
img = draw(C_3,PIC)

module1.show(img)



