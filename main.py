import Functions

team1, team2 = Functions.get_teams_name()

# 1.  Pass Arrows
#Functions.pass_arrows(team1)
# Functions.pass_arrows(team2)

# Pass Flow
Functions.pass_flow(team1)
Functions.pass_flow(team2)

# 2. Pass Network
#Functions.pass_network(team1)
#Functions.pass_network(team2)

# 3. Pressure Map
Functions.pressure_map(team1)
# Functions.pressure_map(team2)

# 4.  Shots Expected Goals
Functions.shots_expected_goals(team1, team2)

# 5.  Player Convex Hull
Functions.player_convex_hull('Fábio Henrique Tavares')
#Functions.player_convex_hull('Harry Winks')