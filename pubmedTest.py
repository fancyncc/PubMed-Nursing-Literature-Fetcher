import requests
from xml.etree import ElementTree

def get_detail(prompt_term):

    # Step 1: 使用 esearch 获取 PubMed ID
    # 设置api_key
    api_key = "123456"
    # 限定的期刊和时间条件
    journal = '"J Clin Nurs"[ta] OR "Nurs Outlook"[ta] OR "Int J Nurs Stud"[ta]'
    year_range = '2020:2025[dp]'
    # 拼接为完整查询字符串
    search_term = f'{prompt_term} AND {journal} AND {year_range}'

    esearch_url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
            "db": "pubmed",
            "term": search_term,
            "retmax": 5,
            "retmode": "json",
            "api_key": api_key
    }
    resp = requests.get(esearch_url, params=params)
    pmids = resp.json()["esearchresult"]["idlist"]

    # Step 2: 使用 efetch 获取摘要
    efetch_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    params = {
        "db": "pubmed",
        "id": ",".join(pmids),
        "retmode": "xml"
    }
    resp = requests.get(efetch_url, params=params)
    root = ElementTree.fromstring(resp.content)

    # 解析并打印文章标题和摘要
    for article in root.findall(".//PubmedArticle"):
        title = article.findtext(".//ArticleTitle")
        abstract = article.findtext(".//AbstractText")
        print(f"📄 标题：{title}\n📄 摘要：{abstract}\n{'-'*50}")
