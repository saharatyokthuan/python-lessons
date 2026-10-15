def apply_discount(total):
    if total >= 2000:
        return total * 0.90
    return total

print(apply_discount(2500))
print(apply_discount(500))
