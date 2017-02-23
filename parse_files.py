from model import (make_cache, make_video, make_request, make_endpoint)

def parse(filename):
    caches = {}
    videos = {}
    requests = []
    endpoints = {}

    with open(filename, mode="r") as f:
        lines = f.readlines()
        lines = [x.strip('\n') for x in lines]

        V, E, R, C, X = map(int, lines[0].split())
        sizes= [int(size) for size in lines[1].split()]

        for i in range(V):
            videos[i] = make_video(i, sizes[i])

        lc = 0
        for i in range(E):
            Ld, K = map(int, lines[i+2+lc].split())
            cache_latencies = []
            for k in range(K):
                cache_latencies.append(tuple(map(int, lines[i+2+lc].split())))
                lc+=1
            cachess = {cache_id: latency_to_endpoint for cache_id, latency_to_endpoint in cache_latencies}

            endpoints[i] = make_endpoint(i, Ld, cachess)

        for i in range(R):
            v, e, n = map(int, lines[i+E+lc+2].split())
            requests.append(make_request(n, v, e))

        caches = {id : make_cache(id, X) for  id in range(0, X)}

    return {
        'V': V,
        'E': E,
        'R': R,
        'C': C,
        'X': X,
        'videos': videos,
        'endpoints': endpoints,
        'requests': requests,
        'caches': caches
    }
