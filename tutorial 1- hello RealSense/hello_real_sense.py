########################################################################
#TUTORIAL: HELLO REALSENSE
#This tutorial checks to see if the RealSense camera is plugged in 
########################################################################
import pyrealsense2 as rs

def main():
    #Create camera object using default configuration
    pipeline = rs.pipeline()
    ctx = rs.context()

    #Check to see if RealSense device is connected
    #query_devices() returns a list of devices!
    if(len(ctx.query_devices()) == 0):
        print("RealSense device not detected")
        exit(1)
    #Start streaming the camera 
    pipeline.start()

    #Camera operations added here (examples in other tutorials)

    #Print out device name and serial number
    #This line assumes only one RealSense device is connected
    #If more than one device is connected, use a for loop to iterate through list
    print(ctx.query_devices()[0].get_info(rs.camera_info.name),
          ctx.query_devices()[0].get_info(rs.camera_info.serial_number))

    #Stop the camera from running *IMPORTANT*
    pipeline.stop()

if __name__ == "__main__":
    main()
