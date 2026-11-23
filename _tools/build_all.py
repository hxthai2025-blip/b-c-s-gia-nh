#!/usr/bin/env python3
"""Tạo toàn bộ site tĩnh Bacsi115.com:
  • 13 bài chuyên đề (GERD từ file Word, trĩ từ tri_content.py) bằng ArticleLayout chung
  • trang tổng quan /kien-thuc-tieu-hoa/, các trang chính sách, 404.html
  • các vùng sinh tự động trong index.html: <head>, đầu trang, trang chủ, chân trang
  • sitemap.xml

Chạy từ thư mục gốc:  python3 _tools/build_all.py      (cần pandoc, bs4, Pillow)
"""
import html
import re

import build_gerd as g
import build_tri as t
import layout as L
import tri_content as tc

E = html.escape
SITE = L.SITE
ic = L.ic

SERIES = [
    dict(key="gerd", name="Trào ngược dạ dày – thực quản (GERD)", tag="GERD", arts=g.ARTICLES, updated=g.MODIFIED,
         desc="Sáu bài từ nhận biết bệnh, chế độ ăn, dùng thuốc đúng cách đến GERD kháng trị, Barrett thực quản và phẫu thuật.",
         featured=g.featured_of, read=lambda a: g.READ_TIME[a["n"]]),
    dict(key="tri", name="Bệnh trĩ", tag="Bệnh trĩ", arts=tc.ARTICLES, updated=tc.MODIFIED,
         desc="Bảy bài về dấu hiệu, phân loại, phân độ Goligher, chăm sóc tại nhà, các phương pháp điều trị, trĩ khi mang thai và trĩ ngoại tắc mạch.",
         featured=lambda a: t.featured_of(a)[0], read=lambda a: t.read_time(a).replace(" đọc", "")),
]
BY_KEY = {s["key"]: s for s in SERIES}


def art(key, n):
    s = BY_KEY[key]
    return s, next(a for a in s["arts"] if a["n"] == n)


def thumb(a_prefix, ser, a, ratio, priority=False):
    f = ser["featured"](a)
    if not f:
        return L.media(a_prefix, None, a["h1"], ratio=ratio, icon="file-text")
    # Ảnh bài viết là hình minh họa y khoa có chú thích → hiển thị trọn khung, không cắt
    return L.media(a_prefix, f["src"], f["alt"], f.get("w"), f.get("h"), ratio, priority, cls="contain", webp=f.get("webp"))


def byline_mini(a_prefix, ser):
    return (f'<span class="byline-mini"><span>{ic(a_prefix, "user")} {E(L.AUTHOR["name"])}</span>'
            f'<span>{ic(a_prefix, "refresh")} Cập nhật {L.fmt_date(ser["updated"])}</span></span>')


# ───────── Trang chủ ─────────
SPECIALTIES = [
    ("Tiêu hóa", "stomach", "Trào ngược dạ dày, bệnh trĩ, viêm dạ dày, tiêu chảy cấp.", "kien-thuc-tieu-hoa/", None, "Xem 13 bài chuyên đề"),
    ("Tim mạch", "heart-pulse", "Tăng huyết áp, rối loạn mỡ máu và cách đọc chỉ số huyết áp.", "#benh-man-tinh", None, "Xem bệnh tim mạch"),
    ("Hô hấp", "wind", "Cúm mùa, viêm họng, viêm mũi dị ứng.", "#benh-thuong-gap", "Hô hấp", "Xem bệnh hô hấp"),
    ("Nội tiết", "flask", "Đái tháo đường type 2, gút và các chỉ số cần biết.", "#benh-man-tinh", None, "Xem bệnh nội tiết"),
    ("Ngoại khoa", "scissors", "Phẫu thuật trĩ, phẫu thuật chống trào ngược: khi nào cần.", "kien-thuc-tieu-hoa/phuong-phap-dieu-tri-benh-tri-longo-laser-phau-thuat/", None, "Đọc bài chuyên sâu"),
    ("Cơ xương khớp", "bone", "Đau thắt lưng cấp: chăm sóc tại nhà và dấu hiệu cần khám.", "#benh-thuong-gap", "Cơ xương khớp", "Xem bệnh cơ xương khớp"),
]
SYMPTOMS = [
    ("Đau bụng", "stomach", "dau-bung", False), ("Sốt", "thermometer", "sot", False), ("Đau ngực", "heart-pulse", "dau-nguc", True),
    ("Đau đầu", "brain", "dau-dau", False), ("Khó thở", "wind", "kho-tho", True), ("Tiêu chảy", "droplet", "tieu-chay", False),
]
FEATURE = ("gerd", 1)
FEATURED_LIST = [("tri", 1), ("tri", 2), ("gerd", 3), ("tri", 5)]


def build_home():
    a = ""
    chips = "".join(f'<a class="chip" href="?q={E(q)}" data-q="{E(q)}">{E(q)}</a>' for q in L.POPULAR)
    hero = f'''<section class="hero" aria-labelledby="hero-title"><div class="wrap hero-grid">
  <div>
    <span class="eyebrow">{ic(a, "badge-check")} Kiến thức sức khỏe cho gia đình Việt</span>
    <h1 id="hero-title">Chăm sóc sức khỏe <span>bắt đầu từ gia đình</span></h1>
    <p class="sub">Tra cứu bệnh lý, triệu chứng và cách chăm sóc bằng ngôn ngữ dễ hiểu. Mỗi bài có nguồn tham khảo và nói rõ khi nào cần đi khám.</p>
    <form class="search" id="homeSearch" role="search" action="./" method="get">
      {ic(a, "search")}<label class="sr-only" for="homeQ">Tìm bệnh hoặc triệu chứng</label>
      <input id="homeQ" name="q" type="search" placeholder="Tìm bệnh, ví dụ: trào ngược dạ dày, sốt xuất huyết…" autocomplete="off">
      <button class="btn" type="submit">Tìm kiếm</button>
    </form>
    <div class="quick"><span>Tìm nhiều:</span>{chips}</div>
    <ul class="trust">
      <li>{ic(a, "book-open")} Có nguồn tham khảo rõ ràng</li>
      <li>{ic(a, "stethoscope")} Bác sĩ phụ trách nội dung</li>
      <li>{ic(a, "shield-check")} Không quảng cáo thuốc</li>
    </ul>
  </div>
  <div class="hero-media">
    {L.media(a, None, "Bác sĩ tư vấn cho bệnh nhân và người nhà", ratio="4/3.4", priority=True, icon="stethoscope", ph="Ảnh bác sĩ tư vấn bệnh nhân – đang chờ ảnh thật có bản quyền")}
    <a class="hero-note" href="{L.ZALO}" target="_blank" rel="noopener"><span class="ib solid">{ic(a, "message")}</span><span><b>Hỏi bác sĩ qua Zalo</b><small>{E(L.AUTHOR["name"])} · {E(L.AUTHOR["dept"])}, {E(L.AUTHOR["org"])}</small></span></a>
  </div>
</div></section>'''

    specs = "".join(
        f'<a class="spec-card" href="{href}"{f" data-spec=\"{E(sp)}\"" if sp else ""}>'
        f'{L.media(a, None, "Ảnh minh họa chuyên khoa " + name, ratio="16/10", icon=icon, ph="Ảnh chuyên khoa sẽ được cập nhật")}'
        f'<span class="body"><h3>{E(name)}</h3><p>{E(desc)}</p><span class="count">{E(cta)} →</span></span></a>'
        for name, icon, desc, href, sp, cta in SPECIALTIES)
    spec_sec = f'''<section class="sec" aria-labelledby="ck"><div class="wrap">
  <div class="section-head"><div><span class="kicker">Chuyên khoa</span><h2 id="ck">Tra cứu theo chuyên khoa</h2><p>Chọn lĩnh vực bạn quan tâm để xem các bệnh và bài viết liên quan.</p></div></div>
  <div class="spec-grid">{specs}</div>
</div></section>'''

    syms = "".join(
        f'<a class="sym-card{" red" if red else ""}" href="#trieu-chung" data-pick-sym="{sid}"><span class="ib">{ic(a, icon)}</span><b>{E(name)}</b>'
        f'<small>{"Có thể là dấu hiệu nguy hiểm" if red else "Xem bệnh có thể liên quan"}</small></a>'
        for name, icon, sid, red in SYMPTOMS)
    sym_sec = f'''<section class="sec alt" aria-labelledby="tc"><div class="wrap">
  <div class="section-head"><div><span class="kicker">Triệu chứng</span><h2 id="tc">Bạn đang gặp triệu chứng gì?</h2><p>Chọn một triệu chứng để xem các bệnh có thể liên quan và dấu hiệu cần đi khám.</p></div><a class="link-more" href="#trieu-chung">Tra cứu nhiều triệu chứng {ic(a, "arrow-right")}</a></div>
  <div class="sym-grid">{syms}</div>
  <p class="sym-note">{ic(a, "alert-triangle")}<span>Đau ngực, khó thở dữ dội, yếu liệt hoặc lơ mơ: <b>gọi 115 ngay</b>. Công cụ chỉ gợi ý bài đọc, không phải chẩn đoán.</span></p>
</div></section>'''

    fs, fa = art(*FEATURE)
    ff = fs["featured"](fa)
    feature = (f'<a class="ed-feature" href="kien-thuc-tieu-hoa/{fa["slug"]}/">{thumb(a, fs, fa, "16/10")}'
               f'<span class="tag-cat">Tiêu hóa · {E(fs["tag"])}</span><h3>{E(fa["h1"])}</h3><p>{E(fa["desc"])}</p>{byline_mini(a, fs)}</a>'
               + (f'<p class="media-cap">{ff["credit"]}</p>' if ff and ff.get("credit") else ""))
    cards = ""
    for k, n in FEATURED_LIST:
        s, x = art(k, n)
        cards += (f'<a class="ed-card" href="kien-thuc-tieu-hoa/{x["slug"]}/">{thumb(a, s, x, "4/3")}'
                  f'<span><span class="tag-cat">{E(s["tag"])}</span><h3>{E(x["h1"])}</h3>{byline_mini(a, s)}</span></a>')
    ed_sec = f'''<section class="sec" aria-labelledby="bv"><div class="wrap">
  <div class="section-head"><div><span class="kicker">Bài viết nổi bật</span><h2 id="bv">Kiến thức được quan tâm</h2><p>Bài viết chuyên sâu, có tóm tắt nhanh, hình minh họa và tài liệu tham khảo.</p></div><a class="link-more" href="kien-thuc-tieu-hoa/">Tất cả bài viết {ic(a, "arrow-right")}</a></div>
  <div class="ed-grid"><div>{feature}</div><div class="ed-list">{cards}</div></div>
</div></section>'''

    n_art = sum(len(s["arts"]) for s in SERIES)
    doc_sec = f'''<section class="sec mint" aria-labelledby="bs"><div class="wrap">
  <div class="section-head"><div><span class="kicker">Đội ngũ chuyên môn</span><h2 id="bs">Bác sĩ phụ trách nội dung</h2></div></div>
  <div class="doctor">
    {L.media(a, None, "Ảnh chân dung " + L.AUTHOR["name"], ratio="4/5", icon="user", ph="Ảnh chân dung bác sĩ – đang chờ ảnh thật")}
    <div>
      <h3>{E(L.AUTHOR["name"])}</h3>
      <p class="muted" style="margin-top:4px">{E(L.AUTHOR["dept"])} · {E(L.AUTHOR["org"])}</p>
      <div class="roles"><span class="role">{ic(a, "pen")} Tác giả</span><span class="role">{ic(a, "stethoscope")} Phụ trách nội dung</span></div>
      <ul class="facts">
        <li>{ic(a, "badge-check")}<span>Công tác tại {E(L.AUTHOR_AFFIL)}.</span></li>
        <li>{ic(a, "check-circle")}<span>Tác giả {n_art} bài chuyên đề trong mục Kiến thức tiêu hóa.</span></li>
        <li>{ic(a, "check-circle")}<span>Trả lời câu hỏi của bạn đọc qua Zalo 0935 498 866.</span></li>
      </ul>
      <div class="acts"><a class="btn" href="kien-thuc-tieu-hoa/">{ic(a, "book-open")} Xem bài viết của bác sĩ</a><a class="btn ghost" href="{L.ZALO}" target="_blank" rel="noopener">{ic(a, "message")} Nhắn Zalo</a></div>
    </div>
  </div>
</div></section>'''

    tools = [
        ("#dinh-duong", "gauge", "Tính chỉ số BMI", "Đánh giá cân nặng theo ngưỡng dành cho người châu Á."),
        ("#benh-man-tinh", "activity", "Đọc chỉ số huyết áp", "Hiểu kết quả đo tại nhà theo các ngưỡng thường dùng."),
        ("#benh-man-tinh", "file-text", "Nhật ký huyết áp", "Ghi lại các lần đo trên máy của bạn để mang theo khi đi khám."),
        ("#trieu-chung", "thermometer", "Tra cứu triệu chứng", "Chọn dấu hiệu đang gặp để đọc về các bệnh có thể liên quan."),
    ]
    tcards = "".join(f'<a class="tool-card" href="{h}"><span class="ib">{ic(a, i)}</span><b>{E(tt)}</b><span>{E(d)}</span><em>Dùng công cụ {ic(a, "arrow-right")}</em></a>' for h, i, tt, d in tools)
    tool_sec = f'''<section class="sec alt" aria-labelledby="cc"><div class="wrap">
  <div class="section-head"><div><span class="kicker">Công cụ sức khỏe</span><h2 id="cc">Theo dõi sức khỏe tại nhà</h2></div></div>
  <div class="tool-grid">{tcards}</div>
  <p class="tool-foot">Các công cụ chỉ hỗ trợ theo dõi và đọc chỉ số, không tự động chẩn đoán và không thay thế ý kiến của bác sĩ.</p>
</div></section>'''

    return f'<div class="view" id="v-trang-chu">\n{hero}\n{spec_sec}\n{sym_sec}\n{ed_sec}\n{doc_sec}\n{tool_sec}\n</div>'


def fill(src, name, content):
    pat = re.compile(rf"(<!--{name}:START-->).*?(<!--{name}:END-->)", re.S)
    assert pat.search(src), f"thiếu vùng {name}"
    return pat.sub(lambda m: m.group(1) + "\n" + content + "\n" + m.group(2), src)


def build_index():
    p = g.ROOT / "index.html"
    s = p.read_text(encoding="utf-8")
    ld = [{"@context": "https://schema.org", "@type": "WebSite", "name": L.BRAND, "alternateName": "Bacsi115", "url": SITE + "/", "inLanguage": "vi",
           "potentialAction": {"@type": "SearchAction", "target": SITE + "/?q={search_term_string}", "query-input": "required name=search_term_string"}},
          L.ld_org()]
    headhtml = L.head("", SITE + "/", "Family Doctor (Bacsi115): Hiểu đúng bệnh, chăm sóc đúng cách",
                      "Tra cứu bệnh lý, triệu chứng và kiến thức sức khỏe bằng tiếng Việt dễ hiểu cho gia đình: tiêu hóa, tim mạch, hô hấp, nội tiết. Có nguồn tham khảo, không quảng cáo thuốc.",
                      None, "website", ld)
    s = fill(s, "HEAD", headhtml.rstrip())
    s = fill(s, "HEADER", L.header(""))
    s = fill(s, "HOME", build_home())
    s = fill(s, "FOOTER", L.footer(""))
    p.write_text(s, encoding="utf-8")


# ───────── Trang tổng quan chuyên đề ─────────
def build_hub():
    url = SITE + "/kien-thuc-tieu-hoa/"
    desc = "Kiến thức tiêu hóa dễ hiểu: chuyên đề trào ngược dạ dày – thực quản (GERD) và chuyên đề bệnh trĩ, mỗi chuyên đề gồm nhiều bài từ cơ bản đến chuyên sâu."
    sections = ""
    for ser in SERIES:
        cards = "".join(
            f'<a class="art-card" href="{x["slug"]}/">{thumb("../", ser, x, "16/9")}<span class="txt"><span class="tag-cat">{E(ser["tag"])} · Bài {x["n"]}</span>'
            f'<h3>{E(x["h1"])}</h3><p>{E(x["desc"])}</p><span class="byline-mini"><span>{ic("../", "clock")} {E(ser["read"](x))}</span>'
            f'<span>{ic("../", "refresh")} {L.fmt_date(ser["updated"])}</span></span></span></a>' for x in ser["arts"])
        sections += (f'<section class="sec" id="{ser["key"]}" style="padding-top:8px"><div class="section-head"><div><span class="kicker">Chuyên đề · {len(ser["arts"])} bài</span>'
                     f'<h2>{E(ser["name"])}</h2><p>{E(ser["desc"])}</p></div></div><div class="art-grid">{cards}</div></section>')
    crumbs = [("Trang chủ", "../"), ("Kiến thức tiêu hóa", None)]
    page = L.head("../", url, "Kiến thức tiêu hóa: trào ngược dạ dày (GERD) và bệnh trĩ | Family Doctor", desc, None, "website",
                  [L.ld_breadcrumb([("Trang chủ", SITE + "/"), ("Kiến thức tiêu hóa", url)])])
    page += L.header("../", current="chuyen-de")
    page += f'''<main id="main">
<div class="art-head"><div class="wrap"><div class="inner">
  {L._crumb_nav(crumbs)}
  <span class="tag-cat">{ic("../", "stomach")} Chuyên khoa Tiêu hóa</span>
  <h1>Kiến thức tiêu hóa</h1>
  <p class="sapo">Hai chuyên đề giúp bạn hiểu đúng bệnh, chăm sóc đúng cách và biết khi nào cần đi khám. Mỗi chuyên đề nên đọc theo thứ tự, bắt đầu từ Bài 1.</p>
</div></div></div>
<div class="wrap" style="padding-top:32px;padding-bottom:24px">{sections}</div>
</main>
'''
    page += L.footer("../", progress=False) + "\n</body>\n</html>\n"
    (g.OUT / "index.html").write_text(page, encoding="utf-8")


# ───────── Trang chính sách (bản nháp cần chủ site duyệt) ─────────
POLICIES = [
    dict(slug="chinh-sach-bien-tap", title="Chính sách biên tập", lead="Cách Family Doctor soạn, kiểm tra và cập nhật nội dung sức khỏe.",
         body=[("Mục tiêu", "<p>Family Doctor cung cấp thông tin sức khỏe bằng tiếng Việt dễ hiểu, giúp người bệnh và gia đình hiểu đúng bệnh, chăm sóc đúng cách và biết khi nào cần đi khám.</p>"),
               ("Nguồn tham khảo", "<p>Nội dung được soạn dựa trên hướng dẫn của Bộ Y tế, Tổ chức Y tế Thế giới và các hiệp hội chuyên ngành. Mỗi bài chuyên đề liệt kê tài liệu tham khảo ở cuối bài.</p>"),
               ("Tác giả", f"<p>Mỗi bài ghi rõ tác giả và ngày cập nhật.</p><p>Bác sĩ phụ trách nội dung hiện tại: {E(L.AUTHOR['name'])}, {E(L.AUTHOR_AFFIL)}.</p>"),
               ("Độc lập và quảng cáo", "<p>Family Doctor không quảng cáo thuốc, không nhận tài trợ để đưa thông tin về sản phẩm vào bài viết và không cam kết kết quả điều trị.</p>"),
               ("Cập nhật và góp ý", f'<p>Nội dung được rà soát khi có hướng dẫn mới. Nếu phát hiện thông tin chưa chính xác, vui lòng báo qua Zalo <a href="{L.ZALO}">0935 498 866</a>.</p>')]),
    dict(slug="chinh-sach-bao-mat", title="Chính sách bảo mật", lead="Family Doctor tôn trọng quyền riêng tư của bạn đọc.",
         body=[("Dữ liệu chúng tôi thu thập", "<p>Website không yêu cầu đăng ký tài khoản và không thu thập thông tin cá nhân trên máy chủ.</p>"),
               ("Biểu mẫu hỏi bác sĩ", "<p>Biểu mẫu “Hỏi bác sĩ” chỉ soạn sẵn nội dung để bạn tự gửi qua Zalo. Câu hỏi chỉ được gửi khi bạn chủ động gửi trong ứng dụng Zalo và không được đăng công khai trên website.</p>"),
               ("Dữ liệu lưu trên thiết bị", "<p>Công cụ Nhật ký huyết áp lưu các lần đo trong bộ nhớ trình duyệt của chính bạn (localStorage). Dữ liệu không được gửi đi và có thể xóa bất cứ lúc nào bằng nút “Xóa nhật ký”.</p>"),
               ("Dịch vụ bên thứ ba", "<p>Website được lưu trữ trên GitHub Pages. Nhà cung cấp hạ tầng có thể ghi nhận thông tin kỹ thuật như địa chỉ IP theo chính sách của họ.</p>"),
               ("Liên hệ", f'<p>Mọi câu hỏi về quyền riêng tư, vui lòng liên hệ qua Zalo <a href="{L.ZALO}">0935 498 866</a>.</p>')]),
    dict(slug="mien-tru-trach-nhiem", title="Miễn trừ trách nhiệm y khoa", lead="Thông tin trên Family Doctor nhằm mục đích giáo dục sức khỏe.",
         body=[("Không thay thế khám bệnh", "<p>Nội dung trên website không thay thế việc khám, chẩn đoán hoặc chỉ định điều trị của bác sĩ. Mỗi người bệnh cần được đánh giá riêng.</p>"),
               ("Dùng thuốc", "<p>Không tự ý dùng, ngừng hoặc thay đổi liều thuốc dựa trên thông tin trên website. Hãy hỏi bác sĩ hoặc dược sĩ trước khi dùng thuốc.</p>"),
               ("Công cụ tra cứu", "<p>Công cụ tra triệu chứng, tính BMI, đọc chỉ số và nhật ký huyết áp chỉ hỗ trợ theo dõi và tìm bài đọc, không đưa ra chẩn đoán.</p>"),
               ("Khi nào cần cấp cứu", "<div class=\"alert danger\"><div><b>Gọi 115 hoặc đến cơ sở y tế gần nhất ngay khi</b>khó thở, đau ngực, yếu liệt hoặc tê một bên người, lơ mơ, co giật, chảy máu nhiều.</div></div>")]),
]


def build_policies():
    for p in POLICIES:
        url = f"{SITE}/{p['slug']}/"
        body = "".join(f'<section><h2 id="{g.slugify(h)}">{E(h)}</h2>{b}</section>' for h, b in p["body"])
        body += '<p class="disclaimer-box">Phiên bản ngày 23/11/2026.</p>'
        page = L.simple_page("../", url=url, title=f"{p['title']} | Family Doctor", desc=p["lead"],
                             crumbs=[("Trang chủ", "../"), (p["title"], None)], h1=p["title"], lead=p["lead"], body_html=body,
                             ld=[L.ld_breadcrumb([("Trang chủ", SITE + "/"), (p["title"], url)])])
        d = g.ROOT / p["slug"]
        d.mkdir(exist_ok=True)
        (d / "index.html").write_text(page, encoding="utf-8")


def build_404():
    # GitHub Pages phục vụ 404.html ở mọi đường dẫn → dùng đường dẫn tuyệt đối "/".
    body = ('<section><p>Trang bạn tìm có thể đã được đổi địa chỉ hoặc không còn tồn tại.</p>'
            '<p><a class="btn" href="/">Về trang chủ</a> <a class="btn ghost" href="/kien-thuc-tieu-hoa/">Kiến thức tiêu hóa</a></p></section>')
    page = L.simple_page("/", url=SITE + "/404.html", title="Không tìm thấy trang | Family Doctor", desc="Không tìm thấy trang.",
                         crumbs=[("Trang chủ", "/"), ("Không tìm thấy trang", None)], h1="Không tìm thấy trang", lead="Lỗi 404", body_html=body)
    page = page.replace('<meta name="robots" content="index, follow, max-image-preview:large">', '<meta name="robots" content="noindex">')
    (g.ROOT / "404.html").write_text(page, encoding="utf-8")


def build_sitemap():
    urls = ["", "kien-thuc-tieu-hoa/"]
    urls += [f"kien-thuc-tieu-hoa/{x['slug']}/" for s in SERIES for x in s["arts"]]
    urls += [f"{p['slug']}/" for p in POLICIES]
    body = "".join(f"  <url><loc>{SITE}/{u}</loc><lastmod>{tc.MODIFIED}</lastmod></url>\n" for u in urls)
    (g.ROOT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + body + "</urlset>\n",
        encoding="utf-8")


if __name__ == "__main__":
    for a in g.ARTICLES:
        g.build_article(a)
    t.build_all_articles()
    build_hub()
    build_policies()
    build_404()
    build_index()
    build_sitemap()
    print("Đã tạo", len(g.ARTICLES), "bài GERD,", len(tc.ARTICLES), "bài trĩ, trang tổng quan, 3 trang chính sách, 404, index.html và sitemap")
