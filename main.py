import os
import sys

class Request():
    def __init__(self,v,e,n):
        self.video = v         # Video requested
        self.endpoint = e      #endpoint requesting
        self.request_num = n   # requests number

class Video():
    def __init__(self, _id, s):
        self.id = _id
        self.size = s     # Size of the video
        self.servers = [] # List of servers in where video is cached

class EndPoint():
    def __init__(self,t,id_ ,c):
        self.id      = id_
        self.latency = t  # Latency to the data center
        self.servers = c  # cache latenies


def parse(filename):
    with open(filename, mode="r") as f:   
        lines = f.readlines()
        lines = [x.strip('\n') for x in lines] 
        
        V, E, R, C, X = map(int, lines[0].split())
        videos = []
        sizes= [int(size) for size in lines[1].split()]
        for i in range(V):
            videos.append(Video(i, sizes[i]))
        endpoints = []
        lc = 0
        for i in range(E):
            Ld, K = map(int, lines[i+2+lc].split())
            cache_latencies = []
            for k in range(K):
                cache_latencies.append(tuple(map(int, lines[i+2+lc].split())))
                lc+=1
            endpoints.append(EndPoint(i, Ld, cache_latencies))            
        requests = []
        for i in range(R):
            v, e, n = map(int, lines[i+E+lc+2].split())
            requests.append(Request(v, e, n))
    return V, E, R, C, X, videos, endpoints, requests

def output(filename, solution):
    pass

if __name__ == "__main__":
    if len(sys.argv) == 2:
        input_ = ["input/" + sys.argv[1]]
        parse(input_[0])
