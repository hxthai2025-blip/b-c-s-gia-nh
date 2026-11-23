#!/usr/bin/env python3
"""Tạo toàn bộ site tĩnh:
  • chuyên đề GERD (6 bài, từ file Word) và chuyên đề bệnh trĩ (7 bài, từ tri_content.py)
  • trang tổng quan /kien-thuc-tieu-hoa/
  • các vùng sinh tự động trong index.html (đầu trang, chân trang, thẻ chuyên đề, bài nổi bật, số bài)
  • sitemap.xml

Chạy từ thư mục gốc của repo:  python3 _tools/build_all.py
Cần pandoc (đọc file Word GERD) và BeautifulSoup (bs4).
"""
import html
import re

import build_gerd as g
import build_tri as t
import layout as L
import tri_content as tc

E = html.escape

READ_GERD = {1: "6–8 phút", 2: "6–8 phút", 3: "7–9 phút", 4: "7–9 phút", 5: "7–9 phút", 6: "8–10 phút"}


def read_time(ser, art):
    if ser["key"] == "gerd":
        return READ_GERD[art["n"]]
    m = re.search(r"Thời gian đọc:\s*([^·]+)", art["meta"])
    return m.group(1).strip() if m else ""


SERIES = [
    dict(key="gerd", name="Trào ngược dạ dày – thực quản (GERD)", tag="GERD", icon="stomach",
         cover="linear-gradient(135deg,#0b6e78 0%,#1b76b8 100%)", c="#0b7a75",
         desc="Sáu bài từ nhận biết bệnh, chế độ ăn, dùng thuốc đúng cách đến GERD kháng trị, Barrett thực quản và phẫu thuật.",
         arts=g.ARTICLES, icons={1: "stomach", 2: "apple", 3: "pill", 4: "refresh", 5: "search", 6: "cross"}),
    dict(key="tri", name="Bệnh trĩ", tag="Bệnh trĩ", icon="droplet",
         cover="linear-gradient(135deg,#b4324a 0%,#e0802f 100%)", c="#be185d",
         desc="Bảy bài về dấu hiệu, phân loại, phân độ Goligher, chăm sóc tại nhà, các phương pháp điều trị, trĩ khi mang thai và trĩ ngoại tắc mạch.",
         arts=tc.ARTICLES, icons={1: "droplet", 2: "alert-triangle", 3: "book-open", 4: "gauge", 5: "leaf", 6: "cross", 7: "baby"}),
]
BY_KEY = {s["key"]: s for s in SERIES}
FEATURED = [("gerd", 1), ("tri", 1), ("tri", 2), ("gerd", 2), ("tri", 5), ("gerd", 3)]


def art_card(ser, art, base, ip):
    """base: tiền tố đường dẫn tới thư mục bài (hub: "", trang chủ: "kien-thuc-tieu-hoa/"); ip: tiền tố tới thư mục gốc để lấy biểu tượng."""
    return (f'<a class="art-card" href="{base}{art["slug"]}/" style="--cover:{ser["cover"]}">'
            f'<div class="thumb"><em>{E(ser["tag"])} · Bài {art["n"]}</em>{L.ic(ip, ser["icons"][art["n"]])}</div>'
            f'<div class="txt"><h3>{E(art["h1"])}</h3><p>{E(art["desc"])}</p>'
            f'<span class="rt">{L.ic(ip, "clock")} {E(read_time(ser, art))}</span></div></a>')


def series_card(ser):
    items = "".join(f'<li>{L.ic("", "check-circle")}<span>{E(x["short"])}</span></li>' for x in ser["arts"][:4])
    more = len(ser["arts"]) - 4
    if more > 0:
        items += f'<li>{L.ic("", "arrow-right")}<span>và {more} bài khác</span></li>'
    return (f'<a class="series-card" href="kien-thuc-tieu-hoa/#{ser["key"]}" style="--cover:{ser["cover"]};--c:{ser["c"]}">'
            f'<div class="cover"><span class="badge">{len(ser["arts"])} bài</span>{L.ic("", ser["icon"])}</div>'
            f'<div class="body"><h3>{E(ser["name"])}</h3><p>{E(ser["desc"])}</p><ul>{items}</ul>'
            f'<span class="go">Đọc chuyên đề {L.ic("", "arrow-right")}</span></div></a>')


def fill(src, name, content):
    pat = re.compile(rf"(<!--{name}:START-->).*?(<!--{name}:END-->)", re.S)
    assert pat.search(src), f"thiếu vùng {name}"
    return pat.sub(lambda m: m.group(1) + "\n" + content + "\n" + m.group(2), src)


def build_index():
    p = g.ROOT / "index.html"
    s = p.read_text(encoding="utf-8")
    s = fill(s, "FONTS", L.FONT_LINK)
    s = fill(s, "HEADER", L.header(""))
    s = fill(s, "FOOTER", L.footer(""))
    s = fill(s, "SERIES", "\n".join(series_card(x) for x in SERIES))
    s = fill(s, "ARTICLES", "\n".join(
        art_card(BY_KEY[k], next(a for a in BY_KEY[k]["arts"] if a["n"] == n), "kien-thuc-tieu-hoa/", "") for k, n in FEATURED))
    s = re.sub(r"(<!--N:START-->).*?(<!--N:END-->)", lambda m: f"{m.group(1)}{sum(len(x['arts']) for x in SERIES)}{m.group(2)}", s, flags=re.S)
    p.write_text(s, encoding="utf-8")


def build_hub():
    url = g.SITE + "/kien-thuc-tieu-hoa/"
    desc = "Kiến thức tiêu hóa dễ hiểu: chuyên đề trào ngược dạ dày – thực quản (GERD) và chuyên đề bệnh trĩ, mỗi chuyên đề gồm nhiều bài từ cơ bản đến chuyên sâu."
    sections = ""
    for ser in SERIES:
        cards = "".join(art_card(ser, a, "", "../") for a in ser["arts"])
        sections += (f'<section class="sec tight" id="{ser["key"]}" style="scroll-margin-top:90px">'
                     f'<div class="section-head"><div><span class="kicker">Chuyên đề · {len(ser["arts"])} bài</span>'
                     f'<h2>{E(ser["name"])}</h2><p>{E(ser["desc"])}</p></div></div>'
                     f'<div class="art-grid">{cards}</div></section>')
    page = g.head("../", url, "Kiến thức tiêu hóa: trào ngược dạ dày (GERD) và bệnh trĩ | Family Doctor", desc)
    page += f'''
<main>
<div class="wrap">
  <div class="page-head">
    <div class="crumb"><a href="../#trang-chu">Trang chủ</a> / Kiến thức tiêu hóa</div>
    <span class="eyebrow">{L.ic("../", "stomach")} Tiêu hóa · Chuyên đề</span>
    <h1>Kiến thức tiêu hóa</h1>
    <p>Hai chuyên đề giúp bạn hiểu đúng bệnh, chăm sóc đúng cách và biết khi nào cần đi khám. Mỗi chuyên đề nên đọc theo thứ tự, bắt đầu từ Bài 1.</p>
  </div>
  {sections}
  <div style="height:48px"></div>
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
    build_index()
    build_sitemap()
    print("Đã tạo", len(g.ARTICLES), "bài GERD,", len(tc.ARTICLES), "bài trĩ, trang tổng quan, index.html và sitemap")
