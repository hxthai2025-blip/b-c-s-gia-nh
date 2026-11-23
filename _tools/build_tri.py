#!/usr/bin/env python3
"""Tạo 7 trang chuyên đề BỆNH TRĨ từ _tools/tri_content.py bằng ArticleLayout dùng chung (layout.article_page).

Chạy:  python3 _tools/build_all.py   (tạo toàn site)
"""
import html
import re

import build_gerd as g
import layout as L
import tri_content as c

E = html.escape
ROOT = g.ROOT
OUT = g.OUT
SITE = g.SITE
IMG_DIR = ROOT / "assets" / "img" / "tri"
BY_N = {a["n"]: a for a in c.ARTICLES}
SERIES_NAME = "Bệnh trĩ"


def _size(f):
    m = re.search(r'viewBox="0 0 (\d+) (\d+)"', (IMG_DIR / f).read_text(encoding="utf-8"))
    return (int(m.group(1)), int(m.group(2))) if m else (640, 400)


def links(body):
    return re.sub(r'href="@(\d)"', lambda m: f'href="../{BY_N[int(m.group(1))]["slug"]}/"', body)


def featured_of(a):
    """Ảnh đại diện = hình minh họa của mục xuất hiện đầu tiên trong bài."""
    for title, *_ in a["sections"]:
        if title in a["figs"]:
            f, alt, cap = a["figs"][title]
            w, h = _size(f)
            return dict(src=f"assets/img/tri/{f}", alt=alt, w=w, h=h, webp=None, caption=E(cap), credit="Hình vẽ: Family Doctor"), title
    return None, None


def read_time(a):
    m = re.search(r"Thời gian đọc:\s*([^·]+)", a["meta"])
    return (m.group(1).strip() + " đọc") if m else ""


def build_article(a):
    url = f"{SITE}/kien-thuc-tieu-hoa/{a['slug']}/"
    featured, feat_title = featured_of(a)
    toc, body = [], [f'<section>{links(a["intro"])}</section>']
    for title, text, *_ in a["sections"]:
        sid = g.slugify(title)
        toc.append((sid, title))
        sec = links(text)
        spec = a["figs"].get(title)
        if spec and title != feat_title:
            f, alt, cap = spec
            w, h = _size(f)
            fig = g.inline_fig("../../", f"assets/img/tri/{f}", alt, cap, "", w, h)
            i = sec.find("</p>")
            sec = sec[:i + 4] + fig + sec[i + 4:] if i >= 0 else fig + sec
        body.append(f'<section><h2 id="{sid}">{E(title)}</h2>{sec}</section>')
    body.append(f'<div class="alert warn"><div><b>Thông điệp an toàn</b>{E(c.SAFETY)}</div></div>')
    toc += [("hoi-dap", "Câu hỏi thường gặp"), ("tai-lieu-tham-khao", "Tài liệu tham khảo")]
    crumbs = [("Trang chủ", "../../"), ("Kiến thức tiêu hóa", "../"), ("Bệnh trĩ", "../#tri"), (a["short"], None)]
    crumbs_abs = [("Trang chủ", SITE + "/"), ("Kiến thức tiêu hóa", SITE + "/kien-thuc-tieu-hoa/"), (a["h1"], url)]
    ld, og = g.schema_of(a, url, featured, c.PUBLISHED, c.MODIFIED, "Chuyên đề bệnh trĩ", crumbs_abs, a["faq"])
    ld[0]["about"] = {"@type": "MedicalCondition", "name": "Bệnh trĩ", "alternateName": "Hemorrhoids"}
    page = L.article_page("../../", url=url, seo_title=a["seo"] + " | Family Doctor", desc=a["desc"], crumbs=crumbs,
                          category=("Tiêu hóa · Bệnh trĩ", "../#tri"), h1=a["h1"], sapo=a["subtitle"],
                          published=c.PUBLISHED, modified=c.MODIFIED, read_time=read_time(a),
                          featured=featured, summary=[E(x) for x in a["summary"]], toc=toc, sections_html="".join(body),
                          faq=a["faq"], refs=[E(r) for r in c.REFS], related=g.related_of(a, c.ARTICLES, "Bệnh trĩ"),
                          series_title="Chuyên đề bệnh trĩ", series_items=g.series_items(a, c.ARTICLES),
                          pager=g.pager_of(a, BY_N), ld=ld, og_image=og)
    d = OUT / a["slug"]
    d.mkdir(parents=True, exist_ok=True)
    (d / "index.html").write_text(page, encoding="utf-8")


def build_all_articles():
    for a in c.ARTICLES:
        build_article(a)


if __name__ == "__main__":
    build_all_articles()
    print("Đã tạo", len(c.ARTICLES), "bài về bệnh trĩ")
