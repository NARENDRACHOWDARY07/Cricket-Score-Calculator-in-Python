print("CRICKET SCORE CALCULATOR")

team = input("Enter team name: ")
overs = int(input("Enter number of overs: "))

runs = 0
wickets = 0
balls = 0

while balls < overs * 6 and wickets < 10:

    print("Ball", balls + 1)
    result = input("Enter runs or W for wicket: ")

    if result == "W" or result == "w":
        wickets += 1
        balls += 1

    else:
        try:
            value = int(result)

            if value in [0, 1, 2, 3, 4, 6]:
                runs += value
                balls += 1
            else:
                print("Invalid run")
                continue

        except ValueError:
            print("Invalid input")
            continue

    print("Score:", runs, "/", wickets)

completed_overs = balls // 6
remaining_balls = balls % 6

if balls == 0:
    run_rate = 0
else:
    run_rate = runs / (balls / 6)

print("\nFINAL SCORE")
print("Team:", team)
print("Score:", runs, "/", wickets)
print("Overs:", str(completed_overs) + "." + str(remaining_balls))
print("Run Rate:", round(run_rate, 2))

if wickets == 10:
    print("Innings finished - all wickets are out")
else:
    print("Innings finished - overs completed")