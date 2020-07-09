import socket
import cv2


import cam_handler
import sensor_handler
import controller_handler

RUN_SENSOR_SERVER = 0
RUN_CONTROLLER_SERVER = 1

DISPLAY_FPS = 1
DISPLAY_DISTANCE = 1  # Whether to display the distance received from the infrared sensor on the pi.
CAM_PRINT_LOGS = 0  # Whether to print camera connection logs.


COLLECT_DATA = 1  #  Whether to collect/capture data for training.


# Getting computer IP address.
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)

port_cam = 5000
port_sensor = 5001
port_controller = 5002

handler_cam = cam_handler.CamHandler(host_ip, port_cam, CAM_PRINT_LOGS)
handler_sensor = sensor_handler.SensorHandler(host_ip, port_sensor, RUN_SENSOR_SERVER)
handler_controller = controller_handler.ControllerHandler(host_ip, port_controller, RUN_CONTROLLER_SERVER)



try:
    while(True):

        # Requesting/getting the frame from the pi.
        frame = handler_cam.get_frame()

        if frame is None:  # Ensuring a frame was received and processed successfully.
            continue

        if DISPLAY_FPS: frame = handler_cam.display_fps(frame)
        

        # Getting the infrared sensor distance from the pi.
        distance = handler_sensor.get_distance()
        if DISPLAY_DISTANCE: frame = handler_sensor.display_distance(frame)




        cv2.imshow("RC Car frame", frame)

        if cv2.waitKey(1) == ord('q'):
            break


        # To control the car using the keyboard and to collect training data if needed.
        handler_controller.process_key_pressed(COLLECT_DATA)  # TODO: Possibly a different name for this method.

        # if COLLECT_DATA:
        #     handler_controller.collect_data(frame, key)
        

finally:

    if COLLECT_DATA:
        handler_controller.save_collected_data()

    handler_cam.server_cam.close_server()

    if RUN_SENSOR_SERVER:
        handler_sensor.server_sensor.close_server()
    if RUN_CONTROLLER_SERVER:
        handler_controller.server_controller.close_server()
        handler_controller.close_controller_window()

    cv2.destroyAllWindows()

