def make_cache(cache_id, capacity):
    return {
        'cache_id': cache_id,
        'video_ids': list(),
        'current_capacity': capacity
    }

def make_request(how_many_times, video_id, endpoint_id):
    # Read only, bastard!
    return {
        'how_many_times': how_many_times,
        'video_id': video_id,
        'endpoint_id': endpoint_id
    }

def make_endpoint(endpoint_id, latency_to_dc, caches=None):
    # w srodku caches:
    # {1: latency_to_cache}

    return {
        'endpoint_id': endpoint_id,
        'latency_to_dc': latency_to_dc,
        'caches': caches if caches else {}
    }

def make_video(video_id, size):
    return {
        'video_id': video_id,
        'size': size
    }
