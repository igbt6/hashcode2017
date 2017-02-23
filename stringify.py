""""
test_cache_data = {
    0: {
        'video_ids': [1, 2, 3, 4, 5],
        'current_capacity': 10
    },
    1: {
        'video_ids': [3, 4, 5],
        'current_capacity': 0
    },
    2: {
        'video_ids': [],
        'current_capacity': 10
    },
    3: {
        'video_ids': [1],
        'current_capacity': 10
    },
}
""""

def stringify(caches, file_name):
    caches_with_videos = {
        cache_id: cache for cache_id, cache in caches.items()
        if len(cache.get('video_ids'))
    }
    # Write cache number
    output_string = '%d\n' % len(caches_with_videos)
    for cache_id, cache in caches_with_videos.items():
        video_ids = ' '.join([
            str(video_id) for video_id in cache.get('video_ids', [])
        ])
        cache_line = '%d %s\n' % (
            cache_id, 
            video_ids
        )
        output_string += cache_line
    with open(file_name, 'w+') as file_handler:
        file_handler.write(output_string)

# stringify(test_cache_data, 'test')