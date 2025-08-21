from pathlib import Path
import json
import random
import string

class Bank:
    __database = "data.json"
    data = []

    # Load existing data from JSON file
    try:
        if Path(__database).exists():
            with open(__database) as fs:
                data = json.loads(fs.read())
    except Exception as err:
        print(f"Error loading database: {err}")

    @classmethod
    def Update_data(cls):
        with open(cls.__database, "w") as fs:
            fs.write(json.dumps(cls.data, indent=4))

    @classmethod
    def Generate_Account(cls):
        alpha = random.choices(string.ascii_letters, k=4)
        numbers = random.choices(string.digits, k=8)
        id = alpha + numbers
        random.shuffle(id)
        return "".join(id)

    # ✅ GUI: Create account
    def create_user_gui(self, name, email, age, phone, pin):
        info = {
            "name": name,
            "email": email,
            "age": age,
            "phonenumber": phone,
            "pin": pin,
            "AccountNo.": self.Generate_Account(),
            "balance": 0
        }
        self.data.append(info)
        self.Update_data()
        return f"✅ Account created! Your Account Number is: {info['AccountNo.']}"

    # ✅ GUI: Deposit money
    def deposit_gui(self, ac, pin, amount):
        user = [i for i in self.data if i["AccountNo."] == ac and i["pin"] == pin]
        if not user:
            return "❌ Invalid account or PIN"
        if amount > 10000:
            return "⚠️ Cannot deposit more than ₹10,000 at once"
        user[0]["balance"] += amount
        self.Update_data()
        return f"💰 Deposited ₹{amount} successfully"

    # ✅ GUI: Withdraw money
    def withdraw_gui(self, ac, pin, amount):
        user = [i for i in self.data if i["AccountNo."] == ac and i["pin"] == pin]
        if not user:
            return "❌ Invalid account or PIN"
        if user[0]["balance"] < amount:
            return "⚠️ Insufficient balance"
        user[0]["balance"] -= amount
        self.Update_data()
        return f"💸 Withdrawn ₹{amount} successfully"

    # ✅ GUI: Get account details
    def get_user_gui(self, ac, pin):
        user = [i for i in self.data if i["AccountNo."] == ac and i["pin"] == pin]
        return user[0] if user else None

    # ✅ GUI: Update details
    def update_user_gui(self, ac, pin, name, age, email, phone, new_pin):
        user = [i for i in self.data if i["AccountNo."] == ac and i["pin"] == pin]
        if not user:
            return "❌ Account not found"
        
        user[0].update({
            "name": name,
            "age": age,
            "email": email,
            "phonenumber": phone,
            "pin": new_pin
        })
        self.Update_data()
        return "✅ Details updated successfully"

    # ✅ GUI: Delete account
    def delete_user_gui(self, ac, pin):
        index = next((i for i, u in enumerate(self.data) if u["AccountNo."] == ac and u["pin"] == pin), None)
        if index is not None:
            self.data.pop(index)
            self.Update_data()
            return "🗑️ Account deleted successfully"
        return "❌ Invalid credentials"