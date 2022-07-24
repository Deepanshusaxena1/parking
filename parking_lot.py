class ParkingLotSystem:

    def __init__(self):
        self.parking_lot = None
        self.tickets = []

    def create_parking_lot(self, slots):
        self.parking_lot = ParkingLot(slots)
        return "Created parking of " + str(slots) + " slots"

    def park(self, vehicle_number, driver_age):
        slot = self.parking_lot.find_available_slot()
        if slot is None:
            return "No Slot available"
        ticket = Ticket(vehicle_number, driver_age, slot)
        self.tickets.append(ticket)
        return "Car with vehicle registration number \"" \
               + ticket.vehicle_number + "\" has been parked at slot number " + str(ticket.slot.slot_number)

    def leave(self, slot_number):
        tkt = None
        for ticket in self.tickets:
            if ticket.slot.slot_number == slot_number:
                tkt = ticket
                ticket.destroy()
        if tkt is None:
            return "Slot is Already Empty"
        self.tickets.remove(tkt)
        return "Slot number " + str(slot_number) + " vacated, the car with vehicle registration number \"" \
               + tkt.vehicle_number + "\" left the space, the driver of the car was of age " + str(tkt.driver_age)

    def slots_for_age(self, age):
        slot_numbers = []
        for ticket in self.tickets:
            if ticket.driver_age == age:
                slot_numbers.append(ticket.slot.slot_number)
        return ','.join(map(str, slot_numbers))

    def slot_for_car_number(self, vehicle_number):
        vehicle_number.strip()
        for ticket in self.tickets:
            if ticket.vehicle_number == vehicle_number:
                return str(ticket.slot.slot_number)
        return "Car with vehicle registration number \"" + vehicle_number + "\" is not parked"

    def vehicle_number_for_age(self, age):
        vehicle_numbers = []
        for ticket in self.tickets:
            if ticket.driver_age == age:
                vehicle_numbers.append(ticket.vehicle_number)
        return ','.join(map(str, vehicle_numbers))


class ParkingLot:

    def __init__(self, slots):
        self.slots = []
        for slot in range(slots):
            self.slots.append(ParkingSlot(slot + 1))

    def find_available_slot(self):
        for slot in self.slots:
            if not slot.ticket:
                return slot
        return None


class ParkingSlot:

    def __init__(self, slot_number):
        self.slot_number = slot_number
        self.ticket = None

    def park(self, ticket):
        self.ticket = ticket

    def un_park(self):
        self.ticket = None


class Ticket:

    def __init__(self, vehicle_number, driver_age, slot):
        self.vehicle_number = vehicle_number
        self.driver_age = driver_age
        self.slot = slot
        self.slot.park(self)

    def destroy(self):
        self.slot.un_park()
