# import required libraries
from vidgear.gears import NetGear
import cv2

# activate Multi-Clients mode
options = {"multiclient_mode": True}

# Define NetGear Client at Server's IP address and assign a unique port address and other parameters
# !!! change following IP address '192.168.x.xxx' with yours !!!
client = NetGear(
    address="192.168.1.197",
    port="5555",
    protocol="tcp",
    pattern=2,
    receive_mode=True,
    logging=True,
    # **options
) 

# loop over
while True:
    # receive data from server
    frame = client.recv()

    # check for frame if None
    if frame is None:
        break

    # {do something with frame here}

    # Show output window
    cv2.imshow("Client 5555 Output", frame)

    # check for 'q' key if pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

# close output window
cv2.destroyAllWindows()

# safely close client
client.close()