from zumi.zumi import Zumi

zumi = Zumi() zumi.reset_gyro()
zumi.mpu.calibrate_MPU()



def main():
    ir_readings = zumi.get_all_IR_data()
    bottom_right_ir = ir_readings[1] 
    bottom_left_ir = ir_readings[3]
    front_right_ir = ir_readings[0]
    front_left_ir = ir_readings[5]
    back_right_ir = ir_readings[2] 
    back_left_ir = ir_readings[4]
  
  
    min_ir_threshold_IR_front_left = 100
    min_ir_threshold_IR_front_right = 100
  
  
    ir_readings = zumi.get_all_IR_data()
 
    while( front_left_ir < 162 and front_right_ir < 190 ): 
        ir_reading = zumi.get_all_IR_data()
        front_right_ir = ir_readings[0]
        front_left_ir = ir_readings[5]
        # zumi.reverse(40, 1)
    zumi.stop()

try:
    main()

finally:
    zumi.stop()
