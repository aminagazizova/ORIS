import threading
import time
import random

class ATM:
    def __init__(self, initial_balance):
        self.balance = initial_balance
        self.lock = threading.Lock()

    def withdraw(self, amount):
        with self.lock:
            if amount > self.balance:
                print(f"Недостаточно средств для снятия {amount}. Остаток на счете: {self.balance}.")
                return False
            else:
                time.sleep(random.uniform(0.1, 0.5))
                self.balance -= amount
                print(f"Снято {amount}. Остаток на счете: {self.balance}.")
                return True

def client(atm, client_name):
    for _ in range(5):
        amount = random.randint(10, 100)  #случайная сумма для снятия
        print(f"{client_name} пытается снять {amount}.")
        atm.withdraw(amount)
        time.sleep(random.uniform(0.1, 0.5))

if __name__ == "__main__":
    initial_balance = 500  #баланс
    atm = ATM(initial_balance)

    clients = []
    for i in range(5):
        client_name = f"Клиент-{i + 1}"
        t = threading.Thread(target=client, args=(atm, client_name))
        clients.append(t)
        t.start()

    for client_thread in clients:
        client_thread.join()

    print("Все клиенты завершили свои операции.")
