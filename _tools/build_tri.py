#!/usr/bin/env python3
"""Tạo 7 trang chuyên đề BỆNH TRĨ từ _tools/tri_content.py.

Chạy:  python3 _tools/build_all.py   (tạo cả GERD, trĩ, trang tổng quan và sitemap)
"""
import html, json, re
from pathlib import Path

import build_gerd as g
import tri_content as c

E = html.escape
ROOT = g.ROOT
OUT = g.OUT
SITE = g.SITE
AUTHOR = g.AUTHOR
IMG_DIR = ROOT / "assets" / "img" / "tri"
BY_N = {a["n"]: a for a in c.ARTICLES}
HUB_URL = SITE + "/kien-thuc-tieu-hoa/"


def fmt_date(d):
    y, m, dd = d.split("-")
    return f"{dd}/{m}/{y}"


def _size(f):
    m = re.search(r'viewBox="0 0 (\d+) (\d+)"', (IMG_DIR / f).read_text(encoding="utf-8"))
    return (int(m.group(1)), int(m.group(2))) if m else (640, 400)


def figure(a, title):
    spec = a["figs"].get(title)
    if not spec:
        return ""
    f, alt, cap = spec
    w, h = _size(f)
    return (f'<figure class="fig"><a href="../../assets/img/tri/{f}" target="_blank" rel="noopener" title="Bấm để xem hình lớn">'
            f'<img src="../../assets/img/tri/{f}" alt="{E(alt)}" loading="lazy" width="{w}" height="{h}"></a>'
            f'<figcaption>{E(cap)} <span class="zoom">Bấm vào hình để xem lớn hơn.</span></figcaption></figure>')


def links(body):
    return re.sub(r'href="@(\d)"', lambda m: f'href="../{BY_N[int(m.group(1))]["slug"]}/"', body)


def build_article(a):
    url = f"{SITE}/kien-thuc-tieu-hoa/{a['slug']}/"
    toc, body = [], []
    body.append(f'<section>{links(a["intro"])}</section>')
    for title, text, *_ in a["sections"]:
        sid = g.slugify(title)
        toc.append(f'<li><a href="#{sid}">{E(title)}</a></li>')
        sec = links(text)
        fig = figure(a, title)
        if fig:
            i = sec.find("</p>")
            sec = sec[:i + 4] + fig + sec[i + 4:] if i >= 0 else fig + sec
        body.append(f'<section><h2 id="{sid}">{E(title)}</h2>{sec}</section>')
    toc.append('<li><a href="#hoi-dap">Câu hỏi thường gặp</a></li>')
    toc.append('<li><a href="#tai-lieu-tham-khao">Tài liệu tham khảo</a></li>')
    faq = "".join(f"<details><summary>{E(q)}</summary><p>{E(ans)}</p></details>" for q, ans in a["faq"])
    body.append(f'<section class="faq"><h2 id="hoi-dap">Câu hỏi thường gặp</h2>{faq}</section>')
    body.append(f'<section><div class="alert info"><div><b>Thông điệp an toàn</b>{E(c.SAFETY)}</div></div></section>')
    refs = "".join(f"<li>{E(r)}</li>" for r in c.REFS)
    body.append(f'<section class="refs-block"><h2 id="tai-lieu-tham-khao">Tài liệu tham khảo</h2><ol class="list refs">{refs}</ol>'
                '<p class="refs"><b>Lưu ý y khoa:</b> Bài viết cung cấp thông tin giáo dục sức khỏe, không thay thế khám bệnh, chẩn đoán hoặc chỉ định điều trị cá thể. Chảy máu hậu môn không mặc nhiên là bệnh trĩ.</p></section>')

    prv, nxt = BY_N.get(a["n"] - 1), BY_N.get(a["n"] + 1)
    pager = '<nav class="pager" aria-label="Bài trong chuyên đề">'
    pager += (f'<a href="../{prv["slug"]}/"><small>← Bài {prv["n"]}</small>{E(prv["short"])}</a>' if prv else "<span></span>")
    pager += (f'<a class="next" href="../{nxt["slug"]}/"><small>Bài {nxt["n"]} →</small>{E(nxt["short"])}</a>' if nxt else "<span></span>")
    pager += "</nav>"
    series = "".join(
        (f'<li aria-current="page"><b>{x["n"]}. {E(x["short"])}</b><span class="soon">Bạn đang đọc</span></li>' if x is a
         else f'<li><a href="../{x["slug"]}/">{x["n"]}. {E(x["short"])}</a></li>') for x in c.ARTICLES)

    schema = {"@context": "https://schema.org", "@type": "MedicalWebPage", "headline": a["h1"], "description": a["desc"],
              "url": url, "inLanguage": "vi", "datePublished": c.PUBLISHED, "dateModified": c.MODIFIED,
              "author": {"@type": "Person", "name": AUTHOR},
              "publisher": {"@type": "Organization", "name": "Family Doctor", "url": SITE + "/"},
              "about": {"@type": "MedicalCondition", "name": "Bệnh trĩ", "alternateName": "Hemorrhoids"},
              "isPartOf": {"@type": "CollectionPage", "name": "Kiến thức tiêu hóa", "url": HUB_URL}}
    faq_schema = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": ans}} for q, ans in a["faq"]]}
    ld = ('<script type="application/ld+json">\n' + json.dumps(schema, ensure_ascii=False, indent=1) + "\n</script>\n"
          '<script type="application/ld+json">\n' + json.dumps(faq_schema, ensure_ascii=False, indent=1) + "\n</script>\n")

    meta_line = f"Tác giả: {AUTHOR} · Đăng ngày: {fmt_date(c.PUBLISHED)} · Cập nhật: {fmt_date(c.MODIFIED)}"
    page = g.head("../../", url, a["seo"] + " | Family Doctor", a["desc"], ld)
    page += f'''
<main>
<div class="wrap">
  <div class="page-head">
    <div class="crumb"><a href="../../#trang-chu">Trang chủ</a> / <a href="../">Kiến thức tiêu hóa</a> / Bệnh trĩ · Bài {a["n"]}</div>
    <span class="eyebrow">Tiêu hóa · Chuyên đề bệnh trĩ · Bài {a["n"]}</span>
    <h1>{E(a["h1"])}</h1>
    <p>{E(a["subtitle"])}</p>
    {g.meta_row("../../", a["meta"].split(" · ")[0], AUTHOR, c.PUBLISHED, c.MODIFIED)}
  </div>

  <div class="article-grid">
    <article class="article stack">
      <nav class="toc" aria-label="Mục lục"><h2>Nội dung bài viết</h2><ol>{"".join(toc)}</ol></nav>
      {"".join(body)}
      {pager}
    </article>

    <aside class="stack">
      <div class="panel stack">
        <h3>Chuyên đề bệnh trĩ</h3>
        <ol class="series">{series}</ol>
        <a href="../">Xem tất cả chuyên đề tiêu hóa →</a>
      </div>
      <div class="panel stack"><h3>Đi ngoài ra máu?</h3><p class="muted">Đừng tự kết luận là trĩ. Hãy xem dấu hiệu cần đi khám sớm.</p><a class="btn" href="../{BY_N[2]["slug"]}/">Dấu hiệu cần khám</a></div>
      <div class="panel stack"><h3>Còn thắc mắc?</h3><p class="muted">Nhắn BS. Thái Hoàng qua Zalo: <b>0935 498 866</b>.</p><a class="btn ghost" href="https://zalo.me/0935498866" target="_blank" rel="noopener">Nhắn Zalo</a></div>
    </aside>
  </div>
</div>
</main>
'''
    page += g.foot("../../")
    d = OUT / a["slug"]
    d.mkdir(parents=True, exist_ok=True)
    (d / "index.html").write_text(page, encoding="utf-8")


def build_all_articles():
    for a in c.ARTICLES:
        build_article(a)


if __name__ == "__main__":
    build_all_articles()
    print("Đã tạo", len(c.ARTICLES), "bài về bệnh trĩ")
