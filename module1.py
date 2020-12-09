def getFromMTL(name,MTL):
    f = open(MTL).readlines()

    for i in iter(f):
        if name in i:

            original = i[4:]

            return float(original.replace(name + " = ", ""))

def get_p(p1,p2,z):
    z = z / (1 - z)
    if z <= 0.5:
        return int((p1[0] + z * p2[0]) / (1 + z)),int((p1[1] + z * p2[1]) / (1 + z))
    else:
        z = 1 / z
        return int((p2[0] + z * p1[0]) / (1 + z)),int((p2[1] + z * p1[1]) / (1 + z))

def show(output):
    import cv2
    screen_res = 1000, 1000
    scale_width = screen_res[0] / output.shape[1]
    scale_height = screen_res[1] / output.shape[0]
    scale = min(scale_width, scale_height)
    window_width = int(output.shape[1] * scale)
    window_height = int(output.shape[0] * scale)

    cv2.namedWindow('Window1', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Window1', window_width, window_height)

    cv2.imshow('Window1', output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()