import cv2

def scan_barcode():
    cap = cv2.VideoCapture(0)  # Open the camera
    detector = cv2.QRCodeDetector()

    while True:
        ret, frame = cap.read()
        if not ret:
            print("❌ Failed to capture frame")
            break

        # Detect and decode barcode
        data, bbox, _ = detector.detectAndDecode(frame)

        if data:  # If barcode is detected
            barcode_number = data.strip()  # Trim any extra spaces
            cap.release()
            cv2.destroyAllWindows()
            return barcode_number  

        cv2.imshow("Barcode Scanner", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
    return None