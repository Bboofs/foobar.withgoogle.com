def solution(xs):
    # Your code here
    from numpy import prod
    
    # Scenario 1: the list has only one item
    if (len(xs) == 1):
        return str(xs[0])
    
    # Create a list of -ve powers
    neg_xs = [x for x in xs if x < 0]
    
    # Create a list of +ve powers
    pos_xs = [x for x in xs if x > 0]
    
    # Scenario 2: the list is all +ve, remove one of the lowest values
    # and return the product of the remaining
    if pos_xs == xs:
        pos_xs.pop(pos_xs.index(min(pos_xs)))
        return str(int(prod(pos_xs)))
        
    # Scenario 3: All the numbers are 0
    if pos_xs == neg_xs:
        return '0'
    
    # Scenario 4: there is one -ve number and all other elements are 0
    if (len(neg_xs) == 1 and (not pos_xs)):
        return '0'
    
    # Scenario 5:
    # Product of odd -ves will always result in a -ve,
    # so remove the largest -ve number
    if(len(neg_xs) % 2 > 0):
        neg_xs.pop(neg_xs.index(max(neg_xs)))
        
    # Note: The product of an empty array will be neutral element 1
    
    # product of the -ve energy
    neg_power = int(prod(neg_xs))
    pos_power = int(prod(pos_xs))
    
    # Scenario 6: Empty list - does not apply since
    # Each array of solar panels contains at least 1 and no more than 50 panels
    
    return str(pos_power * neg_power)
    
print(solution([-2, -3, 4, -5]))
print(solution([2, 0, 2, 2, 0]))
print(solution([2, 2, 2, 2, 2]))
print(solution([0, 0, 0, 0, 0]))
print(solution([0, 0, 0, 0, -3]))
