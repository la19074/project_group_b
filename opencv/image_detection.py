#!/usr/bin/env python3
'''
This file contains a class for the image detection system, including all memory elements
and functions needed to fetch the position of the checkpoints and the ball. Remember to
disable the display functions to save processing power!
'''

# Import modules.
import cv2
import numpy as np
from time import perf_counter
import matplotlib.pyplot as plt # For generating images.

class ImageProcessor():

	def __init__(self, StartTime, MazeSize, HSVLimitsBlue, HSVLimitsGreen):
		# Initialise values.
		self.LastInitialPoints = np.float32([[82, 34], [574, 35], [562, 440], [88, 436]]) # Initial points for perspective correction.
		self.LastPosition = np.array([False, False])
		self.StartTime = StartTime
		self.LastTime = StartTime

		# Initialise settings.
		self.MazeSize = MazeSize # Load the maze's size.
		self.HSVLimitsBlue = HSVLimitsBlue # Upper and lower HSV limits for the blue ball.
		self.HSVLimitsGreen = HSVLimitsGreen # Upper and lower HSV limits for the green frame.
		self.CameraMatrix = np.int32([[500.58972602, 0, 322.3603059], [0, 500.2860463, 255.41210124], [0, 0, 1]]) # Calculated using calibration script.
		self.DistortionCoefficients = np.int32([[0.16793948, -0.03380622, -0.00421432,  0.00209455, -1.29781314]]) # Calculated using calibration script.
		self.EpsilonMultiple = 0.1 # Affects how accurately contour corners are detected.
		self.KernelBlur = (7, 7) # How much to blur the image by.
		self.WaitTime = 1 # [s] Maximum time allowed while ball cannot be found.

	def __repr__(self):
	    # Makes the class printable.
	    return "Image Detector(Last Ball Position: %s, Time Detected: %s)" % (self.LastPosition, round(self.StartTime, 2))

	def order_points(self, Points):
		# Orders four points clockwise from the top left corner.
		XSorted = Points[np.lexsort((Points[:,1], Points[:,0]))] # Sort the points by their x-coordinates.
		LeftPoints = XSorted[:2] # The two leftmost points are the first two in XSorted.
		LeftYSorted = LeftPoints[np.lexsort((LeftPoints[:,0], LeftPoints[:,1]))] # Sort these two points by their y-coordinates.
		RightPoints = XSorted[2:] # The two rightmost points are the last two in XSorted.
		RightYSorted = RightPoints[np.lexsort((RightPoints[:,0], RightPoints[:,1]))] # Sort these two points by their y-coordinates.
		OrderedPoints = np.float32([LeftYSorted[0], RightYSorted[0], RightYSorted[1], LeftYSorted[1]]) # Order the points.
		return OrderedPoints

	def correct_perspective(self, ImageHSV):
		# Correct the maze's tilt perspective.
		Mask = cv2.inRange(ImageHSV, self.HSVLimitsGreen[0], self.HSVLimitsGreen[1]) # Use the lower and upper HSV limits to create a mask.
		MaskDilated = cv2.dilate(Mask, np.ones((3, 3)), iterations = 2) # Dilate and then erode to remove any black blobs in the frame mask.
		MaskEroded = cv2.erode(MaskDilated, np.ones((3, 3)), iterations = 2)
		Contours, Hierarchy = cv2.findContours(MaskDilated, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE) # Find all contours in the mask. Include simple hierarchy.

		if len(Contours) != 0:
			if len(Contours) == 1:
				ContourRect = Contours[0] # If there is only one contour found.
			else:
				MaxContour = max(Contours, key = lambda Contour: cv2.arcLength(Contour, True)) # Select the contour with the largest perimeter. (Assume the rect is the largest contour.)
				MaxContourIndex = Contours.index(MaxContour) # Find index of MaxContour.
				ContourRect = Contours[Hierarchy[0][MaxContourIndex][2]] # Use index and hierarchy to find the internal contour. (Refer to documentation.)

			Perimeter = cv2.arcLength(ContourRect, True) # Find the perimeter of ContourRect.
			#print("Rect Perimeter: " + str(Perimeter)) # Print the perimeter.
			if Perimeter > 1500: # Sanity check: the contour has to be a minimum perimeter.
				Corners = cv2.approxPolyDP(ContourRect, self.EpsilonMultiple * Perimeter, True) # Find the approximate corners of the contour.
				if len(Corners) == 4:
					Points = Corners[:, 0] # Set points as the four corners.
					InitialPoints = self.order_points(Points) # Order the points clockwise from the top left corner.
					self.LastInitialPoints = InitialPoints # Save the new points.
				else:
					InitialPoints = self.LastInitialPoints # If new points were not found, use the last set of points.
			else:
				InitialPoints = self.LastInitialPoints # If new points were not found, use the last set of points.
		else:
			InitialPoints = self.LastInitialPoints # If new points were not found, use the last set of points.

		TransformedPoints = np.float32([[0, 0], [self.MazeSize[0], 0], [self.MazeSize[0], self.MazeSize[1]], [0, self.MazeSize[1]]]) # Points to warp to.
		TransformationMatrix = cv2.getPerspectiveTransform(InitialPoints, TransformedPoints) # Generate matrix for transformation.
		ImageCorrected = cv2.warpPerspective(ImageHSV, TransformationMatrix, (self.MazeSize[0], self.MazeSize[1])) # Correct the perspective warp.

		# Uncomment below to display the results.
		#ImageResult = cv2.cvtColor(ImageHSV, cv2.COLOR_HSV2BGR) # Make a copy of the corrected image in RBG to draw the results on.
		#cv2.drawContours(ImageResult, Contours, -1, (255, 0, 0), 1) # Draw contours onto ImageResult in blue.
		#cv2.polylines(ImageResult, np.int32([InitialPoints]), True, (0, 255, 0), 1) # Draw the rect onto ImageResult in green.
		#self.display("Rect Results", ImageResult, Mask, MaskEroded, MaskDilated) # Display results.

		''' Plot images '''
		ImageColour = cv2.cvtColor(ImageHSV, cv2.COLOR_HSV2RGB) # Make a copy of the corrected image in RBG to draw the results on.
		ImageResult = cv2.cvtColor(MaskDilated, cv2.COLOR_GRAY2RGB)
		cv2.polylines(ImageResult, np.int32([InitialPoints]), True, (0, 255, 0), 2) # Draw the rect onto ImageResult in green.

		plt.figure(1) # Plot second figure.

		plt.subplot(221)
		plt.imshow(ImageColour)
		plt.tick_params(bottom = False, left = False, labelbottom = False, labelleft = False)
		plt.xlabel("(a) Blurred image")

		plt.subplot(222)
		plt.imshow(ImageResult)
		plt.tick_params(bottom = False, left = False, labelbottom = False, labelleft = False)
		plt.xlabel("(b) Processed mask, polygon detected")

		return ImageCorrected

	def ball_detection(self, ImageCorrected):
		# Detect ball position.
		Mask = cv2.inRange(ImageCorrected, self.HSVLimitsBlue[0], self.HSVLimitsBlue[1]) # Use the lower and upper HSV limits to create a mask.
		MaskEroded = cv2.erode(Mask, np.ones((3, 3)), iterations = 1) # Erode and dialate to remove any small blobs left.
		MaskDilated = cv2.dilate(MaskEroded, np.ones((3, 3)), iterations = 1)

		Contours = cv2.findContours(MaskDilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0] # Find all external contours in the mask.

		if len(Contours) > 0: # Check if any contours were found.
			MaxContour = max(Contours, key = lambda Contour: cv2.contourArea(Contour)) # Select the largest contour.
			#print("Ball Area: " + str(cv2.contourArea(MaxContour))) # Print the top down area of the largest contour.
			if cv2.contourArea(MaxContour) > 15: # Sanity check: the contour has to be a minimum size.
				EnclosingCircle = cv2.minEnclosingCircle(MaxContour) # Find the minumum enclosing circle arond the largest contour. Output: ((x, y), r).
				Centre = np.array([EnclosingCircle[0][0], EnclosingCircle[0][1]]) # Save position as the centre of the circle.
				BallFound = True
			else:
				BallFound = False
				Centre = None
		else:
			BallFound = False
			Centre = None

		# Uncomment below to display the results.
		#ImageResult = cv2.cvtColor(ImageCorrected, cv2.COLOR_HSV2BGR) # Make a copy of the corrected image in RBG to draw the results on.
		#cv2.drawContours(ImageResult, Contours, -1, (255, 0, 0), 1) # Draw contours onto ImageResult in blue.
		#try: cv2.circle(ImageResult, (round(Centre[0]), round(Centre[1])), 7, (0, 255, 0), 1) # Draw enclosing circle in green.
		#except: pass
		#self.display("Ball Results", ImageResult, Mask, MaskEroded, MaskDilated) # Display results.

		''' Plot images '''
		ImageColour = cv2.cvtColor(ImageCorrected, cv2.COLOR_HSV2RGB) # Make a copy of the corrected image in RBG to draw the results on.
		ImageResult = cv2.cvtColor(MaskDilated, cv2.COLOR_GRAY2RGB)
		try: cv2.circle(ImageResult, (round(Centre[0]), round(Centre[1])), 7, (0, 255, 0), 2) # Draw enclosing circle in green.
		except: pass

		plt.subplot(223)
		plt.imshow(ImageColour)
		plt.tick_params(bottom = False, left = False, labelbottom = False, labelleft = False)
		plt.xlabel("(c) Corrected image")

		plt.subplot(224)
		plt.imshow(ImageResult)
		plt.tick_params(bottom = False, left = False, labelbottom = False, labelleft = False)
		plt.xlabel("(d) Processed mask, enclosing circle")

		plt.show()

		return BallFound, Centre

	def display(self, WindowName, ImageResult, Mask, MaskEroded, MaskDilated):
		# Stacks images together and dispays them in one window.
		Img1 = np.hstack((ImageResult, cv2.cvtColor(Mask, cv2.COLOR_GRAY2BGR)))
		Img2 = np.hstack((cv2.cvtColor(MaskEroded, cv2.COLOR_GRAY2BGR), cv2.cvtColor(MaskDilated, cv2.COLOR_GRAY2BGR)))
		Img3 = np.vstack((Img1, Img2)) # Stack all images together. Convert to BGR if necessary.

		cv2.imshow(WindowName, Img3) # Draw all results.
		cv2.waitKey(0) # Wait until key is pressed.
		cv2.destroyWindow(WindowName)

	def position_buffer(self, CurrentTime, BallFound, Centre):
		# Outputs the last position of the ball for a short time if there is one, and if the ball cannot be found.
		if BallFound == True:
			Active = True
			Position = Centre
			self.LastTime = CurrentTime
			self.LastPosition = Position
		else:
			if CurrentTime - self.LastTime < self.WaitTime and np.any(np.equal(self.LastPosition, np.array([False, False]))) == False:
				Active = True
				Position = self.LastPosition
			else:
				Active = False
				Position = self.LastPosition
		return Active, Position

	def update(self, CurrentTime, Image):
		'''
		This function updates the position of the ball, it's output should be in the format of a
		tuple: Active, Position. Active should be a boolean value and should be set to True as long
		as the ball is still on the maze, and False when the ball has fallen through a hole. The
		Position of the Ball should be provided as np.array([x, y]). See objects.py for more information.
		Please remember that the y axis starts at the top left corner and increases as you go down
		the maze, opposite to a traditional coordinate system.
		'''

		#ImageUndistorted = cv2.undistort(Image, self.CameraMatrix, self.DistortionCoefficients, None) # Correct for lens distortion. Not used to save processing power.

		ImageBlurred = cv2.GaussianBlur(Image, self.KernelBlur, 0) # Blur image to remove high frequency noise.
		ImageHSV = cv2.cvtColor(ImageBlurred, cv2.COLOR_BGR2HSV) # Convert image to HSV format.

		ImageCorrected = self.correct_perspective(ImageHSV) # Correct the maze's tilt perspective.
		BallFound, Centre = self.ball_detection(ImageCorrected) # Try to detect the position of the ball.
		Active, Position = self.position_buffer(CurrentTime, BallFound, Centre) # Outputs the last position of the ball for a short time if the ball cannot be found.
		if BallFound == True:
			Position += np.array([28.5, 28]) # Add frame width and height.

		return Active, Position

def main():
	# For testing on a signle image.
	MazeSize = np.array([275, 230]) # [mm]
	HSVLimitsBlue = np.array([[70, 58, 0], [120, 201, 75]])
	HSVLimitsGreen = np.array([[22, 95, 23], [86, 248, 148]])
	ImageProcessor_ = ImageProcessor(perf_counter(), MazeSize, HSVLimitsBlue, HSVLimitsGreen)
	#LastTime = perf_counter()
	ImageProcessor_.update(perf_counter(), cv2.imread("111.jpg"))
	#TimeStep = perf_counter() - LastTime
	#print("TimeStep: " + str(TimeStep * 1000))

if __name__ == "__main__":
	main()
