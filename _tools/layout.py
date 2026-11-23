"""Thành phần giao diện dùng chung cho Bacsi115.com (Family Doctor).

`a` là tiền tố đường dẫn tới thư mục gốc: "" cho trang chủ, "../" cho trang cấp 1, "../../" cho bài viết.
Các thành phần:
  ic()            – biểu tượng từ assets/icons.svg
  head()          – <head> chuẩn SEO (title, description, canonical, Open Graph, Twitter, favicon, JSON-LD)
  header()/footer() – đầu và chân trang
  media()         – Image component: tỉ lệ cố định, width/height, lazy/priority, WebP, placeholder có chủ đích
  article_page()  – ArticleLayout dùng cho mọi bài viết
  simple_page()   – trang nội dung đơn giản (chính sách, giới thiệu…)
"""
import html
import json
from pathlib import Path

E = html.escape
ROOT = Path(__file__).resolve().parent.parent
SITE = "https://bacsi115.com"
ZALO = "https://zalo.me/0935498866"
BRAND = "Family Doctor"
TAGLINE = "Hiểu đúng bệnh. Chăm sóc đúng cách."
OG_DEFAULT = "assets/og-default.png"

# Hồ sơ tác giả: CHỈ ghi thông tin đã xác minh. Bằng cấp/chuyên khoa để trống cho tới khi có dữ liệu thật.
AUTHOR = dict(name="BS. Thái Hoàng", role="Bác sĩ phụ trách nội dung Family Doctor",
              dept="Khoa Ngoại tổng hợp", org="Bệnh viện Nhân dân 115",
              verified=["Khoa Ngoại tổng hợp, Bệnh viện Nhân dân 115"])  # do chủ site cung cấp; học hàm, học vị, chứng chỉ chưa có dữ liệu
AUTHOR_AFFIL = AUTHOR["dept"] + ", " + AUTHOR["org"]
REVIEWER = None  # dict(name=..., role=...) khi có người duyệt chuyên môn thật

FONT_LINK = f'<link rel="stylesheet" href="{{a}}assets/fonts/fonts.css">'

POPULAR = ["Trào ngược dạ dày", "Bệnh trĩ", "Tăng huyết áp", "Sốt xuất huyết"]


def ic(a, name, cls=""):
    return f'<svg class="i {cls}" aria-hidden="true"><use href="{a}assets/icons.svg#{name}"/></svg>'


def logo(a, href=None):
    href = href or f"{a}#trang-chu"
    return (f'<a class="logo" href="{href}" aria-label="{BRAND} – Bacsi115.com, về trang chủ">'
            f'<span class="logo-mark" aria-hidden="true">{ic(a, "heart-pulse")}</span>'
            f'<span><b>{BRAND}</b><small>{TAGLINE}</small></span></a>')


# ───────── Image component ─────────
def media(a, src=None, alt="", w=None, h=None, ratio="16/9", priority=False, cls="", ph=None, icon="image", webp=None):
    """Ảnh có tỉ lệ cố định. src=None → placeholder có chủ đích (ghi rõ đang chờ ảnh thật)."""
    style = f"--ratio:{ratio}"
    if not src:
        return (f'<figure class="media ph {cls}" style="{style}" role="img" aria-label="{E(alt)}">'
                f'<div class="ph-inner">{ic(a, icon)}<span>{E(ph or "Ảnh minh họa đang chờ cập nhật")}</span></div></figure>')
    contain = " contain" if src.endswith(".svg") else ""
    load = 'loading="eager" fetchpriority="high"' if priority else 'loading="lazy"'
    size = f' width="{w}" height="{h}"' if w and h else ""
    img = f'<img src="{a}{src}" alt="{E(alt)}"{size} {load} decoding="async">'
    if webp:
        img = f'<picture><source type="image/webp" srcset="{a}{webp}">{img}</picture>'
    return f'<figure class="media{contain} {cls}" style="{style}">{img}</figure>'


# ───────── <head> ─────────
def head(a, canonical, title, desc, og_image=None, og_type="article", ld=None, extra=""):
    og_image = og_image or f"{SITE}/{OG_DEFAULT}"
    lds = "".join('<script type="application/ld+json">\n' + json.dumps(x, ensure_ascii=False, indent=1) + "\n</script>\n" for x in (ld or []))
    return f'''<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<link rel="canonical" href="{canonical}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta property="og:type" content="{og_type}">
<meta property="og:locale" content="vi_VN">
<meta property="og:site_name" content="{BRAND} – Bacsi115.com">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(desc)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{og_image}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#087E83">
<link rel="icon" href="{a}favicon.ico" sizes="any">
<link rel="icon" href="{a}assets/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{a}assets/apple-touch-icon.png">
<link rel="preload" href="{a}assets/fonts/be-vietnam-pro-400-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{a}assets/fonts/be-vietnam-pro-700-vietnamese.woff2" as="font" type="font/woff2" crossorigin>
{FONT_LINK.format(a=a)}
<link rel="stylesheet" href="{a}assets/style.css">
{lds}{extra}</head>
<body>
<a class="skip" href="#main">Bỏ qua tới nội dung chính</a>
'''


# ───────── Đầu trang ─────────
def _sub(a, icon, title, desc, href):
    return (f'<a href="{href}"><span class="ib">{ic(a, icon)}</span>'
            f'<span><b>{title}</b><small>{desc}</small></span></a>')


def header(a="", current=None):
    cur = " cur" if current == "chuyen-de" else ""
    chuyen_de = "".join([
        _sub(a, "stomach", "Kiến thức tiêu hóa", "Tổng quan các chuyên đề", f"{a}kien-thuc-tieu-hoa/"),
        _sub(a, "droplet", "Trào ngược dạ dày (GERD)", "6 bài: từ nhận biết đến điều trị", f"{a}kien-thuc-tieu-hoa/#gerd"),
        _sub(a, "heart-pulse", "Bệnh trĩ", "7 bài: dấu hiệu, phân độ, điều trị", f"{a}kien-thuc-tieu-hoa/#tri"),
    ])
    song_khoe = "".join([
        _sub(a, "shield-check", "Phòng bệnh", "Lịch khám, tầm soát, tiêm chủng", f"{a}#phong-benh"),
        _sub(a, "users", "Sức khỏe theo tuổi", "Chăm sóc từng giai đoạn", f"{a}#suc-khoe-theo-tuoi"),
        _sub(a, "activity", "Bệnh mạn tính", "Huyết áp, đường huyết, mỡ máu", f"{a}#benh-man-tinh"),
        _sub(a, "apple", "Dinh dưỡng & lối sống", "Ăn, ngủ, vận động, BMI", f"{a}#dinh-duong"),
    ])
    action = a or "./"
    chips = "".join(f'<a class="chip" href="{action}?q={E(q)}">{E(q)}</a>' for q in POPULAR)
    return f'''<div class="topbar"><div class="wrap">
  <span class="em"><b>115</b> Cấp cứu ngay nếu khó thở, đau ngực, yếu liệt hoặc lơ mơ</span>
  <span class="hot">{ic(a, "phone")} Hỏi bác sĩ qua Zalo: <a href="{ZALO}">0935 498 866</a></span>
</div></div>
<header class="site">
  <div class="wrap">
    {logo(a)}
    <nav class="main" id="mainNav" aria-label="Điều hướng chính">
      <a href="{a}#trang-chu">Trang chủ</a>
      <a href="{a}#benh-thuong-gap">Bệnh thường gặp</a>
      <a href="{a}#trieu-chung">Triệu chứng</a>
      <div class="has-sub{cur}"><button type="button" aria-haspopup="true">Chuyên đề {ic(a, "chevron-down")}</button><div class="sub-menu">{chuyen_de}</div></div>
      <div class="has-sub"><button type="button" aria-haspopup="true">Sống khỏe {ic(a, "chevron-down")}</button><div class="sub-menu">{song_khoe}</div></div>
    </nav>
    <div class="hd-actions">
      <button class="icon-btn" id="searchBtn" type="button" aria-expanded="false" aria-controls="siteSearch" aria-label="Tìm kiếm">{ic(a, "search")}</button>
      <a class="btn sm hd-cta" href="{a}#hoi-bac-si">{ic(a, "message")} Hỏi bác sĩ</a>
      <button class="menu-btn" id="menuBtn" type="button" aria-expanded="false" aria-controls="mainNav">{ic(a, "menu")} Menu</button>
    </div>
  </div>
  <div class="search-panel" id="siteSearch" hidden>
    <div class="wrap">
      <form action="{action}" method="get" role="search">
        <label class="sr-only" for="siteQ">Tìm bệnh, triệu chứng</label>
        <input id="siteQ" name="q" type="search" placeholder="Tìm bệnh hoặc triệu chứng, ví dụ: trào ngược dạ dày" autocomplete="off">
        <button class="btn" type="submit">{ic(a, "search")} Tìm</button>
      </form>
      <div class="quick"><span>Hay tìm:</span>{chips}</div>
    </div>
  </div>
</header>
'''


HEADER_SCRIPT = '''<script>
(function(){
  var m=document.getElementById("menuBtn"),n=document.getElementById("mainNav");
  if(m&&!m.dataset.bound){m.dataset.bound=1;m.addEventListener("click",function(){var o=n.classList.toggle("open");m.setAttribute("aria-expanded",String(o));});}
  var s=document.getElementById("searchBtn"),p=document.getElementById("siteSearch");
  if(s&&!s.dataset.bound){s.dataset.bound=1;s.addEventListener("click",function(){var open=p.hasAttribute("hidden");if(open){p.removeAttribute("hidden");document.getElementById("siteQ").focus();}else{p.setAttribute("hidden","");}s.setAttribute("aria-expanded",String(open));});}
  document.addEventListener("keydown",function(e){if(e.key==="Escape"&&p&&!p.hasAttribute("hidden")){p.setAttribute("hidden","");s.setAttribute("aria-expanded","false");s.focus();}});
  var b=document.getElementById("progressBar");
  if(b){var u=function(){var h=document.documentElement,t=h.scrollHeight-h.clientHeight;b.style.width=(t>0?Math.min(100,h.scrollTop/t*100):0)+"%";};addEventListener("scroll",function(){requestAnimationFrame(u)},{passive:true});requestAnimationFrame(u);}
})();
</script>'''


# ───────── Chân trang ─────────
def footer(a="", progress=False, script=True):
    prog = '<div class="progress" aria-hidden="true"><i id="progressBar"></i></div>\n' if progress else ""
    return f'''
{prog}<footer class="site-footer">
  <div class="wrap">
    <div class="foot-main">
      <div>
        {logo(a)}
        <p class="foot-about">Nền tảng kiến thức sức khỏe bằng tiếng Việt cho gia đình, người bệnh và người chăm sóc. Nội dung dễ hiểu, có nguồn tham khảo, không quảng cáo thuốc.</p>
        <div class="foot-contact">
          <span>{ic(a, "stethoscope")} {AUTHOR["name"]} – {AUTHOR_AFFIL}</span>
          <span>{ic(a, "message")} Zalo: <a href="{ZALO}">0935 498 866</a></span>
        </div>
      </div>
      <div><h2>Tra cứu</h2><ul>
        <li><a href="{a}#benh-thuong-gap">Bệnh thường gặp</a></li>
        <li><a href="{a}#trieu-chung">Tra cứu triệu chứng</a></li>
        <li><a href="{a}#phong-benh">Phòng bệnh</a></li>
        <li><a href="{a}#suc-khoe-theo-tuoi">Sức khỏe theo tuổi</a></li>
        <li><a href="{a}#benh-man-tinh">Bệnh mạn tính</a></li>
        <li><a href="{a}#dinh-duong">Dinh dưỡng &amp; BMI</a></li></ul></div>
      <div><h2>Chuyên đề</h2><ul>
        <li><a href="{a}kien-thuc-tieu-hoa/">Kiến thức tiêu hóa</a></li>
        <li><a href="{a}kien-thuc-tieu-hoa/#gerd">Trào ngược dạ dày (GERD)</a></li>
        <li><a href="{a}kien-thuc-tieu-hoa/#tri">Bệnh trĩ</a></li>
        <li><a href="{a}#hoi-bac-si">Hỏi bác sĩ</a></li></ul></div>
      <div><h2>Thông tin</h2><ul>
        <li><a href="{a}chinh-sach-bien-tap/">Chính sách biên tập</a></li>
        <li><a href="{a}chinh-sach-bao-mat/">Chính sách bảo mật</a></li>
        <li><a href="{a}mien-tru-trach-nhiem/">Miễn trừ trách nhiệm y khoa</a></li>
        <li><a href="{ZALO}">Liên hệ qua Zalo</a></li></ul></div>
    </div>
    <p class="foot-disc">{ic(a, "alert-triangle")}<span><b>Lưu ý y khoa:</b> Thông tin trên {BRAND} chỉ nhằm mục đích giáo dục sức khỏe, không thay thế khám, chẩn đoán và điều trị của bác sĩ. Khi có dấu hiệu nguy hiểm, gọi <b>115</b> hoặc đến cơ sở y tế gần nhất.</span></p>
    <div class="foot-bottom"><span>© 2026 {BRAND} · Bacsi115.com</span><span>{TAGLINE}</span></div>
  </div>
</footer>
{HEADER_SCRIPT if script else ""}'''


# ───────── JSON-LD ─────────
def ld_org():
    return {"@context": "https://schema.org", "@type": "Organization", "name": BRAND, "alternateName": "Bacsi115",
            "url": SITE + "/", "logo": SITE + "/assets/logo-512.png"}


def ld_breadcrumb(crumbs):
    """crumbs: [(tên, URL tuyệt đối), …]"""
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": u} for i, (n, u) in enumerate(crumbs)]}


def _crumb_nav(crumbs):
    items = "".join((f'<li><a href="{h}">{E(n)}</a></li>' if h else f'<li aria-current="page">{E(n)}</li>') for n, h in crumbs)
    return f'<nav class="crumb" aria-label="Đường dẫn"><ol>{items}</ol></nav>'


def fmt_date(d):
    y, m, dd = d.split("-")
    return f"{dd}/{m}/{y}"


# ───────── ArticleLayout ─────────
def article_page(a, *, url, seo_title, desc, crumbs, category, h1, sapo, published, modified, read_time,
                 featured, summary, toc, sections_html, faq, refs, related, series_title, series_items,
                 pager, ld, og_image=None, side_extra=""):
    """Trả về toàn bộ HTML một bài viết theo thứ tự:
    breadcrumb → chuyên mục → H1 → sapo → tác giả → người duyệt → ngày đăng/cập nhật/thời gian đọc → ảnh đại diện →
    tóm tắt nhanh → mục lục → nội dung (hộp cảnh báo, hình minh họa) → hỏi đáp → tài liệu tham khảo →
    bài liên quan → thông tin tác giả → miễn trừ trách nhiệm."""
    reviewer = (f'<b>{E(REVIEWER["name"])}</b>' if REVIEWER else '<span class="pending">Đang cập nhật</span>')
    hero = ""
    if featured:
        cap = f'<p class="media-cap">{featured.get("caption", "")}{" · " + featured["credit"] if featured.get("credit") else ""}</p>'
        hero = (f'<div class="art-hero">{media(a, featured["src"], featured["alt"], featured.get("w"), featured.get("h"), "16/9", True, webp=featured.get("webp"))}{cap}</div>')
    summary_html = ""
    if summary:
        summary_html = (f'<section class="summary" aria-labelledby="tom-tat"><h2 id="tom-tat">{ic(a, "list-check")} Tóm tắt nhanh</h2>'
                        f'<ul>{"".join(f"<li>{s}</li>" for s in summary)}</ul></section>')
    toc_html = ('<nav class="toc" aria-labelledby="muc-luc"><h2 id="muc-luc">Nội dung bài viết</h2><ol>'
                + "".join(f'<li><a href="#{i}">{E(t)}</a></li>' for i, t in toc) + "</ol></nav>")
    faq_html = ""
    if faq:
        faq_html = ('<section class="faq"><h2 id="hoi-dap">Câu hỏi thường gặp</h2>'
                    + "".join(f"<details><summary>{E(q)}</summary><p>{E(ans)}</p></details>" for q, ans in faq) + "</section>")
    refs_html = ('<section class="refs-block"><h2 id="tai-lieu-tham-khao">Tài liệu tham khảo</h2><ol class="refs">'
                 + "".join(f"<li>{r}</li>" for r in refs) + "</ol></section>") if refs else ""
    rel_html = ""
    if related:
        rel_html = ('<section class="related"><h2>Bài viết liên quan</h2><div class="rel-grid">'
                    + "".join(f'<a class="rel-card" href="{r["url"]}"><span class="tag-cat">{E(r["tag"])}</span><b>{E(r["title"])}</b><span>{E(r["desc"])}</span></a>' for r in related)
                    + "</div></section>")
    verified = "".join(f"<li>{E(v)}</li>" for v in AUTHOR["verified"])
    author_box = (f'<section class="author-box" aria-labelledby="tac-gia"><span class="avatar">{ic(a, "user", "lg")}</span><div>'
                  f'<h2 id="tac-gia">Về tác giả: {E(AUTHOR["name"])}</h2>'
                  f'<p>{E(AUTHOR["role"])}.</p>'
                  + (f'<ul class="list" style="margin-top:8px">{verified}</ul>' if verified else '')
                  + '<p class="pending">Học hàm, học vị và chứng chỉ hành nghề: đang bổ sung.</p>'
                  + f'<p><a href="{a}kien-thuc-tieu-hoa/">Xem các bài viết</a> · <a href="{ZALO}">Liên hệ qua Zalo</a></p></div></section>')
    disclaimer = (f'<p class="disclaimer-box"><b>Miễn trừ trách nhiệm:</b> Bài viết cung cấp thông tin giáo dục sức khỏe, không thay thế khám, chẩn đoán hoặc chỉ định điều trị của bác sĩ. '
                  f'Không tự ý dùng, ngừng hay đổi liều thuốc. Khi có dấu hiệu nguy hiểm, gọi 115. <a href="{a}mien-tru-trach-nhiem/">Đọc đầy đủ</a>.</p>')
    page = head(a, url, seo_title, desc, og_image, "article", ld)
    page += header(a, current="chuyen-de")
    page += f'''<main id="main">
<div class="art-head"><div class="wrap"><div class="inner">
  {_crumb_nav(crumbs)}
  <a class="tag-cat" href="{category[1]}">{E(category[0])}</a>
  <h1>{E(h1)}</h1>
  <p class="sapo">{E(sapo)}</p>
  <div class="byline">
    <div class="person"><span class="avatar">{ic(a, "user")}</span><div><small>Tác giả · {E(AUTHOR_AFFIL)}</small><b>{E(AUTHOR["name"])}</b></div></div>
    <div class="person"><span class="avatar">{ic(a, "badge-check")}</span><div><small>Người duyệt chuyên môn</small>{reviewer}</div></div>
    <div class="dates"><span>{ic(a, "calendar")} Đăng {fmt_date(published)}</span><span>{ic(a, "refresh")} Cập nhật {fmt_date(modified)}</span><span>{ic(a, "clock")} {E(read_time)}</span></div>
  </div>
</div>{hero}</div></div>
<div class="art-body"><div class="wrap"><div class="article-grid">
  <article class="article">
    {summary_html}
    {toc_html}
    {sections_html}
    {faq_html}
    {refs_html}
    {rel_html}
    {author_box}
    {disclaimer}
    {pager}
  </article>
  <aside aria-label="Chuyên đề">
    <div class="side-card"><h3>{E(series_title)}</h3><ol class="series">{series_items}</ol><p style="margin-top:12px"><a class="link-more" href="{a}kien-thuc-tieu-hoa/">Tất cả chuyên đề {ic(a, "arrow-right")}</a></p></div>
    {side_extra}
    <div class="side-card"><h3>Còn thắc mắc?</h3><p class="muted" style="font-size:.92rem">Nhắn {E(AUTHOR["name"])} qua Zalo để được hướng dẫn.</p><p style="margin-top:12px"><a class="btn ghost sm" href="{ZALO}" target="_blank" rel="noopener">{ic(a, "message")} Nhắn Zalo</a></p></div>
  </aside>
</div></div></div>
</main>
'''
    page += footer(a, progress=True)
    page += "\n</body>\n</html>\n"
    return page


def simple_page(a, *, url, title, desc, crumbs, h1, lead, body_html, ld=None):
    page = head(a, url, title, desc, None, "website", ld)
    page += header(a)
    page += f'''<main id="main">
<div class="art-head"><div class="wrap"><div class="inner">
  {_crumb_nav(crumbs)}
  <h1>{E(h1)}</h1>
  <p class="sapo">{E(lead)}</p>
</div></div></div>
<div class="art-body"><div class="wrap"><article class="article">{body_html}</article></div></div>
</main>
'''
    page += footer(a, progress=False)
    page += "\n</body>\n</html>\n"
    return page
