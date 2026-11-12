from .lrs import locate, locate_by_county_milepost

def geocode(route_id, county_code, milepost):
    """LRS v2 lookup; falls back to county + milepost when the route ID is missing."""
    if route_id:
        return locate(route_id, milepost)
    return locate_by_county_milepost(county_code, milepost)
