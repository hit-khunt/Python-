from random import randint

class train:
    def __init__(self, trainNo):
        self.trainNo = trainNo

    def bookTicket(self, fro, to):
        print(f"The train is booked in train no: {self.trainNo} from {fro} to {to}. ")

    def getStatus(self):
        print(f"Train no: {self.trainNo} is running on time")

    def getFare(self, fro, to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(222, 5555)}")

t = train(12399)
t.bookTicket("Surat", "Rajkot")
t.getStatus()
t.getFare("Surat", "Rajkot")
