x = client.submit(inc, 1)
y = client.submit(dec, 2)
total = client.submit(add, x, y)

print(total)           # This is still a future
client.gather(total)   # This blocks until the computation has finished
