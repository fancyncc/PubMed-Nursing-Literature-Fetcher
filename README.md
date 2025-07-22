# PubMed Nursing Literature Fetcher

本代码使用 **NCBI E-utilities API** 从 PubMed 数据库中检索指定关键词、期刊、时间范围内的护理相关文献，并提取文章标题与摘要。

------

## 一、功能介绍

- 用户输入检索关键词（如“depression”或“patient safety”）
- 限定在以下护理类期刊中检索（可更改）：
  - *Journal of Clinical Nursing (J Clin Nurs)*
  - Nursing Outlook (Nurs Outlook)
  - *International Journal of Nursing Studies (Int J Nurs Stud)*
- 限定发表时间为 **2020 至 2025 年**
- 自动输出前 5 篇文献的标题与摘要

------

#### 示例运行效果

```
输入自然语言搜索描述：虚拟现实与远程护理服务的融合
耗时:60.15s    GPT output: "Virtual Reality" AND "Telehealth" AND integration； "Virtual Reality" AND "Telehealth" AND ("systematic review" OR "meta-analysis")
"Virtual Reality" AND "Telehealth" AND integration

📄 标题：A tailored de-implementation strategy to reduce low-value home-based nursing care: A multiple interrupted time series study.
📄 摘要：To evaluate the effects of a multifaceted de-implementation strategy (RENEW) on the volume (time in minutes) of care spent by home-based nursing care teams on three widely used low-value nursing practices: (1) 'washing the client with water and soap by default' & 'washing the client from head to toe daily', (2) 'application of zinc cream, powders or pastes when treating intertrigo' and (3) 'assisting with putting on/taking off compression stockings while the client can do this him/herself (possibly with an aid)'.
--------------------------------------------------
📄 标题：The association between self-reported substance use and work schedule characteristics among nurses: A cross-sectional study.
📄 摘要：Job stress due to adverse work schedules has been associated with negative effects on nurses, including substance use. Nurses' potentially harmful substance use related to adverse schedules amid the COVID-19 pandemic may be of critical concern for nurse wellness and patient safety.
--------------------------------------------------
📄 标题：Practice-based models for nurse scientists: A scoping review of core components, development, evaluations, and key success factors.
📄 摘要：The need for improved organizational support for practice-based nurse scientists has been stressed. To provide a synopsis of the field, we mapped the existing literature.
--------------------------------------------------
📄 标题：Advancing human rights, health equity, and equitable health policy with LGBTQ+ people: An American Academy of Nursing consensus paper.
📄 摘要：Health disparities among LGBTQ+ people arise from sociocultural contexts of gender oppression. Complex historical, legal, and policy landscapes perpetuate inequities through discriminatory legislation and policies. Intersections of ideology, theology, and politics converge to shape anti-LGBTQ+ initiatives that have detrimental impacts on human rights and health outcomes. This consensus statement recommends promoting inclusive laws and policies, expanding antidiscrimination protections, and amplifying awareness within nursing and other healthcare practitioner communities, particularly in the United States. By advocating for a human rights-based approach and leveraging international frameworks, such as the International Bill of Human Rights and Yogyakarta Principles, we seek to empower nurses and policy stakeholders to address systemic barriers and advance health equity, equitable health policy, and human rights with LGBTQ+ people globally. These recommendations affirm the Academy's position, align seamlessly with its stance against oppressive laws and policies, and reinforce its mission to influence policy for improved health and equity.
--------------------------------------------------
📄 标题：Shaping the nursing workforce through virtual reality: Pitfalls and possibilities of implementation in a nursing curriculum.
📄 摘要：Nursing workforce concerns are shaping how colleges and schools of nursing effectively implement teaching strategies like simulation. With the growning nursing shortage, more chronic and complex conditions, and situations for patients arising, the education of student nurses must adapt to help this growning concern. Virtual reality simulation (VR-Sim) is a modality considered for nursing education, and it shows benefits in the literature. However, little is known about the implementation process within a nursing program.
--------------------------------------------------
"Virtual Reality" AND "Telehealth" AND ("systematic review" OR "meta-analysis")

📄 标题：A tailored de-implementation strategy to reduce low-value home-based nursing care: A multiple interrupted time series study.
📄 摘要：To evaluate the effects of a multifaceted de-implementation strategy (RENEW) on the volume (time in minutes) of care spent by home-based nursing care teams on three widely used low-value nursing practices: (1) 'washing the client with water and soap by default' & 'washing the client from head to toe daily', (2) 'application of zinc cream, powders or pastes when treating intertrigo' and (3) 'assisting with putting on/taking off compression stockings while the client can do this him/herself (possibly with an aid)'.
--------------------------------------------------
📄 标题：The association between self-reported substance use and work schedule characteristics among nurses: A cross-sectional study.
📄 摘要：Job stress due to adverse work schedules has been associated with negative effects on nurses, including substance use. Nurses' potentially harmful substance use related to adverse schedules amid the COVID-19 pandemic may be of critical concern for nurse wellness and patient safety.
--------------------------------------------------
📄 标题：Practice-based models for nurse scientists: A scoping review of core components, development, evaluations, and key success factors.
📄 摘要：The need for improved organizational support for practice-based nurse scientists has been stressed. To provide a synopsis of the field, we mapped the existing literature.
--------------------------------------------------
📄 标题：Advancing human rights, health equity, and equitable health policy with LGBTQ+ people: An American Academy of Nursing consensus paper.
📄 摘要：Health disparities among LGBTQ+ people arise from sociocultural contexts of gender oppression. Complex historical, legal, and policy landscapes perpetuate inequities through discriminatory legislation and policies. Intersections of ideology, theology, and politics converge to shape anti-LGBTQ+ initiatives that have detrimental impacts on human rights and health outcomes. This consensus statement recommends promoting inclusive laws and policies, expanding antidiscrimination protections, and amplifying awareness within nursing and other healthcare practitioner communities, particularly in the United States. By advocating for a human rights-based approach and leveraging international frameworks, such as the International Bill of Human Rights and Yogyakarta Principles, we seek to empower nurses and policy stakeholders to address systemic barriers and advance health equity, equitable health policy, and human rights with LGBTQ+ people globally. These recommendations affirm the Academy's position, align seamlessly with its stance against oppressive laws and policies, and reinforce its mission to influence policy for improved health and equity.
--------------------------------------------------
📄 标题：Shaping the nursing workforce through virtual reality: Pitfalls and possibilities of implementation in a nursing curriculum.
📄 摘要：Nursing workforce concerns are shaping how colleges and schools of nursing effectively implement teaching strategies like simulation. With the growning nursing shortage, more chronic and complex conditions, and situations for patients arising, the education of student nurses must adapt to help this growning concern. Virtual reality simulation (VR-Sim) is a modality considered for nursing education, and it shows benefits in the literature. However, little is known about the implementation process within a nursing program.
--------------------------------------------------
```

------

## 二、使用方法

1. 环境要求

   - Python 3.7+
   - `request`包
   - `openai`包

2. 安装依赖

   ```python
   pip install requests
   pip install openai==0.28
   ```

3. 设置API KEY

   ```python
   # 设置api_key
   api_key = "your-api-key"  # pubmedTest.py
   openai.api_key = "your-api-key"  # test_convert_google_query.py
   ```

4. 运行

   ```
   python PubMed_Fetcher.py
   ```

------

## 三、技术说明

该代码使用 NCBI 提供的 [E-utilities API](https://www.ncbi.nlm.nih.gov/books/NBK25499/)：

- 使用 `esearch.fcgi` 获取 PubMed ID（PMID）
- 使用 `efetch.fcgi` 获取对应文献的 XML 格式内容（标题、摘要等）

查询中使用的参数包括：

- `"retmax": 5`：限制最多返回 5 条文献
- `"ta"`：限制在特定期刊（Title Abbreviation）
- `"dp"`：发表时间（Date of Publication）

------

## 四、其他

此代码可拓展为以下功能：

- 保存结果为 CSV 或 JSON
- 增加筛选文献类型（如只显示 review）
