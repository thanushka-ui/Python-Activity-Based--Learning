def calculate_library_fine(days_delayed, fine_per_day=5):
    """
    Calculates the total fine for an overdue library book.
    """
    if days_delayed <= 0:
        return 0  # No fine if returned on time or early!
    
    total_fine = days_delayed * fine_per_day
    return total_fine

