# nyitott-zárt elv OCP

from abc import ABC, abstractmethod


class Discount(ABC):
    @abstractmethod
    def calculate(self, price):
        pass

    def info(self):
        print("info-teg")


class ClubCardDiscount(Discount):
    def calculate(self, price):
        return price / 2


class NoDiscount(Discount):
    def calculate(self, price):
        return price


class PercentageDiscount(Discount):
    def __init__(self, percent):
        self.percent = percent

    def calculate(self, price):
        return price * (1 - self.percent / 100)


def apply_discount(discount: Discount, price: float):
    return discount.calculate(price)


no_discount = NoDiscount()
percent_discount = PercentageDiscount(10)

print(apply_discount(no_discount, 100))
print(apply_discount(percent_discount, 100))


# LSP - liskov helyettesítés

# rossz version
class Bird:
    def fly(self):
        return "repül"


class Pingvin(Bird):
    def fly(self):
        raise NotImplementedError("nem tud repülni")
# end r-v


class Bird:
    def move(self):
        return "sétál"


class FlyingBird(Bird):
    def fly(self):
        return "repül"


class NonFlyingBird(Bird):
    def walk(self):
        return "totyog"



pingvin = NonFlyingBird()
sparrow = FlyingBird()

print(sparrow.fly())
print(pingvin.move())



# interfész ISP

from abc import ABC, abstractmethod


class Printer(ABC):
    @abstractmethod
    def print(self, content):
        pass


class Scanner(ABC):
    @abstractmethod
    def scan(self):
        pass


class MultiFunctionDevice(Printer, Scanner):
    def print(self, content):
        print(f"nyomtat: {content}")

    def scan(self):
        return "Scanning in progress 1%"


class SimplePrinter(Printer):
    def print(self, content):
        print("nyomtat")


printer = SimplePrinter()
printer.print("hello")

mdf = MultiFunctionDevice()
print(mdf.scan())


# DIP

from abc import ABC, abstractmethod


class NotificationSender(ABC):
    @abstractmethod
    def send(self, msg):
        pass


class EmailSender(NotificationSender):
    def send(self, msg):
        print(f"sending mail: {msg}")


class SmsSender(NotificationSender):
    def send(self, msg):
        print(f'sending sms {msg}')


class NotificationService:
    def __init__(self, sender: NotificationSender):
        self.sender = sender

    def notify(self, msg):
        self.sender.send(msg)


email_service = NotificationService(EmailSender())
sms_service = NotificationService(SmsSender())

email_service.notify("úton van")
sms_service.notify("10p és ott")