from parking_lot import ParkingLotSystem

p = ParkingLotSystem()


def write_output(line):
    file1 = open("output.txt", "a")
    file1.write(line + "\n")
    file1.close()


def erase_output_file_content():
    open('output.txt', 'w').close()


erase_output_file_content()
with open("input.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        line_data = line.split(' ')
        command = line_data[0]
        if command == 'Create_parking_lot':
            slots = int(line_data[1])
            output = p.create_parking_lot(slots)
            write_output(output)
        elif command == 'Park':
            vehicle_number = line_data[1]
            age = int(line_data[3])
            output = p.park(vehicle_number, age)
            write_output(output)
        elif command == 'Leave':
            slot_number = int(line_data[1])
            output = p.leave(slot_number)
            write_output(output)
        elif command == 'Slot_numbers_for_driver_of_age':
            age = int(line_data[1])
            output = p.slots_for_age(age)
            write_output(output)
        elif command == 'Slot_number_for_car_with_number':
            vehicle_number = line_data[1].split('\n')[0]
            output = p.slot_for_car_number(vehicle_number)
            write_output(output)
        elif command == 'Vehicle_registration_number_for_driver_of_age':
            age = int(line_data[1])
            output = p.vehicle_number_for_age(age)
            write_output(output)
