def validate_ip(ip):
    parts = ip.split(".")
    if len(parts) != 4:
        return False
    return all(0 <= int(p) <= 255 for p in parts)