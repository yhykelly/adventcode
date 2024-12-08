def load_file(filepath):
    with open(filepath) as reader:
        l = [l.strip() for l in reader.readlines()]
    equations = [] # store goal and candidates
    for line in l:
        eq = line.split(":")
        sum = eq[0] # the intended sum / product
        elements = eq[1].strip().split(" ") # the element candidates
        elements.append(sum)
        equations.append(elements)
    return equations

def _permutation_repeat(combos, text, prefix, n, k):
    if k == 0: # base, len(prefix) == len(text)
        combos.append(prefix)
        return
    for i in range(n):
        new_prefix = prefix + text[i] 
        _permutation_repeat(combos, text, new_prefix, n, k-1)
    return combos

def permutation_repeat(text, k):
    combos = []
    combo = _permutation_repeat(combos, text, "", len(text), k)
    return combo

def main():
    good_sum = 0
    equations = load_file('input-dec7-sample.txt')
    for equation in equations:
        candidates = [int(element) for element in equation[:-1]]
        ans = int(equation[-1])
        num_slots = len(candidates) -1
        operators_combos = permutation_repeat("+|*", num_slots)
        for combonation in operators_combos:
            combonation = list(combonation)
            current_pos = 0
            result = candidates[current_pos]
            while (len(combonation) > 0):
                following = candidates[current_pos+1]
                operator = combonation.pop()
                # # part2
                # if operator == "|":
                #     result = int(str(result)+str(following))
                # # update to elif for part 2
                if operator == "+": 
                    result += following
                elif operator == "*":
                    result *= following
                current_pos += 1
            if result == ans:
                good_sum += ans
                print(equation)
                print(result)
                print("ans:", ans)
                print("-----")
                break
    print("final:", good_sum)


if __name__ == "__main__":
    main()