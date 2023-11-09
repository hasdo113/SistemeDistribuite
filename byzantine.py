import random

import time

def receive_message():
    # simulam primirea unui mesaj
    time.sleep(0.5)
    msg = {
        "type": random.choice(["initial", "echo", "ready"]),
        "from": random.randint(0, n-1)
    }
    return msg


n = 10 # numarul total de noduri
k = 2 # numarul de noduri stricate

# initializam dictionarul pentru numaratori
msg_count = {
    "initial": [0] * n,
    "echo": [0] * n,
    "ready": [0] * n
}

# selectam k noduri la intamplare pentru a trimite mesajele initiale
initial_nodes = random.sample(range(n), k)

# trimitem mesajele initiale catre nodurile selectate
for node in initial_nodes:
    msg_count["initial"][node] += 1

print("Sending initial messages to nodes: ", initial_nodes)

# asteptam mesaje de echo de la k + 1 noduri
while True:
    msg = receive_message()
    if msg["type"] == "echo" and msg_count["echo"][msg["from"]] == 0:
        msg_count["echo"][msg["from"]] += 1
        if sum(msg_count["echo"]) > (n + k) / 2:
            break

print("Received echo messages from nodes: ", [i for i in range(n) if msg_count["echo"][i]>0])

# selectam k noduri diferite la intamplare pentru a trimite mesaje de echo
echo_nodes = random.sample(set(range(n)) - set(initial_nodes), k)

# trimitem mesajele de echo catre nodurile selectate
for node in echo_nodes:
    msg_count["echo"][node] += 1

print("Sending echo messages to nodes: ", echo_nodes)

# asteptam sa primim mesaje de ready de la k + 1 noduri
while True:
    msg = receive_message()
    if msg["type"] == "ready" and msg_count["ready"][msg["from"]] == 0:
        msg_count["ready"][msg["from"]] += 1
        if sum(msg_count["ready"]) > k + 1:
            break

print("Received ready messages from nodes: ", [i for i in range(n) if msg_count["ready"][i]>0])

# decidem valoarea lui i bazat pe numarul majoritar de mesaje
i = max(range(n), key=lambda x: msg_count["initial"][x] + msg_count["echo"][x] + msg_count["ready"][x])
print("Decision: ", i)
