import stepper

if __name__ == "__main__":

    parser = argparse.ArgumentParser(prog="y-motor", description='Runs y-motor to desired position')

    parser.add_argument('--dir', type=int)
    parser.add_argument('--t', type=int)
    parser.add_argument('--v', type=int)

    args = parser.parse_args()

    dir = args.dir
    duration = args.t
    speed = args.v

    stepper.move_motor(10,15,11,12,speed,duration,dir) # motor_y
