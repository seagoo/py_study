# coding = utf-8

"""在 Python 中有许多有趣的库可供学习， wordcloud 库必须得算一个，我们最后的题目就是，学习 wordcloud 基本用法，然后生成一张词云图。
Wordcloud文档：	
为省去小伙伴找资源的时间，我们在此提供了女神的 png 图片和一些文本词汇
资源地址：https://git.oschina.net/zx576/novel/attach_files
最后的效果图"""

import os.path as path, PIL.Image as image, numpy as np, wordcloud as wdcd
d = path.dirname(__file__)
text = open(path.join(d, 'Jane Eyre(简·爱).txt')).read()
alice_mask = np.array(image.open(path.join(d, "anne.png")))
wc = wdcd.WordCloud(background_color="white", max_words=2000, mask=alice_mask)
wc.generate(text)
wc.to_file(path.join(d, "anne_wc.png"))