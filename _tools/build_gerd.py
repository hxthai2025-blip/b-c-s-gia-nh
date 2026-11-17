#!/usr/bin/env python3
"""Tạo 6 trang chuyên đề GERD từ các file Word trong _tools/gerd/.

Chạy từ thư mục gốc của repo:  python3 _tools/build_gerd.py
Cần có pandoc và BeautifulSoup (bs4).
Thư mục bắt đầu bằng "_" không được GitHub Pages đăng lên web.
"""
import html, json, re, subprocess, unicodedata
from pathlib import Path
from bs4 import BeautifulSoup, NavigableString

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "_tools" / "gerd"
OUT = ROOT / "kien-thuc-tieu-hoa"
SITE = "https://bacsi115.com"
AUTHOR = "BS. Thái Hoàng"
PUBLISHED = "2026-11-17"
MODIFIED = "2026-11-17"

ARTICLES = [
  dict(n=1, file="01_GERD_va_phan_biet_voi_viem_loet_da_day.docx",
    slug="gerd-la-gi-trieu-chung-phan-biet-viem-loet-da-day",
    h1="GERD là gì? Cách nhận biết và phân biệt với viêm loét dạ dày",
    short="GERD là gì? Nhận biết và phân biệt với viêm loét dạ dày",
    seo="GERD là gì? Triệu chứng và cách phân biệt với đau dạ dày",
    desc="GERD gây ợ nóng, ợ trớ và khó chịu sau ăn. Tìm hiểu dấu hiệu thường gặp, cách chẩn đoán và phân biệt GERD với viêm loét dạ dày – tá tràng.",
    faq=[("GERD là bệnh gì?","GERD là bệnh trào ngược dạ dày – thực quản, xảy ra khi dịch dạ dày trào ngược gây triệu chứng khó chịu hoặc biến chứng."),
         ("Ợ nóng có phải luôn là GERD?","Ợ nóng là triệu chứng điển hình nhưng không đủ để tự xác định bệnh. Bác sĩ cần đánh giá bệnh sử, dấu hiệu cảnh báo và chỉ định thăm dò khi cần."),
         ("GERD khác viêm loét dạ dày như thế nào?","GERD chủ yếu gây trào ngược lên thực quản; viêm loét dạ dày – tá tràng liên quan tổn thương niêm mạc dạ dày hoặc tá tràng. Triệu chứng có thể chồng lấp.")],
    links={"4.":[(2,"chế độ ăn cho người bị trào ngược dạ dày – thực quản"),(3,"các thuốc điều trị GERD và cách sử dụng an toàn")],
           "5.":[(4,"nguyên nhân khiến GERD dai dẳng hoặc khó kiểm soát"),(5,"Barrett thực quản – biến chứng cần theo dõi của GERD")]}),
  dict(n=2, file="02_Che_do_an_cho_nguoi_bi_GERD.docx",
    slug="trao-nguoc-da-day-nen-an-gi-kieng-gi",
    h1="Chế độ ăn cho người bị trào ngược dạ dày – thực quản",
    short="Chế độ ăn cho người bị trào ngược dạ dày – thực quản",
    seo="Người bị trào ngược dạ dày nên ăn gì và kiêng gì?",
    desc="Người bị trào ngược dạ dày nên ăn gì, hạn chế gì? Xem nguyên tắc ăn uống, cách nhận diện thực phẩm khởi phát triệu chứng và thói quen giúp giảm trào ngược.",
    faq=[("Người bị trào ngược dạ dày nên ăn gì?","Ưu tiên khẩu phần cân đối, lượng vừa phải, thực phẩm dễ dung nạp và cách chế biến ít dầu mỡ. Không có một thực đơn duy nhất phù hợp với tất cả."),
         ("Bị GERD có phải kiêng cà phê và trái cây chua hoàn toàn không?","Không nhất thiết. Chỉ nên hạn chế những món thực sự làm triệu chứng nặng hơn ở từng người."),
         ("Ăn tối trước khi ngủ bao lâu?","Nên kết thúc bữa ăn ít nhất 2–3 giờ trước khi nằm.")],
    links={"Mở đầu":[(1,"GERD là gì và cách nhận biết")],
           "6.":[(3,"các nhóm thuốc điều trị GERD và cách sử dụng an toàn")],
           "Thông điệp":[(4,"vì sao triệu chứng trào ngược vẫn kéo dài dù đã điều trị")]}),
  dict(n=3, file="03_Thuoc_dieu_tri_GERD_va_su_dung_an_toan.docx",
    slug="thuoc-dieu-tri-trao-nguoc-da-day-cach-dung-ppi",
    h1="Các nhóm thuốc điều trị GERD và cách sử dụng an toàn",
    short="Các nhóm thuốc điều trị GERD và cách sử dụng an toàn",
    seo="Thuốc điều trị trào ngược dạ dày: Cách dùng PPI an toàn",
    desc="Tìm hiểu các nhóm thuốc điều trị GERD, cách dùng PPI đúng thời điểm, vai trò của thuốc khác và những lưu ý để tránh tự ý dùng thuốc kéo dài.",
    faq=[("PPI nên uống lúc nào?","Nhiều PPI dạng uống thông thường được dùng trước bữa ăn 30–60 phút; thời điểm cụ thể phụ thuộc loại thuốc và hướng dẫn kê đơn."),
         ("Uống PPI lâu dài có nguy hiểm không?","PPI có chỉ định và lợi ích rõ trong nhiều trường hợp. Việc dùng kéo dài cần được bác sĩ đánh giá định kỳ về chỉ định, liều và thời gian."),
         ("Có thể tự tăng gấp đôi liều PPI khi còn ợ nóng không?","Không nên tự tăng liều. Cần kiểm tra cách dùng, tuân thủ, chẩn đoán và nguyên nhân khác trước khi điều chỉnh điều trị.")],
    links={"Mở đầu":[(1,"GERD là gì và cách nhận biết"),(2,"chế độ ăn cho người bị trào ngược dạ dày – thực quản")],
           "7.":[(4,"GERD kháng trị: vì sao uống thuốc mãi không khỏi"),(6,"khi nào có thể cân nhắc phẫu thuật chống trào ngược")]}),
  dict(n=4, file="04_GERD_khang_tri_vi_sao_uong_thuoc_khong_khoi.docx",
    slug="gerd-khang-tri-uong-thuoc-trao-nguoc-khong-khoi",
    h1="GERD kháng trị: Vì sao uống thuốc mãi không khỏi?",
    short="GERD kháng trị: Vì sao uống thuốc mãi không khỏi?",
    seo="GERD kháng trị: Vì sao uống thuốc trào ngược không khỏi?",
    desc="Ợ nóng, ợ trớ vẫn kéo dài dù dùng thuốc? Tìm hiểu GERD kháng trị, những nguyên nhân thường gặp và các xét nghiệm bác sĩ có thể chỉ định.",
    faq=[("Khi nào được gọi là GERD kháng trị?","Cần có bằng chứng khách quan về GERD và triệu chứng còn dai dẳng sau khi đã tối ưu hóa điều trị. Một định nghĩa thường dùng là còn triệu chứng dù dùng PPI liều gấp đôi ít nhất 8 tuần."),
         ("Vì sao uống PPI mà vẫn ợ nóng?","Có thể do dùng thuốc chưa đúng thời điểm, tuân thủ chưa đủ, trào ngược không acid, quá mẫn thực quản hoặc nguyên nhân khác không phải GERD."),
         ("GERD kháng trị có cần nội soi không?","Bác sĩ cân nhắc nội soi và các thăm dò sinh lý thực quản tùy tình huống, đặc biệt khi triệu chứng kéo dài hoặc đang xem xét can thiệp.")],
    links={"2.":[(3,"cách dùng PPI đúng thời điểm và an toàn")],
           "3.":[(5,"Barrett thực quản và nguy cơ biến chứng của GERD")],
           "5.":[(6,"khi nào có thể cân nhắc phẫu thuật chống trào ngược")]}),
  dict(n=5, file="05_Barrett_thuc_quan_tu_trieu_chung_den_theo_doi.docx",
    slug="barrett-thuc-quan-la-gi-nguy-co-ung-thu-theo-doi",
    h1="Barrett thực quản: Khi nào trào ngược dạ dày trở nên đáng lo?",
    short="Barrett thực quản: Khi nào trào ngược trở nên đáng lo?",
    seo="Barrett thực quản là gì? Nguy cơ ung thư và lịch theo dõi",
    desc="Barrett thực quản là tổn thương tiền ung thư nhưng không đồng nghĩa chắc chắn mắc ung thư. Tìm hiểu chẩn đoán, phân tầng nguy cơ và theo dõi nội soi.",
    faq=[("Barrett thực quản có phải ung thư không?","Không. Barrett là biến đổi niêm mạc thực quản làm tăng nguy cơ ung thư biểu mô tuyến, nhưng đa số người bệnh không tiến triển thành ung thư."),
         ("Barrett thực quản được chẩn đoán bằng cách nào?","Chẩn đoán dựa trên nội soi kết hợp sinh thiết và đánh giá mô bệnh học."),
         ("Người mắc Barrett cần nội soi bao lâu một lần?","Khoảng cách theo dõi phụ thuộc chiều dài đoạn Barrett, kết quả mô bệnh học và hướng dẫn chuyên môn. Bác sĩ sẽ cá thể hóa lịch theo dõi.")],
    links={"1.":[(1,"bệnh trào ngược dạ dày – thực quản (GERD)")],
           "2.":[(4,"GERD kéo dài, khó kiểm soát dù đã dùng thuốc")],
           "5.":[(6,"phẫu thuật chống trào ngược và giới hạn của nó")]}),
  dict(n=6, file="06_Phau_thuat_chong_trao_nguoc_trong_GERD_khang_tri.docx",
    slug="phau-thuat-trao-nguoc-da-day-khi-nao-can",
    h1="Phẫu thuật chống trào ngược trong GERD kháng trị",
    short="Phẫu thuật chống trào ngược trong GERD kháng trị",
    seo="Phẫu thuật trào ngược dạ dày: Khi nào cần và có hiệu quả không?",
    desc="Phẫu thuật chống trào ngược được cân nhắc ở người bệnh chọn lọc sau khi xác nhận GERD khách quan. Tìm hiểu chỉ định, đánh giá trước mổ, kỹ thuật và nguy cơ.",
    faq=[("GERD kháng trị có phải mổ không?","Không phải tất cả. Chỉ cân nhắc phẫu thuật ở người bệnh phù hợp sau khi xác nhận GERD khách quan, đánh giá triệu chứng và chức năng thực quản."),
         ("Trước phẫu thuật chống trào ngược cần làm xét nghiệm gì?","Thường cần nội soi, đo pH hoặc pH – trở kháng thực quản và đo áp lực thực quản độ phân giải cao; một số trường hợp cần chụp thực quản cản quang."),
         ("Nissen và Toupet khác nhau thế nào?","Nissen tạo van quấn đáy vị 360°, còn Toupet là quấn bán phần khoảng 270°. Lựa chọn phụ thuộc giải phẫu, chức năng nhu động và đánh giá của ê-kíp điều trị.")],
    links={"1.":[(4,"GERD kháng trị và cách bác sĩ đánh giá")],
           "2.":[(3,"tối ưu điều trị bằng thuốc trước khi cân nhắc can thiệp")],
           "6.":[(5,"theo dõi Barrett thực quản sau khi điều trị trào ngược")]}),
]
BY_N = {a["n"]: a for a in ARTICLES}

# Hình minh họa: số bài -> {đầu mục: (tệp, alt, chú thích)}
FIGS = {
  1: {"1.": ("gerd-co-che-trao-nguoc-da-day-thuc-quan.svg", "Sơ đồ thực quản, cơ thắt thực quản dưới và dạ dày, dịch acid trào ngược lên thực quản", "Khi cơ thắt thực quản dưới hở hoặc yếu, dịch dạ dày trào ngược lên thực quản."),
      "3.": ("gerd-va-viem-loet-da-day-vi-tri-trieu-chung.svg", "Vị trí khó chịu thường gặp: GERD nóng rát sau xương ức, viêm loét dạ dày – tá tràng đau vùng thượng vị", "Vị trí khó chịu chỉ mang tính gợi ý; hai bệnh có thể chồng lấp.")},
  2: {"1.": ("nguyen-tac-an-uong-nguoi-bi-trao-nguoc.svg", "Bốn nguyên tắc ăn uống: ăn vừa đủ, ăn chậm, ăn tối sớm, ghi nhật ký ăn uống", "Bốn nguyên tắc ăn uống đơn giản cho người bị trào ngược."),
      "4.": ("an-toi-som-ke-cao-dau-giuong-giam-trao-nguoc.svg", "Ăn tối xong ít nhất 2–3 giờ mới đi ngủ và kê cao phần đầu giường", "Ăn tối sớm và kê cao đầu giường giúp giảm trào ngược về đêm.")},
  3: {"1.": ("thoi-diem-uong-thuoc-ppi-truoc-bua-an.svg", "Uống PPI thông thường trước bữa ăn 30–60 phút", "Với đa số PPI dạng thông thường: uống trước bữa ăn 30–60 phút."),
      "2.": ("cac-nhom-thuoc-dieu-tri-gerd.svg", "Bốn nhóm thuốc: PPI, kháng thụ thể H2, alginate và thuốc kháng acid", "Các nhóm thuốc thường dùng trong GERD và tác dụng chính.")},
  4: {"2.": ("nguyen-nhan-uong-thuoc-trao-nguoc-khong-khoi.svg", "Sáu nguyên nhân thường gặp khiến uống thuốc trào ngược chưa đỡ", "Những lý do thường gặp khi điều trị chưa hiệu quả."),
      "3.": ("quy-trinh-danh-gia-gerd-khang-tri.svg", "Sơ đồ các bước đánh giá khi uống thuốc trào ngược vẫn chưa đỡ", "Các bước bác sĩ thường đi qua trước khi kết luận GERD kháng trị.")},
  5: {"1.": ("barrett-thuc-quan-bien-doi-niem-mac.svg", "So sánh niêm mạc thực quản bình thường (biểu mô lát) và Barrett (biểu mô trụ chuyển sản ruột)", "Barrett: niêm mạc lát bình thường được thay bằng biểu mô trụ."),
      "4.": ("barrett-thuc-quan-cac-muc-do-loan-san.svg", "Các mức kết quả sinh thiết Barrett từ không loạn sản đến ung thư và hướng xử trí", "Nguy cơ tăng theo mức độ loạn sản; đa số không tiến triển thành ung thư.")},
  6: {"3.": ("danh-gia-truoc-phau-thuat-chong-trao-nguoc.svg", "Bốn bước đánh giá trước phẫu thuật: nội soi, đo pH – trở kháng, đo áp lực thực quản, chụp cản quang", "Các thăm dò thường cần trước khi quyết định phẫu thuật."),
      "4.": ("phau-thuat-nissen-va-toupet-chong-trao-nguoc.svg", "Mặt cắt minh họa quấn đáy vị Nissen 360 độ và Toupet khoảng 270 độ quanh thực quản", "Nissen quấn toàn bộ 360°, Toupet quấn bán phần khoảng 270°.")},
}


def figure(a, title):
    for key, (f, alt, cap) in FIGS.get(a["n"], {}).items():
        if title.startswith(key):
            return (f'<figure class="fig"><a href="../../assets/img/gerd/{f}" target="_blank" rel="noopener" title="Bấm để xem hình lớn">'
                    f'<img src="../../assets/img/gerd/{f}" alt="{E(alt)}" loading="lazy" width="600" height="400"></a>'
                    f'<figcaption>{E(cap)} <span class="zoom">Bấm vào hình để xem lớn hơn.</span></figcaption></figure>')
    return ""


LOGO_SVG = '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 11.5 12 4l9 7.5"/><path d="M5.5 10v9.5h13V10"/><path d="M12 11.5v5M9.5 14h5"/></svg>'
E = html.escape


def slugify(t):
    t = unicodedata.normalize("NFD", t.replace("đ", "d").replace("Đ", "D"))
    t = "".join(c for c in t if unicodedata.category(c) != "Mn").lower()
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")


def link(n, text):
    return f'<a href="../{BY_N[n]["slug"]}/">{E(text)}</a>'


def parse(a):
    raw = subprocess.run(["pandoc", "-t", "html", "--wrap=none", str(SRC / a["file"])],
                         capture_output=True, text=True, check=True).stdout
    soup = BeautifulSoup(raw, "html.parser")
    first_h = soup.find("h1")
    pre = [el for el in first_h.find_all_previous() if el.parent is soup]
    subtitle = next((p.get_text(" ", strip=True) for p in pre if p.name == "p" and p.find("em")), "")
    th = soup.find("th")
    audience = th.get_text(" ", strip=True) if th else ""
    for el in pre:
        el.decompose()
    note = ""
    for p in soup.find_all("p"):
        txt = p.get_text(" ", strip=True)
        if txt.startswith("FAMILY DOCTOR"):
            p.decompose()
        elif txt.startswith("Lưu ý y khoa"):
            note = re.sub(r"^Lưu ý y khoa:\s*", "", txt)
            p.decompose()

    # Paragraphs made of "•" or "1." lines separated by <br> become real lists
    for p in soup.find_all("p"):
        parts, cur = [], []
        for node in list(p.contents):
            if getattr(node, "name", None) == "br":
                parts.append(cur); cur = []
            else:
                cur.append(node)
        parts.append(cur)
        texts = ["".join(str(x) for x in part).strip() for part in parts]
        bullets = [t for t in texts if t.startswith("•")]
        numbered = [t for t in texts if re.match(r"^\d+\\?\.\s", t)]
        if len(bullets) >= 2 or len(numbered) >= 2:
            intro = [t for t in texts if not (t.startswith("•") or re.match(r"^\d+\\?\.\s", t))]
            tag = "ol" if numbered and not bullets else "ul"
            items = bullets or numbered
            new = ""
            if intro:
                new += "<p>" + " ".join(intro) + "</p>"
            new += f'<{tag} class="list">' + "".join(
                "<li>" + re.sub(r"^(•\s*|\d+\\?\.\s*)", "", t) + "</li>" for t in items) + f"</{tag}>"
            p.replace_with(BeautifulSoup(new, "html.parser"))
    for ul in soup.find_all(["ul", "ol"]):
        ul["class"] = "list"
    # "A. Nissen ..." style sub-headings
    for p in soup.find_all("p"):
        if re.match(r"^[A-E]\.\s", p.get_text(strip=True)) and len(p.get_text()) < 90:
            p.name = "h3"

    # Group into sections by the Word heading-1s
    sections = []
    for h in soup.find_all("h1"):
        title = h.get_text(" ", strip=True)
        body = []
        sib = h.next_sibling
        while sib is not None and getattr(sib, "name", None) != "h1":
            if not (isinstance(sib, NavigableString) and not sib.strip()):
                body.append(str(sib))
            sib = sib.next_sibling
        sections.append(dict(title=title, body="".join(body)))
    return subtitle, audience, note, sections


def head(a, canonical, title, desc, extra=""):
    return f'''<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="article">
<meta property="og:locale" content="vi_VN">
<meta property="og:site_name" content="Family Doctor">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(desc)}">
<meta property="og:url" content="{canonical}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700&family=Lora:wght@500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{a}assets/style.css">
{extra}</head>
<body>

<div class="topbar"><div class="wrap">
  <span>Cấp cứu: gọi <strong>115</strong> nếu khó thở, đau ngực, yếu liệt hoặc lơ mơ</span>
  <span>Hỏi bác sĩ qua Zalo: <a href="https://zalo.me/0935498866" style="color:#fff;font-weight:600">0935 498 866</a></span>
</div></div>

<header class="site">
  <div class="wrap">
    <a class="logo" href="{a}#trang-chu" aria-label="Family Doctor – Trang chủ">
      <span class="logo-mark" aria-hidden="true">{LOGO_SVG}</span>
      <span><b>FAMILY DOCTOR</b><small>Bác sĩ gia đình</small></span>
    </a>
    <button class="menu-btn" id="menuBtn" aria-expanded="false" aria-controls="mainNav">Menu</button>
    <nav class="main" id="mainNav" aria-label="Điều hướng chính">
      <a href="{a}#trang-chu">Trang chủ</a>
      <a href="{a}#benh-thuong-gap" aria-current="page">Bệnh thường gặp</a>
      <a href="{a}#trieu-chung">Triệu chứng</a>
      <a href="{a}#phong-benh">Phòng bệnh</a>
      <a href="{a}#suc-khoe-theo-tuoi">Sức khỏe theo tuổi</a>
      <a href="{a}#benh-man-tinh">Bệnh mạn tính</a>
      <a href="{a}#dinh-duong">Dinh dưỡng &amp; lối sống</a>
      <a href="{a}#hoi-bac-si">Hỏi bác sĩ</a>
    </nav>
  </div>
</header>
'''


def foot(a):
    return f'''
<div class="disclaimer"><div class="wrap">Thông tin trên Family Doctor chỉ nhằm mục đích tham khảo, không thay thế chẩn đoán và điều trị của bác sĩ.</div></div>
<footer>
  <div class="wrap foot-grid">
    <div>
      <a class="logo" href="{a}#trang-chu"><span class="logo-mark" aria-hidden="true">{LOGO_SVG}</span><span><b>FAMILY DOCTOR</b><small>Chăm sóc sức khỏe, bắt đầu từ gia đình.</small></span></a>
      <p class="muted" style="margin-top:12px;max-width:44ch">Thông tin y khoa dễ hiểu, có cơ sở khoa học và hướng đến lợi ích người bệnh.</p>
      <p style="margin-top:10px">BS. Thái Hoàng · Zalo <a href="https://zalo.me/0935498866">0935 498 866</a></p>
    </div>
    <div><h4>Tra cứu</h4><ul>
      <li><a href="{a}#benh-thuong-gap">Bệnh thường gặp</a></li><li><a href="{a}kien-thuc-tieu-hoa/">Chuyên đề trào ngược (GERD)</a></li><li><a href="{a}#trieu-chung">Triệu chứng</a></li><li><a href="{a}#benh-man-tinh">Bệnh mạn tính</a></li></ul></div>
    <div><h4>Sống khỏe</h4><ul>
      <li><a href="{a}#phong-benh">Phòng bệnh</a></li><li><a href="{a}#suc-khoe-theo-tuoi">Sức khỏe theo tuổi</a></li><li><a href="{a}#dinh-duong">Dinh dưỡng &amp; lối sống</a></li><li><a href="{a}#hoi-bac-si">Hỏi bác sĩ</a></li></ul></div>
  </div>
</footer>

<script>
document.getElementById("menuBtn").addEventListener("click",function(){{
  var o=document.getElementById("mainNav").classList.toggle("open");
  this.setAttribute("aria-expanded",String(o));
}});
</script>
</body>
</html>
'''


def fmt_date(d):
    y, m, dd = d.split("-")
    return f"{dd}/{m}/{y}"


def build_article(a):
    subtitle, audience, note, sections = parse(a)
    url = f"{SITE}/kien-thuc-tieu-hoa/{a['slug']}/"
    toc, body = [], []
    refs = None
    for s in sections:
        t = s["title"]
        if t.startswith("Tài liệu tham khảo"):
            refs = s
            continue
        sid = slugify(re.sub(r"^\d+\.\s*", "", t))
        extra = ""
        for key, targets in a["links"].items():
            if t.startswith(key):
                extra += '<p class="see-also">Đọc thêm: ' + " · ".join(link(n, txt) for n, txt in targets) + "</p>"
        cls = ' class="key-message"' if t.startswith("Thông điệp") else ""
        fig = figure(a, t)
        sbody = s["body"]
        if fig:
            i = sbody.find("</p>")
            sbody = sbody[:i + 4] + fig + sbody[i + 4:] if i >= 0 else fig + sbody
        if t != "Mở đầu":
            toc.append(f'<li><a href="#{sid}">{E(t)}</a></li>')
            body.append(f'<section{cls}><h2 id="{sid}">{E(t)}</h2>{sbody}{extra}</section>')
        else:
            body.append(f'<section>{s["body"]}{extra}</section>')
    toc.append('<li><a href="#hoi-dap">Câu hỏi thường gặp</a></li>')
    faq_html = "".join(f"<details><summary>{E(q)}</summary><p>{E(ans)}</p></details>" for q, ans in a["faq"])
    body.append(f'<section class="faq"><h2 id="hoi-dap">Câu hỏi thường gặp</h2>{faq_html}</section>')
    if refs:
        body.append(f'<section class="refs-block"><h2 id="tai-lieu-tham-khao">Tài liệu tham khảo</h2><div class="refs">{refs["body"]}</div>'
                    f'<p class="refs"><b>Lưu ý y khoa:</b> {E(note)}</p></section>')

    nxt = BY_N.get(a["n"] + 1)
    prv = BY_N.get(a["n"] - 1)
    pager = '<nav class="pager" aria-label="Bài trong chuyên đề">'
    pager += (f'<a href="../{prv["slug"]}/"><small>← Bài {prv["n"]}</small>{E(prv["short"])}</a>' if prv else "<span></span>")
    pager += (f'<a class="next" href="../{nxt["slug"]}/"><small>Bài {nxt["n"]} →</small>{E(nxt["short"])}</a>' if nxt else "<span></span>")
    pager += "</nav>"

    series = "".join(
        (f'<li aria-current="page"><b>{x["n"]}. {E(x["short"])}</b><span class="soon">Bạn đang đọc</span></li>' if x is a
         else f'<li><a href="../{x["slug"]}/">{x["n"]}. {E(x["short"])}</a></li>') for x in ARTICLES)

    schema = {"@context": "https://schema.org", "@type": "MedicalWebPage", "headline": a["h1"],
              "description": a["desc"], "url": url, "inLanguage": "vi",
              "datePublished": PUBLISHED, "dateModified": MODIFIED,
              "author": {"@type": "Person", "name": AUTHOR},
              "publisher": {"@type": "Organization", "name": "Family Doctor", "url": SITE + "/"},
              "isPartOf": {"@type": "CollectionPage", "name": "Chuyên đề trào ngược dạ dày – thực quản (GERD)", "url": SITE + "/kien-thuc-tieu-hoa/"}}
    faq_schema = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": ans}} for q, ans in a["faq"]]}
    ld = ('<script type="application/ld+json">\n' + json.dumps(schema, ensure_ascii=False, indent=1) + "\n</script>\n"
          '<script type="application/ld+json">\n' + json.dumps(faq_schema, ensure_ascii=False, indent=1) + "\n</script>\n")

    meta_line = f"Tác giả: {AUTHOR} · Đăng ngày: {fmt_date(PUBLISHED)} · Cập nhật: {fmt_date(MODIFIED)}"
    aud = " · ".join(x.strip() for x in audience.split("|")) if audience else ""
    page = head("../../", url, a["seo"] + " | Family Doctor", a["desc"], ld)
    page += f'''
<main>
<div class="wrap">
  <div class="page-head">
    <div class="crumb"><a href="../../#trang-chu">Trang chủ</a> / <a href="../">Chuyên đề GERD</a> / Bài {a["n"]}</div>
    <span class="eyebrow">Tiêu hóa · Chuyên đề GERD · Bài {a["n"]}</span>
    <h1>{E(a["h1"])}</h1>
    <p>{E(subtitle)}</p>
    <p class="meta" style="margin-top:12px">{E(aud)}</p>
    <p class="meta">{E(meta_line)}</p>
  </div>

  <div class="article-grid">
    <article class="article stack">
      <nav class="toc" aria-label="Mục lục"><h2>Nội dung bài viết</h2><ol>{"".join(toc)}</ol></nav>
      {"".join(body)}
      {pager}
    </article>

    <aside class="stack">
      <div class="panel stack">
        <h3>Chuyên đề trào ngược dạ dày – thực quản</h3>
        <ol class="series">{series}</ol>
        <a href="../">Xem tổng quan chuyên đề →</a>
      </div>
      <div class="panel stack"><h3>Chưa chắc có phải bệnh này?</h3><p class="muted">Chọn các dấu hiệu đang gặp để xem những bệnh có thể liên quan.</p><a class="btn" href="../../#trieu-chung">Tra triệu chứng</a></div>
      <div class="panel stack"><h3>Còn thắc mắc?</h3><p class="muted">Nhắn BS. Thái Hoàng qua Zalo: <b>0935 498 866</b>.</p><a class="btn ghost" href="https://zalo.me/0935498866" target="_blank" rel="noopener">Nhắn Zalo</a></div>
    </aside>
  </div>
</div>
</main>
'''
    page += foot("../../")
    d = OUT / a["slug"]
    d.mkdir(parents=True, exist_ok=True)
    (d / "index.html").write_text(page, encoding="utf-8")


def build_hub():
    url = f"{SITE}/kien-thuc-tieu-hoa/"
    desc = "Chuyên đề 6 bài về bệnh trào ngược dạ dày – thực quản (GERD): nhận biết, chế độ ăn, thuốc điều trị, GERD kháng trị, Barrett thực quản và phẫu thuật."
    cards = "".join(
        f'<a class="card" href="{x["slug"]}/"><span class="tag">Bài {x["n"]}</span><h3>{E(x["h1"])}</h3><p>{E(x["desc"])}</p><span class="more">Đọc bài →</span></a>'
        for x in ARTICLES)
    page = head("../", url, "Trào ngược dạ dày – thực quản (GERD): Chuyên đề 6 bài | Family Doctor", desc)
    page += f'''
<main>
<div class="wrap">
  <div class="page-head">
    <div class="crumb"><a href="../#trang-chu">Trang chủ</a> / <a href="../#benh-thuong-gap">Bệnh thường gặp</a> / Chuyên đề GERD</div>
    <span class="eyebrow">Tiêu hóa · Chuyên đề</span>
    <h1>Trào ngược dạ dày – thực quản (GERD)</h1>
    <p>Sáu bài viết đi từ nhận biết bệnh, ăn uống, dùng thuốc đúng cách, đến khi nào triệu chứng đáng lo và khi nào cần can thiệp. Nên đọc theo thứ tự, bắt đầu từ Bài 1.</p>
  </div>
  <div class="grid">{cards}</div>
</div>
</main>
'''
    page += foot("../")
    (OUT / "index.html").write_text(page, encoding="utf-8")


if __name__ == "__main__":
    for a in ARTICLES:
        build_article(a)
    build_hub()
    print("Đã tạo", len(ARTICLES), "bài và trang chuyên đề trong", OUT)
