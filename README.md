# Zhou Yi Divination
# This is a simple caculator for Zhou Yi divination.
# Suppose there are some initial number of sticks, separate them into two heaps, each heap at least has 5 sticks.
# Take away one stick from right heap, then divide them by 4 to get res_left and res_right. If the res_X number is 0 then treat it as 4.
# Take away res_left and res_right from two heaps. Merge the two heaps together.
# Re-do above operations, for totally 3 times. At last we get N sticks left. The divination result number is N/4.
# This program is to get the divination number for 6 times and print the result in sequence.
