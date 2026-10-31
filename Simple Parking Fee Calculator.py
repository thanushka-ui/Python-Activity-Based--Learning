def calculate_parking_fee(hours_parked, base_hours=2, base_rate=10.0, hourly_rate=5.0):
    """
    Calculates total parking fee with a flat base rate for initial hours
    and an incremental rate for extra hours.
    """
    if hours_parked <= 0:
        return 0.0
    
    if hours_parked <= base_hours:
        total_fee = base_rate
    else:
        extra_hours = hours_parked - base_hours
        total_fee = base_rate + (extra_hours * hourly_rate)
        
    return total_fee

