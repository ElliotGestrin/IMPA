import sys

file = sys.stdin # open(sys.argv[1])
T = int( file.readline() )
subjects = {}
result = ""

for case in range(1, T+1):
    N = int( file.readline() )

    for i in range(0, N):
        subject, time = file.readline().strip().split(" ")
        subjects[subject] = int(time)

    D = int( file.readline() )
    due = file.readline().strip()
    result += f"Case {case}: "
    try:
        completion_time = subjects[due]
        if( completion_time <= D ): result += "Yesss\n"
        elif ( completion_time <= D + 5 ): result += "Late\n"
        else: result += "Do your own homework!\n"
    except KeyError:
        result += "Do your own homework!\n"

    subjects.clear()

print(result[0:-1])
