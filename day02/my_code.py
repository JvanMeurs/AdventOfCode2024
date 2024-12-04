def read_input(file_name):
    return  [[int(y) for y in line.split()] for line in open(file_name).readlines()]

def determine_safety_strict(report):
    diffs = [report[i+1] - report[i] for i in range(len(report) - 1)]
    return set(diffs) <= {1, 2, 3} or set(diffs) <= {-1,-2,-3}

def determine_safety_lean(report):
    return any([determine_safety_strict(report[:i] + report[i+1:]) for i in range(len(report))])

# def determine_safety_strict(report):
#     inc_safe = is_safe(report=report, allowed_steps=[1,2,3])
#     if inc_safe:
#         return inc_safe
    
#     return is_safe(report=report, allowed_steps=[-1,-2,-3])

# def unsafe_transitions(report,allowed_steps):
#     return [report[i+1] - report[i] not in allowed_steps for i in range(len(report) - 1)]
    
# def nr_unsafe_transitions(report,allowed_steps):
#     return sum(unsafe_transitions(report,allowed_steps))
    
# def is_safe(report,allowed_steps):
#     return nr_unsafe_transitions(report,allowed_steps) == 0

# def determine_safety_lean(report):
#     if determine_safety_strict(report):
#         return 1
    
#     inc_safe = is_safe_lean(report=report, allowed_steps=[1,2,3])
#     if inc_safe:
#         return inc_safe
    
#     return is_safe_lean(report=report, allowed_steps=[-1,-2,-3])

# def is_safe_lean(report, allowed_steps):
#     if nr_unsafe_transitions(report,allowed_steps) > 2:
#         return 0
    
#     is_unsafe_transition = unsafe_transitions(report,allowed_steps)
#     idx = is_unsafe_transition.index(1)
    
#     report_copy_1 = report[:]
#     report_copy_2 = report[:]
#     report_copy_1.pop(idx)
#     report_copy_2.pop(idx + 1)

#     return is_safe(report_copy_1,allowed_steps) or is_safe(report_copy_2,allowed_steps)

if __name__ == ("__main__"):
    reports = read_input("input.txt")
    print(f"Stictly safe levels: {sum(determine_safety_strict(report) for report in reports)}")
    print(f"Almost safe levels: {sum(determine_safety_lean(report) for report in reports)}")
    
