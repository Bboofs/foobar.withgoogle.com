def solution(pegs):
    # Your code here
    from fractions import Fraction
    peg_count = len(pegs)
    if((not pegs) or peg_count == 1):
        return [-1,-1]
    even = True if (peg_count % 2 == 0) else False
    sum = (pegs[peg_count - 1] - pegs[0]) if even else (- pegs[0] - pegs[peg_count -1])
    print('Sum1:', sum)
    
    if(peg_count > 2):
        for peg in range(1, peg_count-1):
            sum += 2 * (-1) ** (peg+1) * pegs[peg]
    print('Sum2:', sum)
    first_r = Fraction(2 * (float(sum)/3 if even else sum)).limit_denominator()
    
    print('first_r:', first_r)
    # now that we have the radius of the first gear, we should again check the input 
    # array of pegs to verify that the pegs radius' is at least 1.
    # since for valid results, first_r >= 1 and r = 2 * last_r
    # thus for valid results first_r >= 2

    if first_r < 2:
        return [-1,-1]
    
    current_r = first_r
    for peg in range(0, peg_count-2):
        centre_dist = pegs[peg+1] - pegs[peg]
        print(peg, centre_dist)
        next_r = centre_dist - current_r
        if (current_r < 1 or next_r < 1):
            return [-1,-1]
        else:
            current_r = next_r

    return [first_r.numerator, first_r.denominator]
    