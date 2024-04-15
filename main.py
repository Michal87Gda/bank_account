from client import Client, ClientWithMinimum

Horge = ClientWithMinimum("A_man", 1400, 1000)
jorge = Client("B_man")

# Horge.deposit(145)
# Horge.try_withdraw(200)

result = Horge.try_withdraw(400)

if result.is_ok():
    print(result.message)
else:
    print(result.message)