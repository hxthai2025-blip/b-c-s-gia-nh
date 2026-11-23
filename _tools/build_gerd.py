#!/usr/bin/env python3
"""Tạo 6 trang chuyên đề GERD từ các file Word trong _tools/gerd/.

Chạy từ thư mục gốc của repo:  python3 _tools/build_gerd.py
Cần có pandoc và BeautifulSoup (bs4).
Thư mục bắt đầu bằng "_" không được GitHub Pages đăng lên web.
"""
import html, json, re, subprocess, unicodedata
from pathlib import Path
from bs4 import BeautifulSoup, NavigableString
import layout as L

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

# Hình minh họa: số bài -> danh sách (đầu mục, tệp, alt, chú thích, nguồn ảnh hoặc None)
CC4 = "https://creativecommons.org/licenses/by-sa/4.0"
CC3 = "https://creativecommons.org/licenses/by-sa/3.0"
WM = "https://commons.wikimedia.org/wiki/File:"
CREDIT_GERD = ("BruceBlaus", "CC BY-SA 4.0", CC4, WM + "GastroEsophageal_Reflux_Disease_(GERD).jpg", "đã thêm chú thích tiếng Việt")
CREDIT_HERNIA = ("BruceBlaus", "CC BY-SA 4.0", CC4, WM + "Hiatal_Hernia.png", "đã thay chú thích bằng tiếng Việt")
CREDIT_NISSEN = ("Dana Hamers", "CC BY-SA 3.0", CC3, WM + "Doorsnede-Nissen_wiki.jpg", "")
CREDIT_BARRETT = ("Samir", "dùng tự do theo giấy phép của tác giả", None, WM + "Barretts_esophagus.jpg", "")
CREDIT_STRICTURE = ("Samir", "phạm vi công cộng", None, WM + "Peptic_stricture.png", "")

FIGS = {
  1: [("1.", "gerd-giai-phau-trao-nguoc-co-nhan.jpg", "Hình giải phẫu so sánh dạ dày bình thường và dạ dày bị trào ngược GERD, dịch dạ dày trào lên thực quản", "Bình thường, cơ thắt thực quản dưới đóng kín. Ở người bị GERD, cơ thắt hở và dịch dạ dày trào lên thực quản.", CREDIT_GERD),
      ("3.", "gerd-va-viem-loet-da-day-vi-tri-trieu-chung.svg", "Vị trí khó chịu thường gặp: GERD nóng rát sau xương ức, viêm loét dạ dày – tá tràng đau vùng thượng vị", "Vị trí khó chịu chỉ mang tính gợi ý; hai bệnh có thể chồng lấp.", None)],
  2: [("1.", "nguyen-tac-an-uong-nguoi-bi-trao-nguoc.svg", "Bốn nguyên tắc ăn uống: ăn vừa đủ, ăn chậm, ăn tối sớm, ghi nhật ký ăn uống", "Bốn nguyên tắc ăn uống đơn giản cho người bị trào ngược.", None),
      ("4.", "an-toi-som-ke-cao-dau-giuong-giam-trao-nguoc.svg", "Ăn tối xong ít nhất 2–3 giờ mới đi ngủ và kê cao phần đầu giường", "Ăn tối sớm và kê cao đầu giường giúp giảm trào ngược về đêm.", None)],
  3: [("1.", "thoi-diem-uong-thuoc-ppi-truoc-bua-an.svg", "Uống PPI thông thường trước bữa ăn 30–60 phút", "Với đa số PPI dạng thông thường: uống trước bữa ăn 30–60 phút.", None),
      ("2.", "cac-nhom-thuoc-dieu-tri-gerd.svg", "Bốn nhóm thuốc: PPI, kháng thụ thể H2, alginate và thuốc kháng acid", "Các nhóm thuốc thường dùng trong GERD và tác dụng chính.", None)],
  4: [("2.", "nguyen-nhan-uong-thuoc-trao-nguoc-khong-khoi.svg", "Sáu nguyên nhân thường gặp khiến uống thuốc trào ngược chưa đỡ", "Những lý do thường gặp khi điều trị chưa hiệu quả.", None),
      ("3.", "quy-trinh-danh-gia-gerd-khang-tri.svg", "Sơ đồ các bước đánh giá khi uống thuốc trào ngược vẫn chưa đỡ", "Các bước bác sĩ thường đi qua trước khi kết luận GERD kháng trị.", None),
      ("3.", "hep-thuc-quan-do-trao-nguoc-anh-noi-soi.jpg", "Ảnh nội soi thực quản bị hẹp do trào ngược kéo dài", "Ví dụ hình ảnh nội soi: thực quản bị hẹp do trào ngược acid kéo dài.", CREDIT_STRICTURE)],
  5: [("1.", "barrett-thuc-quan-anh-noi-soi.jpg", "Ảnh nội soi đoạn cuối thực quản của người bị Barrett thực quản", "Ví dụ hình ảnh nội soi đoạn cuối thực quản ở người bị Barrett.", CREDIT_BARRETT),
      ("4.", "barrett-thuc-quan-cac-muc-do-loan-san.svg", "Các mức kết quả sinh thiết Barrett từ không loạn sản đến ung thư và hướng xử trí", "Nguy cơ tăng theo mức độ loạn sản; đa số không tiến triển thành ung thư.", None)],
  6: [("2.", "thoat-vi-khe-hoanh-co-nhan.jpg", "Hình giải phẫu so sánh dạ dày bình thường và thoát vị khe hoành, một phần dạ dày trồi lên qua cơ hoành", "Thoát vị khe hoành: một phần dạ dày trồi lên khỏi cơ hoành, thường làm trào ngược nặng hơn.", CREDIT_HERNIA),
      ("3.", "danh-gia-truoc-phau-thuat-chong-trao-nguoc.svg", "Bốn bước đánh giá trước phẫu thuật: nội soi, đo pH – trở kháng, đo áp lực thực quản, chụp cản quang", "Các thăm dò thường cần trước khi quyết định phẫu thuật.", None),
      ("4.", "phau-thuat-nissen-mat-cat-minh-hoa.jpg", "Hình minh họa mặt cắt phẫu thuật quấn đáy vị Nissen quanh thực quản với các mũi khâu", "Mặt cắt minh họa van quấn đáy vị Nissen quanh đoạn cuối thực quản.", CREDIT_NISSEN),
      ("4.", "phau-thuat-nissen-va-toupet-chong-trao-nguoc.svg", "Mặt cắt minh họa quấn đáy vị Nissen 360 độ và Toupet khoảng 270 độ quanh thực quản", "Nissen quấn toàn bộ 360°, Toupet quấn bán phần khoảng 270°.", None)],
}

IMG_DIR = ROOT / "assets" / "img" / "gerd"


def _size(f):
    if f.endswith(".svg"):
        m = re.search(r'viewBox="0 0 (\d+) (\d+)"', (IMG_DIR / f).read_text(encoding="utf-8"))
        return (int(m.group(1)), int(m.group(2))) if m else (600, 400)
    from PIL import Image
    with Image.open(IMG_DIR / f) as im:
        return im.size


def credit_html(cred):
    if not cred:
        return ""
    who, lic, lic_url, page, note = cred
    lic_html = f'<a href="{lic_url}" target="_blank" rel="noopener">{E(lic)}</a>' if lic_url else E(lic)
    return (f'Nguồn hình: {E(who)} · {lic_html} · <a href="{page}" target="_blank" rel="noopener">Wikimedia Commons</a>'
            + (f" ({E(note)})" if note else ""))


def webp_of(rel):
    """Trả về đường dẫn .webp nếu đã tạo (build_all tạo từ ảnh JPG/PNG)."""
    if rel.endswith((".jpg", ".png")):
        w = rel.rsplit(".", 1)[0] + ".webp"
        if (ROOT / w).exists():
            return w
    return None


def inline_fig(a_prefix, rel, alt, cap, credit, w, h):
    """Hình minh họa trong thân bài: lazy, có width/height, WebP nếu có, bấm để phóng to."""
    img = f'<img src="{a_prefix}{rel}" alt="{E(alt)}" loading="lazy" decoding="async" width="{w}" height="{h}">'
    wp = webp_of(rel)
    if wp:
        img = f'<picture><source type="image/webp" srcset="{a_prefix}{wp}">{img}</picture>'
    cr = f'<span class="credit">{credit}</span>' if credit else ""
    return (f'<figure class="fig"><a href="{a_prefix}{rel}" target="_blank" rel="noopener" title="Bấm để xem hình lớn">{img}</a>'
            f'<figcaption>{E(cap)} <span class="zoom">Bấm vào hình để xem lớn hơn.</span>{cr}</figcaption></figure>')


def featured_of(a):
    """Ảnh đại diện = hình đầu tiên của bài (không lặp lại trong thân bài)."""
    figs = FIGS.get(a["n"], [])
    if not figs:
        return None
    key, f, alt, cap, cred = figs[0]
    rel = f"assets/img/gerd/{f}"
    w, h = _size(f)
    return dict(src=rel, alt=alt, w=w, h=h, webp=webp_of(rel), caption=E(cap), credit=credit_html(cred))


def figure(a, title):
    out = ""
    for i, (key, f, alt, cap, cred) in enumerate(FIGS.get(a["n"], [])):
        if i == 0 or not title.startswith(key):
            continue
        w, h = _size(f)
        out += inline_fig("../../", f"assets/img/gerd/{f}", alt, cap, credit_html(cred), w, h)
    return out


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


READ_TIME = {1: "6–8 phút", 2: "6–8 phút", 3: "7–9 phút", 4: "7–9 phút", 5: "7–9 phút", 6: "8–10 phút"}
SERIES_NAME = "Trào ngược dạ dày – thực quản (GERD)"


def related_of(a, arts, tag, n=3):
    """Bài liên quan trong cùng chuyên đề: các bài kế tiếp (vòng tròn)."""
    i = arts.index(a)
    pick = [arts[(i + k) % len(arts)] for k in range(1, n + 1)]
    return [dict(url=f'../{x["slug"]}/', title=x["h1"], desc=x["desc"], tag=f"{tag} · Bài {x['n']}") for x in pick]


def pager_of(a, by_n):
    nxt, prv = by_n.get(a["n"] + 1), by_n.get(a["n"] - 1)
    p = '<nav class="pager" aria-label="Bài trong chuyên đề">'
    p += (f'<a href="../{prv["slug"]}/"><small>← Bài {prv["n"]}</small>{E(prv["short"])}</a>' if prv else "<span></span>")
    p += (f'<a class="next" href="../{nxt["slug"]}/"><small>Bài {nxt["n"]} →</small>{E(nxt["short"])}</a>' if nxt else "<span></span>")
    return p + "</nav>"


def series_items(a, arts):
    return "".join(
        (f'<li aria-current="page"><b>{x["n"]}. {E(x["short"])}</b><span class="soon">Bạn đang đọc</span></li>' if x is a
         else f'<li><a href="../{x["slug"]}/">{x["n"]}. {E(x["short"])}</a></li>') for x in arts)


def schema_of(a, url, featured, published, modified, series_name, crumbs_abs, faq):
    img = (SITE + "/" + featured["src"]) if featured and not featured["src"].endswith(".svg") else f"{SITE}/{L.OG_DEFAULT}"
    page = {"@context": "https://schema.org", "@type": "MedicalWebPage", "headline": a["h1"], "description": a["desc"],
            "url": url, "mainEntityOfPage": url, "inLanguage": "vi", "image": img,
            "datePublished": published, "dateModified": modified,
            "author": {"@type": "Person", "name": L.AUTHOR["name"], "jobTitle": "Bác sĩ " + L.AUTHOR["dept"],
                       "worksFor": {"@type": "Hospital", "name": L.AUTHOR["org"]}},
            "publisher": {"@type": "Organization", "name": L.BRAND, "url": SITE + "/", "logo": {"@type": "ImageObject", "url": SITE + "/assets/logo-512.png"}},
            "isPartOf": {"@type": "CollectionPage", "name": series_name, "url": SITE + "/kien-thuc-tieu-hoa/"}}
    if L.REVIEWER:
        page["reviewedBy"] = {"@type": "Person", "name": L.REVIEWER["name"]}
    out = [page, L.ld_breadcrumb(crumbs_abs)]
    if faq:
        out.append({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": ans}} for q, ans in faq]})
    return out, img


def build_article(a):
    subtitle, audience, note, sections = parse(a)
    url = f"{SITE}/kien-thuc-tieu-hoa/{a['slug']}/"
    toc, body, refs, summary = [], [], [], []
    for s in sections:
        t = s["title"]
        if t.startswith("Tài liệu tham khảo"):
            refs = [str(li.decode_contents()) for li in BeautifulSoup(s["body"], "html.parser").find_all("li")]
            continue
        if t.startswith("Thông điệp"):
            txt = BeautifulSoup(s["body"], "html.parser").get_text(" ", strip=True)
            summary = [E(x.strip().rstrip(".")) + "." for x in re.split(r"(?<=\.)\s+", txt) if x.strip()]
            continue
        sid = slugify(re.sub(r"^\d+\.\s*", "", t))
        extra = ""
        for key, targets in a["links"].items():
            if t.startswith(key):
                extra += '<p class="see-also">Đọc thêm: ' + " · ".join(link(n, txt) for n, txt in targets) + "</p>"
        fig = figure(a, t)
        sbody = s["body"]
        if fig:
            i = sbody.find("</p>")
            sbody = sbody[:i + 4] + fig + sbody[i + 4:] if i >= 0 else fig + sbody
        if t != "Mở đầu":
            toc.append((sid, t))
            body.append(f'<section><h2 id="{sid}">{E(t)}</h2>{sbody}{extra}</section>')
        else:
            body.append(f'<section>{sbody}{extra}</section>')
    toc += [("hoi-dap", "Câu hỏi thường gặp"), ("tai-lieu-tham-khao", "Tài liệu tham khảo")]
    featured = featured_of(a)
    crumbs = [("Trang chủ", "../../"), ("Kiến thức tiêu hóa", "../"), ("GERD", "../#gerd"), (a["short"], None)]
    crumbs_abs = [("Trang chủ", SITE + "/"), ("Kiến thức tiêu hóa", SITE + "/kien-thuc-tieu-hoa/"), (a["h1"], url)]
    ld, og = schema_of(a, url, featured, PUBLISHED, MODIFIED, "Chuyên đề " + SERIES_NAME, crumbs_abs, a["faq"])
    page = L.article_page("../../", url=url, seo_title=a["seo"] + " | Family Doctor", desc=a["desc"], crumbs=crumbs,
                          category=("Tiêu hóa · GERD", "../#gerd"), h1=a["h1"], sapo=subtitle,
                          published=PUBLISHED, modified=MODIFIED, read_time=READ_TIME[a["n"]] + " đọc",
                          featured=featured, summary=summary, toc=toc, sections_html="".join(body), faq=a["faq"],
                          refs=refs, related=related_of(a, ARTICLES, "GERD"), series_title="Chuyên đề " + SERIES_NAME,
                          series_items=series_items(a, ARTICLES), pager=pager_of(a, BY_N), ld=ld, og_image=og)
    d = OUT / a["slug"]
    d.mkdir(parents=True, exist_ok=True)
    (d / "index.html").write_text(page, encoding="utf-8")
