# -*- coding: utf-8 -*-

import calendar
import numpy as np

#  Change these values to generate a new course schedule
year = 2025
# Format is [month, day]
start = [1, 8]
end = [4, 18]

# 0-M, 1-T, 2-W, 3-R, 4-F, 5-S, 6-S
Days = [0, 2, 4]

# Format is (month, day): 'Holiday Name'
# Fall Holidays
# Holidays = {
#     (9, 5): "Labor Day",
#     (10, 17): "Fall Break",
#     (10, 18): "Fall Break",
#     (11, 21): "Thanksgiving Break",
#     (11, 22): "Thanksgiving Break",
#     (11, 23): "Thanksgiving Break",
#     (11, 24): "Thanksgiving Break",
#     (11, 25): "Thanksgiving Break",
# }
# Summer Holidays
# Holidays = {(7, 3): '\\nth{4} July',
#             (7, 24): "\\nth{24} July"
#             }
# Spring Holidays
Holidays = {
    (1, 20): "Martin Luther King Day",
    (2, 17): "President's Day",
    (3, 10): "Spring Break",
    (3, 11): "Spring Break",
    (3, 12): "Spring Break",
    (3, 13): "Spring Break",
    (3, 14): "Spring Break",
    (4, 1): "Festival of Excellence",
}

# Format is ['title', 'chapter', length] for topics
# Format is ['Exam #'] for midterm exams

# Atkins 11th Edition
Topics = [
    ["The Origins of Quantum Mechanics", "7A", 1],
    ["Wavefunctions", "7B", 1],
    ["Operators and Observables", "7C", 1],
    ["Special Topic: Experiments and Interpretations in QM", "**", 1],
    ["Translational Motion", "7D", 1],
    ["Vibrational Motion", "7E", 1],
    ["Rotational Motion", "7F", 1],
    # ["Catch-up/Review Day -- Midterm Exam 1 (Ch. 7)"],
    ["Hydrogenic Atoms", "8A", 1],
    ["Many Electron Atoms", "8B", 1],
    ["Atomic Spectra", "8C", 1],
    ["Valence-Bond Theory", "9A", 1],
    ["MO Theory: the Hydrogen Molecule-Ion", "9B", 1],
    ["MO Theory: Homonuclear Diatomic Molecules", "9C", 1],
    ["MO Theory: Heteronuclear Diatomic Molecules", "9D", 1],
    ["MO Theory: Polyatomic Molecules", "9E", 1],
    # ["Catch-up/Review Day -- Midterm Exam 2 (Ch. 8--9)"],
    ["Shape and Symmetry", "10A", 1],
    ["Group Theory", "10B", 1],
    ["Applications of Symmetry", "10C", 1],
    ["General Features of Molecular Spectroscopy", "11A", 1],
    ["Rotational Spectroscopy", "11B", 1],
    ["Vibrational Spectroscopy of Diatomic Molecules", "11C", 1],
    ["Vibrational Spectroscopy of Polyatomic Molecules", "11D", 1],
    ["Symmetry Analysis of Vibrational Spectroscopy", "11E", 1],
    ["Electronic Spectra", "11F", 1],
    ["Decay of Excited States", "11G", 1],
    ["Special Topic: Lasers and Spectroscopy", "**", 1],
    # ["Catch-up/Review Day -- Midterm Exam 3 (Ch. 10--11)"],
    ["General Principles of NMR", "12A", 1],
    ["Features of NMR Spectra", "12B", 1],
    ["Pulse Technique in NMR", "12C", 1],
    ["Electron Paramagnetic Resonance", "12D", 1],
    ["The Boltzmann Distribution", "13A", 1],
    ["Molecular Partition Functions", "13B", 1],
    ["Molecular Energies", "13C", 1],
    ["The Canonical Ensemble", "13D", 1],
    ["Internal Energy and Entropy", "13E", 1],
    ["Derived Functions", "13F", 1],
    ["Electric Properties of Molecules", "14A", 1],
    ["Interactions Between Molecules", "14B", 1],
    ["Liquids", "14C", 1],
    ["Macromolecules and Self-Assembly", "14D-E", 1],
    #  ['Self-Assembly', '14E', 1],
    # ["Catch-up/Review Day -- Midterm Exam 4 (Ch. 12--13)"],
    ["Catch-up/Review Day"],
]

Day_Letters = ["M", "T", "W", "R", "F", "S", "S"]
#%%
Class_Days = []
Total_Days = 0
for month in range(start[0], end[0] + 1):
    cal = calendar.monthcalendar(year, month)
    for week in cal:
        if month is start[0] and max(week) < start[1]:
            pass
        elif month is end[0] and week[0] > end[1]:
            pass
        elif (0 not in week) or (week[-1] == 0):
            Class_Days.append("New Week")
        for day, date in enumerate(week):
            if month is start[0] and date < start[1]:
                pass
            elif month is end[0] and date > end[1]:
                pass
            elif day not in Days:
                pass
            elif date == 0:
                pass
            elif (month, date) not in Holidays:
                today = "{}, {}. {}".format(
                    Day_Letters[day], calendar.month_abbr[month], date
                )
                Class_Days.append(today)
                Total_Days += 1
            else:
                today = "{}, {}. {}".format(
                    Day_Letters[day], calendar.month_abbr[month], date
                )
                Class_Days.append([today, Holidays[(month, date)]])

shortfall = len(Topics) - Total_Days
print("Shortfall is {}".format(shortfall))
#%%
combined_times = np.ones(len(Topics)) * 5
for i in range(len(Topics) - 1):
    try:
        combined_times[i] = Topics[i][2] + Topics[i + 1][2]
    except:
        pass
#%%
combined_indexes = []
i = 0
j = 0
while i < len(combined_times) and j < shortfall:
    if combined_times[i] < 1.75:
        answer = raw_input("Combine {} with {}?".format(Topics[i][0], Topics[i + 1][0]))
        if answer == "y":
            combined_indexes.append(i)
            i += 2
            j += 1
        else:
            i += 1
    else:
        i += 1
print("Made up {} of the shortfall of {}.".format(j, shortfall))
#%%
schedule = "\\begin{tabular}{rcccc}\n\
& Date && Topic & Chapter\\\\\n"
topic_num = 0
week_num = 1
day_num = 0
while day_num < len(Class_Days):
    if Class_Days[day_num] == "New Week":
        schedule = schedule + "\\midrule\nWeek {} ".format(week_num)
        week_num += 1
        day_num += 1
    if len(Class_Days[day_num]) == 2:  # Holidys
        schedule = schedule + "& {}".format(Class_Days[day_num][0])
        schedule = (
            schedule
            + "& \\multicolumn{{3}}{{l}}{{\\textbf{{{} -- No Class!}}}}\\\\\n".format(
                Class_Days[day_num][1]
            )
        )
    elif topic_num in combined_indexes:  # Combined topics
        schedule = schedule + "& \\multirow{{2}}{{*}}{{{}}}".format(Class_Days[day_num])
        schedule = schedule + "& & {} & {}\\\\\n".format(
            Topics[topic_num][0], Topics[topic_num][1]
        )
        topic_num += 1
        schedule = schedule + "& & & {} & {}\\\\\n".format(
            Topics[topic_num][0], Topics[topic_num][1]
        )
        topic_num += 1
    elif len(Topics[topic_num]) > 1:  # Regular Topics
        schedule = schedule + "& {}".format(Class_Days[day_num])
        schedule = schedule + "&& {} & {}\\\\\n".format(
            Topics[topic_num][0], Topics[topic_num][1]
        )
        topic_num += 1
    else:  # Exams
        schedule = schedule + "& {}".format(Class_Days[day_num])
        schedule = (
            schedule
            + "& \\multicolumn{{3}}{{l}}{{\\textbf{{{}}}}}\\\\\n".format(
                Topics[topic_num][0]
            )
        )
        topic_num += 1
    day_num += 1
schedule = schedule + "\\midrule\n"
schedule = (
    schedule
    + "Finals Week& W, May 2& \\multicolumn{3}{l}{\\textbf{Final Exam --- 1:00 pm -- 2:50 pm Bring a pencil and scantron}}\\\\\n"
)
schedule = schedule + "\\end{tabular}"
print("Here is your schedule")
print("---------------------")
print(schedule)
with open("schedule_3620.tex", "w") as f:
    f.write(schedule)

# Other classes' Topics
Topics = [
    ["Intro", "1", 0.75],
    ["Blackbody Radiation", "1", 0.25],
    ["Photoelectric Effect", "1", 0.5],
    ["Rydberg Formula", "1", 0.5],
    ["The Bohr Model", "1", 1],
    ["Classical Waves", "2", 0.5],
    ["QM Waves", "2", 0.75],
    ['The Schr\\"odinger Equation', "2", 1],
    ["Operators", "2", 1],
    ["Eigenvalues", "2", 1],
    ["Midterm Exam 1 (Ch. 1-2)"],
    ["Postulates of QM", "3", 0.75],
    ["Free Particle", "4", 0.5],
    ["Particle in a Box", "4", 0.8],
    ["PIB and the Real World", "5", 0.5],
    ["Tunneling", "5", 0.75],
    ["Conjugated Molecules", "5", 0.5],
    ["Quantum Dots", "5", 0.5],
    ["Midterm Exam 2 (Ch. 3-5)"],
    ["Commutators", "6", 0.75],
    ["The Uncertainty Principle", "6", 0.75],
    ["Harmonic Oscillator", "7", 1],
    ["Rigid Rotor Model", "7", 1],
    ["Spherical Harmonics", "7", 0.75],
    ["Intro to Spectroscopy", "8", 0.5],
    ["Vibrational Spectra", "8", 1],
    ["Rotational Spectra", "8", 0.9],
    ["Selection Rules", "8", 0.5],
    ["The Hydrogen Atom", "9", 1],
    ["Midterm Exam 3 (Ch. 6-8)"],
    ["Atomic Orbitals", "9", 1],
    ["Radial Probability Function", "9", 0.5],
    ["Shell Model", "9", 0.5],
    ["The Helium Atom", "10", 1],
    ["Electron Spin", "10", 0.8],
    ["Variational Method", "10", 1],
    ["Hartree-Fock Equations", "10", 1],
    ["Atomic Spectroscopy", "11", 1],
    ["Midterm Exam 4 (Ch. 9-11)"],
    ["Chemical Bonds", "12", 0.75],
    ["Generating MOs", "12", 0.75],
    ["Homonuclear Diatomics", "12", 0.75],
    ["Heteronuclear Diatomis", "12", 0.75],
    ["Bond Order and Length", "12", 0.75],
    ["Lewis Structures", "13", 1],
    ["VSEPR Model", "13", 0.5],
    ["Hybridization", "13", 0.5],
    ['H\\"uckle Theory', "13", 0.75],
    ["Solids", "13", 1],
    ["Midterm Exam 5 (Ch. 12-13)"],
    ["Electronic Transitions", "14", 1],
    ["Molecular Term Symbols", "14", 1],
    ["Electronic Spectroscopy", "14", 0.85],
    ["Symmetry Elements", "16", 0.75],
    ["Point Groups", "16", 0.5],
    ["Irreducible Representations", "16", 1],
    ["MOs of \\ch{H2O}", "16", 0.75],
    ["Normal Vibrational Modes", "16", 1],
    ["Selection Rules", "16", 0.6],
    ["Projection Operators", "16", 0.75],
    ["Midterm Exam 6 (Ch. 14, 16)"],
]


# 10th edition:
Topics = [
    ["The Origins of Quantum Mechanics", "7A", 1],
    ["Dynamics of Microscopic Systems", "7B", 1],
    ["The Principles of Quantum Theory", "7C", 1],
    ["Experiments and Interpretations in QM", "**", 1],
    ["Translation", "8A", 1],
    ["Vibrational Motion", "8B", 1],
    ["Rotational Motion", "8C", 1],
    ["Catch-up/Review Day -- Midterm Exam 1 (Ch. 7--8)"],
    ["Hydrogenic Atoms", "9A", 1],
    ["Many Electron Atoms", "9B", 1],
    ["Atomic Spectra", "9C", 1],
    ["Valence-Bond Theory", "10A", 1],
    ["Principles of Molecular Orbital Theory", "10B", 1],
    ["Homonuclear Diatomic Molecules", "10C", 1],
    ["Heteronuclear Diatomic Molecules", "10D", 1],
    ["Polyatomic Molecules", "10E", 1],
    ["Catch-up/Review Day -- Midterm Exam 2 (Ch. 9--10)"],
    ["Symmetry Elements", "11A", 1],
    ["Group Theory", "11B", 1],
    ["Applications of Symmetry", "11C", 1],
    ["General Features of Molecular Spectroscopy", "12A", 1],
    ["Molecular Rotation", "12B", 1],
    ["Rotational Spectroscopy", "12C", 1],
    ["Vibrational Spectroscopy of Diatomic Molecules", "12D", 1],
    ["Vibrational Spectroscopy of Polyatomic Molecules", "12E", 1],
    ["Spectroscopy Special Topics", "**", 1],
    ["Electronic Spectra", "13A", 1],
    ["Decay of Excited States", "13B", 1],
    ["Lasers", "13C", 1],
    ["Catch-up/Review Day -- Midterm Exam 3 (Ch. 11--13)"],
    ["General Principles of NMR", "14A", 1],
    ["Features of NMR Spectra", "14B", 1],
    ["The Boltzmann Distribution", "15A", 1],
    ["Molecular Partition Functions", "15B", 1],
    ["Molecular Energies", "15C", 1],
    ["The Canonical Ensemble", "15D", 1],
    ["Internal Energy and Entropy", "15E", 1],
    ["Derived Functions", "15F", 1],
    ["Electric Properties of Molecules", "16A", 1],
    ["Interactions Between Molecules", "16B", 1],
    ["Liquids", "16C", 1],
    ["Catch-up/Review Day -- Midterm Exam 4 (Ch. 14--16)"],
]
