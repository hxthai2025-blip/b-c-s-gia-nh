#!/usr/bin/env python3
"""Tạo toàn bộ mục Kiến thức tiêu hóa: chuyên đề GERD (6 bài), chuyên đề bệnh trĩ (7 bài),
trang tổng quan /kien-thuc-tieu-hoa/ và sitemap.xml.

Chạy từ thư mục gốc của repo:  python3 _tools/build_all.py
Cần pandoc (đọc file Word GERD) và BeautifulSoup (bs4).
"""
import html

import build_gerd as g
import build_tri as t
import tri_content as tc

E = html.escape


def card(slug, tag, title, desc):
    return (f'<a class="card" href="{slug}/"><span class="tag">{E(tag)}</span><h3>{E(title)}</h3>'
            f'<p>{E(desc)}</p><span class="more">Đọc bài →</span></a>')


def build_hub():
    url = g.SITE + "/kien-thuc-tieu-hoa/"
    desc = "Kiến thức tiêu hóa dễ hiểu: chuyên đề trào ngược dạ dày – thực quản (GERD) và chuyên đề bệnh trĩ, mỗi chuyên đề gồm nhiều bài từ cơ bản đến chuyên sâu."
    gerd = "".join(card(x["slug"], f'Bài {x["n"]}', x["h1"], x["desc"]) for x in g.ARTICLES)
    tri = "".join(card(x["slug"], f'Bài {x["n"]}', x["h1"], x["desc"]) for x in tc.ARTICLES)
    page = g.head("../", url, "Kiến thức tiêu hóa: trào ngược dạ dày (GERD) và bệnh trĩ | Family Doctor", desc)
    page += f'''
<main>
<div class="wrap">
  <div class="page-head">
    <div class="crumb"><a href="../#trang-chu">Trang chủ</a> / <a href="../#benh-thuong-gap">Bệnh thường gặp</a> / Kiến thức tiêu hóa</div>
    <span class="eyebrow">Tiêu hóa · Chuyên đề</span>
    <h1>Kiến thức tiêu hóa</h1>
    <p>Hai chuyên đề giúp bạn hiểu đúng bệnh, chăm sóc đúng cách và biết khi nào cần đi khám. Mỗi chuyên đề nên đọc theo thứ tự, bắt đầu từ Bài 1.</p>
  </div>
  <section class="block" style="margin-top:0">
    <div class="section-head"><h2 id="gerd">Trào ngược dạ dày – thực quản (GERD)</h2></div>
    <p class="muted" style="margin-bottom:16px;max-width:62ch">Sáu bài từ nhận biết bệnh, chế độ ăn, dùng thuốc đúng cách đến GERD kháng trị, Barrett thực quản và phẫu thuật.</p>
    <div class="grid">{gerd}</div>
  </section>
  <section class="block">
    <div class="section-head"><h2 id="tri">Bệnh trĩ</h2></div>
    <p class="muted" style="margin-bottom:16px;max-width:62ch">Bảy bài về dấu hiệu, phân loại, phân độ, chăm sóc tại nhà, các phương pháp điều trị, trĩ khi mang thai và trĩ ngoại tắc mạch.</p>
    <div class="grid">{tri}</div>
  </section>
</div>
</main>
'''
    page += g.foot("../")
    (g.OUT / "index.html").write_text(page, encoding="utf-8")


def build_sitemap():
    urls = ["", "kien-thuc-tieu-hoa/"]
    urls += [f"kien-thuc-tieu-hoa/{x['slug']}/" for x in g.ARTICLES]
    urls += [f"kien-thuc-tieu-hoa/{x['slug']}/" for x in tc.ARTICLES]
    body = "".join(f"  <url><loc>{g.SITE}/{u}</loc><lastmod>{tc.MODIFIED}</lastmod></url>\n" for u in urls)
    (g.ROOT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + body + "</urlset>\n",
        encoding="utf-8")


if __name__ == "__main__":
    for a in g.ARTICLES:
        g.build_article(a)
    t.build_all_articles()
    build_hub()
    build_sitemap()
    print("Đã tạo", len(g.ARTICLES), "bài GERD,", len(tc.ARTICLES), "bài trĩ, trang tổng quan và sitemap")
