import serial

def serial_communication(port,baudrate,timeout,datasize):
    """Serial Communication"""
    try:
        ser = serial.Serial(port=port, baudrate=baudrate, timeout=timeout)  
        data = ser.readline(datasize)
        #print("Serial Data:", data)
        if data:
            # print(data)
            return data
        else:
            return None
    except Exception as error:
        # print(error)
        return error
    finally:
        ser.close()