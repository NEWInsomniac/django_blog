# 分页函数

    # 需求细分：
    # 1.如果当前页是第一页，则上一页不显示。
    # 2.如果当前页是最后一页，则下一页不显示。
    # 3.永远显示10页的页数。
    # 4.当前页小于等于5的时候，当前页显示在1-5之间。
    # 5.当前页大于5的时候，小于总数减5的时候，那么当前页显示在中间。
    # 6.当前页大约总数减5的时候，显示在最尾巴。

#
# 当前页：current_page
# 显示的最大页数： max_page
# 开始页:start
# 结束页：end
# 中位数： middle = max_page / 2
# 最大页数：num_pages
import math
def custompaginater(num_pages, current_page, max_page):
    middle = math.ceil(max_page / 2)
    # 当最大页数小于  显示的最大页数
    if num_pages < max_page:
        start = 1
        end = num_pages
    else:
        # 当前页小于等于middle 时。
        if current_page <=  middle:
            start = 1
            end = max_page
        else: # 中间情况
            start = current_page - middle
            end = current_page + middle - 1
            # 当前页在尾部的情况
            if current_page + middle > num_pages:
                start = num_pages - max_page + 1
                end = num_pages
    return start,end


