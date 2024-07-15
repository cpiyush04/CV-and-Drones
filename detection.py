import numpy as np
import cv2



def pose_estimation(frame, aruco_dict_type, matrix_coefficients, distortion_coefficients):

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	arucoDict=cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
	arucoParams=cv2.aruco.DetectorParameters()
	detector = cv2.aruco.ArucoDetector(arucoDict, arucoParams)
	corners, ids, rejected_img_points = detector.detectMarkers(gray)
	   	 
	if len(corners) > 0:
		for i in range(0, len(ids)):
			marker_size = 50
			marker_corners = corners[i][0].astype(np.float32)
			objp = np.array([[0, 0, 0],
                             [marker_size, 0, 0],
                             [marker_size, marker_size, 0],
                             [0, marker_size, 0]], dtype=np.float32)
			_,rvec, tvec = cv2.solvePnP(objp, marker_corners, matrix_coefficients, distortion_coefficients)
			#rvec, tvec, markerPoints = cv2.aruco.estimatePoseSingleMarkers(corners[i], 50, matrix_coefficients,distortion_coefficients)
			cv2.aruco.drawDetectedMarkers(frame, corners)
			cv2.drawFrameAxes(frame, matrix_coefficients, distortion_coefficients, rvec, tvec, 5)
			print(tvec)
	return frame

img=cv2.imread("marker0.png")
h,w,_=img.shape
width=1000
height=int(width*(h/w))
img=cv2.resize(img,(width,height),interpolation=cv2.INTER_CUBIC)
intrinsic_camera = np.array(((216.59801131,0.,313.74473864),( 0., 270.66544048,238.11774055),(0.,0.,1.)))
distortion = np.array(( 0.02327178, -0.08459351,  0.00155897, -0.00124459,  0.09113074))

detected_markers=pose_estimation(img,cv2.aruco.DICT_4X4_50,intrinsic_camera,distortion)
# corners,ids,rejected=cv2.aruco.detectMarkers(img,arucoDict,parameters=arucoParams)
# detected_markers=aruco_display(corners,ids,rejected,img)
cv2.imshow("Image",detected_markers)
cv2.waitKey(0)
cv2.destroyAllWindows()
