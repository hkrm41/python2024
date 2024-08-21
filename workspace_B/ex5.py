import  wikipedia
wiki=wikipedia.page('Artificial intelligence')
text='''Food Apple Fruit Banana Juice Rice Water Butter Bread Beef Chicken Drink Noodles Cream Baguette'''
print(text)

from wordcloud import WordCloud
wd=WordCloud(width =2000, height = 1500).generate(text)

import matplotlib.pyplot as plt
plt.figure(figsize=(10, 8))
plt.axis('off')
plt.imshow(wd)
plt.show()
#이장혁