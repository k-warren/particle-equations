particles = [
    ["particle", "charge", "baryon number", "lepton electron number", "lepton muon number", "strangeness"],
    ["proton", 1, 1, 0, 0, 0],
    ["neutron", 0, 1, 0, 0, 0],
    ["pion", 1, 0, 0, 0, 0],
    ["kaon", 1, 0, 0, 0, 0],
    ["electron", -1, 0, 1, 0, 0],
    ["muon", -1, 0, 0, 1, 0],
    ["neutrino", 0, 0, 1, 0, 0],
]
while True:
    equation = input("Please enter the equation using words:")
    equation = equation.split(" ")
    print(f"Equation: {equation}")
    lhs = []
    rhs = []
    side = lhs

    particle_names = [particle[0] for particle in particles]

    for token in equation:
        if token == "=":
            side = rhs
        elif token != "+":
            if token not in particle_names:
                print(f"Error: {token} is not a valid particle.")
                exit(1)
            side.append(token)

    print(f"LHS: {lhs}")
    print(f"RHS: {rhs}")

    lhs_charge = sum([particles[particle_names.index(particle)][1] for particle in lhs])
    rhs_charge = sum([particles[particle_names.index(particle)][1] for particle in rhs])
    lhs_baryon_number = sum([particles[particle_names.index(particle)][2] for particle in lhs])
    rhs_baryon_number = sum([particles[particle_names.index(particle)][2] for particle in rhs])
    lhs_lepton_electron_number = sum([particles[particle_names.index(particle)][3] for particle in lhs])
    rhs_lepton_electron_number = sum([particles[particle_names.index(particle)][3] for particle in rhs])
    lhs_lepton_muon_number = sum([particles[particle_names.index(particle)][4] for particle in lhs])
    rhs_lepton_muon_number = sum([particles[particle_names.index(particle)][4] for particle in rhs])
    lhs_strangeness = sum([particles[particle_names.index(particle)][5] for particle in lhs])
    rhs_strangeness = sum([particles[particle_names.index(particle)][5] for particle in rhs])

    if lhs_charge == rhs_charge and lhs_baryon_number == rhs_baryon_number and lhs_lepton_electron_number == rhs_lepton_electron_number and lhs_lepton_muon_number == rhs_lepton_muon_number and lhs_strangeness == rhs_strangeness:
        print("The equation is balanced.")
        pass
    else:
        print("The equation is not balanced.")
        pass
