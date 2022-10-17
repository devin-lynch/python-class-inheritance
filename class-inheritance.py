# CLASS INHERITANCE 

    # All phones

    # have a phone number

    # can place phone calls

    # can send text messages

class Phone():
    def __init__(self, phone_number):
        self.phone_number = phone_number

    def __str__(self):
        return str(self.phone_number)

    def call(self, other_number):
        print(f'Ring-a-ding-ding, calling {other_number} from {self.phone_number}')

    def text(self, other_number, msg):
        print(f'beep boop sending text from {self.phone_number} to {other_number}')
        print(msg)

gabes_phone = Phone(6666661234)

# print(gabes_phone)

# gabes_phone.call(5105483936)

# gabes_phone.text(123456789, 'u up?')




# to create a subclass, you just need to pass the parent class as a parameter:

class IPhone(Phone): # the Phone parameter says iphone is an extension of Phone, and thus we have access to the functions from Phone
    def __init__(self, phone_number, generation, color):
        super().__init__(phone_number)
        self.generation = generation
        self.color = color

    def __str__(self):
        return f'gen {self.generation} {self.color} Iphone {self.phone_number}'

    def set_fingerprint(self, my_fingerprint):
        self.fingerprint = my_fingerprint

    def unlock(self, fingerprint=None):
        if (not self.fingerprint):
            print('Phone unlocked because fingerprint not set yet')
        elif (fingerprint == self.fingerprint):
            print("Phone unlocked. Fingerprint matches.")
        else:
            print("Phone locked. Fingerprint doesn't match.")



westons_iphone = IPhone(4443332211, 14, 'Rose Gold')

westons_iphone.set_fingerprint('Westons thumb')
# westons_iphone.unlock('Westons thumb')


class Android(Phone):
    def __init__(self, phone_number, keyboard="Default"):
        super().__init__(phone_number)
        self.keyboard = keyboard

    def __str__(self):
        return f'This Android\'s number is {self.phone_number} and uses the {self.keyboard} keyboard'

gabes_android = Android(6666661234, "UK")
devos_android = Android(123456789, "Spanish")
print(gabes_android)
print(devos_android)



# westons_iphone.call(gabes_phone)
# westons_iphone.text(gabes_phone, f'Hey nerd, I have a {westons_iphone.color} iphone hehehe')