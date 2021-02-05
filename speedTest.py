import speedtest
st = speedtest.Speedtest()

def mb(speed):
    speed = speed/1000000
    return speed

def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier

d_speed = truncate(mb(st.download()), 2)
u_speed = truncate(mb(st.upload()), 2)

server = []
st.get_servers(server)
ping = mb(st.results.ping)

print(f"download speed: {d_speed}Mbps\nupload speed: {u_speed}Mbps\nping: {ping}ms")
