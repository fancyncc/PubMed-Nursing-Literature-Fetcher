import test_convert_google_query as tcg
import pubmedTest as pt

natural_input = input("输入自然语言搜索描述：")
google_query = tcg.get_query(natural_input)

# 用 split() 方法分割成多个查询语句
queries = google_query[0].split('；')

# 使用 for 循环遍历每一个查询语句
for i, q in enumerate(queries, 1):
    print(q.strip())
    pt.get_detail(q.strip())
