import cv2
import numpy as np
import matplotlib.pyplot as plt 

def interactive_edge_detection(image_path):
    
    
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Image not found!")
        return

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    display_image("Original Grayscale Image", gray_image)
 
    print("\nSelect an option:")
    print("1. Sobel Edge Detection")
    print("2. Canny Edge Detection")
    print("3. Laplacian Edge Detection")
    print("4. Gaussian Smoothing")
    print("5. Median Filtering")
    print("6. Exit")

    while True:
       

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            sobelx = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=5)
            sobely = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=5)
            sobel = cv2.magnitude(sobelx, sobely)
            sobel = np.uint8(np.clip(sobel, 0, 255))
            display_image("Sobel Edge Detection", sobel)

        elif choice == '2':
            threshold1 = int(input("Enter threshold1 for Canny: "))
            threshold2 = int(input("Enter threshold2 for Canny: "))
            canny = cv2.Canny(gray_image, threshold1, threshold2)
            display_image("Canny Edge Detection", canny)

        elif choice == '3':
            laplacian = cv2.Laplacian(gray_image, cv2.CV_64F)
            laplacian = np.uint8(np.clip(np.absolute(laplacian), 0, 255))
            display_image("Laplacian Edge Detection", laplacian)

        elif choice == '4':
            ksize = int(input("Enter kernel size for Gaussian blur (odd number): "))
            gaussian = cv2.GaussianBlur(gray_image, (ksize, ksize), 0)
            display_image("Gaussian Smoothing", gaussian)

        elif choice == '5':
            ksize = int(input("Enter kernel size for Median filter (odd number): "))
            median = cv2.medianBlur(gray_image, ksize)
            display_image("Median Filtering", median)

        elif choice == '6':
            print("Exiting.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")
