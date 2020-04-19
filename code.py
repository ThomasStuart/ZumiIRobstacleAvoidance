from zumi.zumi import Zumi

zumi = Zumi() 
#zumi.reset_gyro()
#zumi.mpu.calibrate_MPU()
POWER = 40 
TIME  = 1 

def main():
    print("Program Started")
    
    ir_readings = zumi.get_all_IR_data()
    bottom_right_ir = ir_readings[1] 
    bottom_left_ir  = ir_readings[3]
    front_right_ir  = ir_readings[0]
    front_left_ir   = ir_readings[5]
    back_right_ir   = ir_readings[2] 
    back_left_ir    = ir_readings[4]
  
  
    threshold_IR_FL  = 150
    threshold_IR_FR  = 150
  
  
    ir_readings = zumi.get_all_IR_data()
    
    while( True ): 
        
        ir_reading = zumi.get_all_IR_data()
        front_right_ir = ir_reading[0]
        front_left_ir  = ir_reading[5]
        
        if front_left_ir < threshold_IR_FL and front_right_ir < threshold_IR_FR:
            zumi.reverse(POWER, TIME )
   
    zumi.stop()
    print("Program Ended")
try:
    main()

finally:
    zumi.stop()
