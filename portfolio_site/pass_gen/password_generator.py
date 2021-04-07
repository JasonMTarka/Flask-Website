from random import choice, shuffle


class Password:
    def __init__(self, lowercase=True, uppercase=True, nums=True, syms=False,
                 min_nums=2, min_syms=2, pass_len=8, value=""):
        self.nums = nums
        self.syms = syms
        self.lowercase = lowercase
        self.uppercase = uppercase
        self.min_nums = min_nums
        self.min_syms = min_syms
        self.pass_len = pass_len
        self.value = value

    def __repr__(self):
        if self.value:
            return self.value
        else:
            return ""

    def __len__(self):
        return self.pass_len

    def __getitem__(self, position):
        return self.value[position]

    def generate(self):

        def _constructor():
            temp_password = []
            if self.nums:
                for i in range(0, self.min_nums):
                    temp_password.append(choice(NUMS))
            if self.syms:
                for i in range(0, self.min_syms):
                    temp_password.append(choice(SYMBOLS))
            while len(temp_password) > self.pass_len:
                temp_password.pop()
            while len(temp_password) < self.pass_len:
                temp_password.append(choice(source))
            shuffle(temp_password)
            return temp_password

        source = ""
        LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
        UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        NUMS = "0123456789"
        SYMBOLS = "!@#$%^&*"

        if self.lowercase:
            source += LOWERCASE
        if self.uppercase:
            source += UPPERCASE
        if self.nums:
            source += NUMS
        if self.syms:
            source += SYMBOLS

        if source:
            password = _constructor()
            self.value = "".join(password)
