"""Khung dùng chung: đầu trang, chân trang, biểu tượng.

`a` là tiền tố đường dẫn tới thư mục gốc của site: "" cho trang chủ, "../../" cho các bài viết, "../" cho trang tổng quan.
"""

FONT_LINK = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
             '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
             '<link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700&display=swap" rel="stylesheet">')

ZALO = "https://zalo.me/0935498866"


def ic(a, name, cls=""):
    return f'<svg class="i {cls}" aria-hidden="true"><use href="{a}assets/icons.svg#{name}"/></svg>'


def logo(a, href=None):
    href = href or f"{a}#trang-chu"
    return (f'<a class="logo" href="{href}" aria-label="Family Doctor – Trang chủ">'
            f'<span class="logo-mark" aria-hidden="true">{ic(a, "heart-pulse")}</span>'
            f'<span><b>Family Doctor</b><small>Kiến thức sức khỏe đáng tin cậy</small></span></a>')


def _sub(a, icon, color, title, desc, href):
    return (f'<a href="{href}"><span class="ib" style="--c:{color}">{ic(a, icon)}</span>'
            f'<span><b>{title}</b><small>{desc}</small></span></a>')


def header(a="", current=None):
    """current: 'chuyen-de' để tô sáng mục Chuyên đề (dùng cho trang bài viết)."""
    cur = " cur" if current == "chuyen-de" else ""
    chuyen_de = "".join([
        _sub(a, "stomach", "#0b7a75", "Kiến thức tiêu hóa", "Tổng quan các chuyên đề", f"{a}kien-thuc-tieu-hoa/"),
        _sub(a, "droplet", "#c2410c", "Trào ngược dạ dày (GERD)", "6 bài: từ nhận biết đến điều trị", f"{a}kien-thuc-tieu-hoa/#gerd"),
        _sub(a, "heart-pulse", "#be185d", "Bệnh trĩ", "7 bài: dấu hiệu, phân độ, điều trị", f"{a}kien-thuc-tieu-hoa/#tri"),
    ])
    song_khoe = "".join([
        _sub(a, "shield-check", "#0b7a75", "Phòng bệnh", "Lịch khám, tầm soát, tiêm chủng", f"{a}#phong-benh"),
        _sub(a, "users", "#1b6fb3", "Sức khỏe theo tuổi", "Chăm sóc từng giai đoạn", f"{a}#suc-khoe-theo-tuoi"),
        _sub(a, "activity", "#7c3aed", "Bệnh mạn tính", "Sống chung và kiểm soát", f"{a}#benh-man-tinh"),
        _sub(a, "apple", "#4d7c0f", "Dinh dưỡng & lối sống", "Ăn, ngủ, vận động", f"{a}#dinh-duong"),
    ])
    return f'''<div class="topbar"><div class="wrap">
  <span class="em"><b>115</b> Cấp cứu ngay nếu khó thở, đau ngực, yếu liệt hoặc lơ mơ</span>
  <span class="hot">{ic(a, "phone")} Hỏi bác sĩ qua Zalo: <a href="{ZALO}">0935 498 866</a></span>
</div></div>

<header class="site">
  <div class="wrap">
    {logo(a)}
    <button class="menu-btn" id="menuBtn" aria-expanded="false" aria-controls="mainNav">{ic(a, "menu")} Menu</button>
    <nav class="main" id="mainNav" aria-label="Điều hướng chính">
      <a href="{a}#trang-chu">Trang chủ</a>
      <a href="{a}#benh-thuong-gap">Bệnh thường gặp</a>
      <a href="{a}#trieu-chung">Triệu chứng</a>
      <div class="has-sub{cur}"><button type="button" aria-haspopup="true">Chuyên đề {ic(a, "chevron-down")}</button><div class="sub-menu">{chuyen_de}</div></div>
      <div class="has-sub"><button type="button" aria-haspopup="true">Sống khỏe {ic(a, "chevron-down")}</button><div class="sub-menu">{song_khoe}</div></div>
      <span class="nav-cta"><a class="btn sm" href="{a}#hoi-bac-si">{ic(a, "message")} Hỏi bác sĩ</a></span>
    </nav>
  </div>
</header>
'''


def footer(a="", progress=False):
    prog = ('<div class="progress" aria-hidden="true"><i id="progressBar"></i></div>\n' if progress else "")
    script = '''<script>
document.getElementById("menuBtn").addEventListener("click",function(){
  var o=document.getElementById("mainNav").classList.toggle("open");
  this.setAttribute("aria-expanded",String(o));
});
(function(){var b=document.getElementById("progressBar");if(!b)return;
  function u(){var h=document.documentElement,s=h.scrollTop||document.body.scrollTop,t=h.scrollHeight-h.clientHeight;b.style.width=(t>0?Math.min(100,s/t*100):0)+"%"}
  addEventListener("scroll",u,{passive:true});u()})();
</script>''' if progress else ""
    return f'''
{prog}<div class="disclaimer"><div class="wrap">{ic(a, "alert-triangle")}<span>Thông tin trên Family Doctor chỉ nhằm mục đích tham khảo, không thay thế chẩn đoán và điều trị của bác sĩ.</span></div></div>
<footer class="site-footer">
  <div class="wrap">
    <div class="foot-main">
      <div>
        {logo(a)}
        <p class="foot-about">Thông tin y khoa dễ hiểu, có cơ sở khoa học và hướng đến lợi ích người bệnh. Chăm sóc sức khỏe, bắt đầu từ gia đình.</p>
        <div class="foot-contact">
          <span>{ic(a, "stethoscope")} BS. Thái Hoàng – bác sĩ phụ trách nội dung</span>
          <span>{ic(a, "message")} Zalo: <a href="{ZALO}">0935 498 866</a></span>
        </div>
      </div>
      <div><h4>Tra cứu</h4><ul>
        <li><a href="{a}#benh-thuong-gap">Bệnh thường gặp</a></li>
        <li><a href="{a}#trieu-chung">Tra cứu triệu chứng</a></li>
        <li><a href="{a}#phong-benh">Phòng bệnh</a></li>
        <li><a href="{a}#suc-khoe-theo-tuoi">Sức khỏe theo tuổi</a></li>
        <li><a href="{a}#benh-man-tinh">Bệnh mạn tính</a></li>
        <li><a href="{a}#dinh-duong">Dinh dưỡng &amp; lối sống</a></li></ul></div>
      <div><h4>Chuyên đề</h4><ul>
        <li><a href="{a}kien-thuc-tieu-hoa/">Kiến thức tiêu hóa</a></li>
        <li><a href="{a}kien-thuc-tieu-hoa/#gerd">Trào ngược dạ dày (GERD)</a></li>
        <li><a href="{a}kien-thuc-tieu-hoa/#tri">Bệnh trĩ</a></li>
        <li><a href="{a}#dinh-duong">Tính chỉ số BMI</a></li>
        <li><a href="{a}#benh-man-tinh">Đọc chỉ số huyết áp</a></li></ul></div>
      <div><h4>Cần hỗ trợ?</h4>
        <div class="foot-em"><b>Cấp cứu: gọi 115</b>Khó thở, đau ngực, yếu liệt, lơ mơ, chảy máu nhiều.</div>
        <ul style="margin-top:14px"><li><a href="{a}#hoi-bac-si">Gửi câu hỏi cho bác sĩ</a></li><li><a href="{ZALO}">Nhắn Zalo trực tiếp</a></li></ul>
      </div>
    </div>
    <div class="foot-bottom"><span>© 2026 Family Doctor · bacsi115.com</span><span>Nội dung giáo dục sức khỏe, không thay thế khám và điều trị.</span></div>
  </div>
</footer>
{script}'''
