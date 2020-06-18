import socket
import cv2

from servers import cam_server

# Computer IP address.
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)

port_cam = 5000

# Creates and starts a UDP camera server(socket) to receive from the Raspberry Pi.
server_cam = cam_server.CameraServer(host_ip, port_cam)
server_cam.start_server()


try:
    while(True):

        # Requesting frame from RC Car
        frame = server_cam.get_frame()

        if frame is None:
            print("No frame received")

        else:
            # frame = cv2.resize(frame, (0, 0), fx=2, fy=2)
            cv2.imshow("RC Car raw frame", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break



finally:
    server_cam.close_server()

    cv2.destroyAllWindows()
    