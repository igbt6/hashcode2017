# {
#     'V': V,
#     'E': E,
#     'R': R,
#     'C': C,
#     'X': X,
#     'videos': videos,
#     'endpoints': endpoints,
#     'requests': requests
# }

def run_that_beast(problem):
    requests = problem['requests']
    endpoints = problem['endpoints']
    videos = problem['videos']
    caches = problem['caches']

    while requests:
        print 'Nice infinite loop'
        sorted_requests = sort_requests(requests, endpoints, caches, videos)
        current_request = sorted_requests.pop(0)

        handle_request()

        if are_all_caches_full(caches):
            break

    return caches


def are_all_caches_full(caches):
    empty_caches = {
        cache_id: cache for cache_id, cache in caches.items()
        if cache.get('current_capacity') <= 0
    }

    return len(empty_caches) == len(caches)


def handle_request(request, endpoints, caches, videos):
    video = videos[request['video_id']]
    endpoint = videos[request['endpoint_id']]

    found_closest_cache = get_closest_cache(endpoint, video, caches)

    if not found_closest_cache:
        return None

    closest_cache = caches[found_closest_cache['cache_id']]
    if video['video_id'] not in closest_cache['video_ids']:
        closest_cache['video_ids'].append(video['video_id'])
        closest_cache['current_capacity'] -= video['size']


def sort_requests(requests, endpoints, caches, videos):
    requests_with_weights = [
            (get_weight_for_request(request, endpoints, caches, videos), request) for request in requests]

    sorted_requests = sorted(requests_with_weights, reverse=True)

    return [request for weight, request in sorted_requests]


def get_closest_cache(endpoint, video, caches):
    endpoints_caches = endpoint['caches']
    nice_caches = []

    for cache_id, latency in endpoints_caches.items():
        cache = caches[cache_id]
        if cache['current_capacity'] > video['size']:
            nice_caches.append((latency, cache_id))

            # TODO: check if video is already in this cache


    if not nice_caches:
        return None

    sorted_nice_caches = sorted(nice_caches)

    return {
        'cache_id': sorted_nice_caches[0][1],
        'latency': sorted_nice_caches[0][0]
    }


def get_closest_cache_with_video(endpoint, video, caches):
    endpoints_caches = endpoint['caches']
    nice_caches = []

    for cache_id, latency in endpoints_caches.items():
        cache = caches[cache_id]
        if video['video_id'] in cache['video_ids']:
            nice_caches.append((latency, cache_id))

    if not nice_caches:
        return None

    sorted_nice_caches = sorted(nice_caches)

    return {
        'cache_id': sorted_nice_caches[0][1],
        'latency': sorted_nice_caches[0][0]
    }



def get_weight_for_request(request, endpoints, caches, videos):
    endpoint = endpoints[request['endpoint_id']]

    latency_to_dc = endpoint['latency_to_dc']
    how_many_times = request['how_many_times']
    video = videos[request['video_id']]

    latency_to_closest_cache = getattr(get_closest_cache(endpoint, video, caches), 'latency', latency_to_dc)
    latency_to_cache_with_video = getattr(get_closest_cache_with_video(endpoint, video, caches), 'latency', 0)

    weight = how_many_times * (latency_to_dc - latency_to_closest_cache + latency_to_cache_with_video)

    return weight
