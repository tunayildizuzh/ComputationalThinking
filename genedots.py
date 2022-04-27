from matplotlib import pyplot as plt

dot1 = 'My care is loss of care, by old care done'
dot2 = 'Your care is gain of care, by new care won'


def dots(str1, str2, window):
    results = []
    x_vals = []
    y_vals = []
    for i,x in enumerate(str1):
        for j,y in enumerate(str2):
            string1 = list(str1[i:i+window])
            string2 = list(str2[j:j+window])
            if len(string1) < window:
                continue
            if len(string2) < window:
                continue

            if string1 == string2:
                results.append(string1)
                x_vals.append(i)
                y_vals.append(j)

    return results , x_vals, y_vals


print(dots(dot1,dot2, 5)[1])
print(dots(dot1,dot2, 5)[2])

# Plotting settings.

# plt.scatter(dots(dot1,dot2, 5)[1], dots(dot1,dot2, 5)[2])
# plt.title('Window size = 5')
# plt.xlabel('My care is loss of care, by old care done')
# plt.ylabel('Your care is gain of care, by new care won')
# plt.show()