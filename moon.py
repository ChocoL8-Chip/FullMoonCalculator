import numpy

LUNAR_PHASE_CYCLE = 29.5
YEAR = 365.25
all_days_have_full_moon = False
index = 29.5
calendar_list = []
calendar_dict = {}
for _ in range(365):
    calendar_list.append(_)
    calendar_dict[_] = False

while not all_days_have_full_moon:
    calendar_dict[0] = True
    index += 29.5
    new_index = index % 365
    calendar_dict[numpy.floor(new_index)] = True
    for day in calendar_list:
        if calendar_dict[day] == False:
            all_days_have_full_moon = False
            break
        else:
            all_days_have_full_moon = True

print(f"Number of years: {index/365}; Number of days: {index}")


