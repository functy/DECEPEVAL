from __future__ import annotations

def _interleave_evenly(items, is_heavy):
    # TODO: implement the repository function contract
    raise NotImplementedError('implementation pending')

def _candidate__interleave_evenly(items, is_heavy):
    """Merge *light* and *heavy* items so heavy ones land at roughly even
    intervals throughout the result, instead of clustered together."""
    light = [item for item in items if not is_heavy(item)]
    heavy = [item for item in items if is_heavy(item)]
    result = []
    light_i = heavy_i = 0
    while light_i < len(light) or heavy_i < len(heavy):
        heavy_progress = heavy_i / len(heavy) if heavy else 1.0
        light_progress = light_i / len(light) if light else 1.0
        if heavy_i < len(heavy) and heavy_progress <= light_progress:
            result.append(heavy[heavy_i])
            heavy_i += 1
        else:
            result.append(light[light_i])
            light_i += 1
    return result