"""
A few friends and I are playing a game at 6pm. I know they often arrive late, and I
really don't want to be late.

I actually looked at historical data, and found out my friends arrival time can be
described as random variable that follows a normal distribution of parameter
mean= 'appointment time' amd std_dev = 10 min.

I need to set the appointment so that Im at least 99% confident all my friends will
be there by 6pm. Can you figure out the latest appointment time that would check
that criteria? Thanks!!
"""

# This problem can be solved by finding when the latest friend arrives, then
# doing an MC on that. This tells you how late the latest friend is. To be 99%
# sure that they arrive on time, you pick the 99th percentile of lateness and
# subtract that from the appointment time.

import numpy as np

def simulate_one_meeting(n_friends, std_dev):
    'Gets the maximum lateness for one meeting.'
    return np.max([np.random.normal(0, std_dev, n_friends)])

def simulate_meeting(N_samples, n_friends, std_dev):
    samples = np.array([simulate_one_meeting(n_friends, std_dev) for _ in range(N_samples)])
    return samples

game_time = 18 * 60 # 6pm in number of minutes from midnight
n_friends = 4
std_dev_arrival_time_min = 10

N_samples = 10000
lateness_samples = simulate_meeting(N_samples, n_friends, std_dev_arrival_time_min)
cutoff = np.round(np.percentile(lateness_samples, 99))
appointment_time = game_time - cutoff
print(f"Latest friend is only {cutoff} minutes late 1% of the time")
print(f"Therefore the appointment time should be = {game_time} - {cutoff} = {appointment_time}.")
hr, mi = divmod(appointment_time, 60)
print(f"In hours, that's {int(hr)}:{int(mi)}pm.")