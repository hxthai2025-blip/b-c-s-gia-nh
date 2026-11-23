"""Nội dung chuyên đề BỆNH TRĨ (7 bài), soạn theo bộ SEO "Family Doctor – Bộ 7 bài SEO bệnh trĩ 2026".

Mỗi bài: tiêu đề, từ khóa, mô tả, các mục, câu hỏi thường gặp, liên kết nội bộ.
Nội dung giáo dục sức khỏe; cần bác sĩ chuyên khoa rà soát trước khi đăng chính thức.
"""

PUBLISHED = "2026-11-23"
MODIFIED = "2026-11-23"

SAFETY = ("Không tự kết luận chảy máu hậu môn là do trĩ. Đi khám khi chảy máu mới xuất hiện hoặc tái diễn, "
          "hoặc có dấu hiệu báo động; cấp cứu nếu chảy máu nhiều kèm choáng/ngất hoặc đau dữ dội kèm sốt.")

REFS = [
    "Qureshi W, et al. AGA Clinical Practice Update on Diagnosis and Treatment of Hemorrhoids: Expert Review. Clinical Gastroenterology and Hepatology. 2026;24(7):1773–1781. doi:10.1016/j.cgh.2026.04.008.",
    "Hawkins AT, et al. The American Society of Colon and Rectal Surgeons Clinical Practice Guidelines for the Management of Hemorrhoids. Diseases of the Colon & Rectum. 2024;67(5):614–623. doi:10.1097/DCR.0000000000003276.",
    "SIUCP Guidelines for the management of acute and chronic hemorrhoidal disease. Annals of Coloproctology. 2024;40(4):287–320. doi:10.3393/ac.2023.00871.0124.",
]


def ul(items):
    return '<ul class="list">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def ol(items):
    return '<ol class="list">' + "".join(f"<li>{i}</li>" for i in items) + "</ol>"


def table(head, rows):
    h = "".join(f"<th>{c}</th>" for c in head)
    r = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows)
    return f'<div class="table-wrap"><table><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table></div>'


def info(title, text):
    return f'<div class="alert info"><div><b>{title}</b>{text}</div></div>'


def danger(title, items):
    return f'<div class="alert danger"><div><b>{title}</b>{ul(items)}</div></div>'


ARTICLES = [
# ───────────────────────────── BÀI 1 ─────────────────────────────
dict(n=1, summary=['Bệnh trĩ là khi các đệm mạch máu bình thường ở hậu môn phì đại hoặc sa xuống và gây triệu chứng.', 'Dấu hiệu thường gặp: chảy máu đỏ tươi khi đi ngoài, sa búi trĩ, ngứa hoặc khó chịu ở hậu môn.', 'Nền tảng điều trị là chất xơ, đủ nước, không rặn, không ngồi lâu; thủ thuật hoặc phẫu thuật chỉ khi cần.', 'Không tự kết luận mọi trường hợp ra máu là trĩ; đi khám khi chảy máu mới xuất hiện hoặc tái diễn.'], slug="benh-tri-la-gi-nguyen-nhan-trieu-chung-dieu-tri",
  h1="Bệnh trĩ là gì? Nguyên nhân, triệu chứng và cách điều trị",
  short="Bệnh trĩ là gì? Nguyên nhân, triệu chứng và cách điều trị",
  seo="Bệnh trĩ là gì? Nguyên nhân, triệu chứng và cách điều trị",
  desc="Giải thích bệnh trĩ, nguyên nhân, triệu chứng, phân loại và các phương pháp điều trị hiện nay.",
  kw="bệnh trĩ",
  subtitle="Hiểu đúng về bệnh trĩ để nhận biết sớm, chăm sóc đúng cách và biết khi nào cần đến gặp bác sĩ.",
  meta="Người trưởng thành và gia đình · Thời gian đọc: 6–8 phút",
  intro="<p>Đi ngoài ra máu đỏ tươi, ngứa rát hay thấy một khối nhỏ ở hậu môn khiến nhiều người nghĩ ngay đến bệnh trĩ. Trĩ rất thường gặp và đa số trường hợp có thể kiểm soát được. Tuy vậy, <b>không phải mọi trường hợp chảy máu hay có khối ở hậu môn đều là trĩ</b>.</p><p>Bài viết này giải thích bệnh trĩ là gì, vì sao xuất hiện, các dấu hiệu thường gặp và hướng điều trị hiện nay, để bạn biết khi nào có thể tự chăm sóc và khi nào cần đi khám.</p>",
  sections=[
    ("Bệnh trĩ là gì?", "<p>Ở người bình thường, ống hậu môn có những <b>đệm mô mềm</b> chứa mạch máu, cơ trơn và mô liên kết. Các đệm này giúp đóng kín ống hậu môn và góp phần kiểm soát đại tiện. Khi các đệm này bị thay đổi, phì đại hoặc sa xuống, gây ra triệu chứng như chảy máu đỏ tươi, sa búi trĩ, ngứa hoặc khó chịu thì gọi là <b>bệnh trĩ</b>.</p><p>Nói cách khác, đệm hậu môn là cấu trúc bình thường ai cũng có; chỉ khi chúng gây triệu chứng mới là bệnh.</p>", "giai-phau"),
    ("Nguyên nhân và yếu tố nguy cơ", "<p>Bệnh trĩ thường do <b>nhiều yếu tố phối hợp</b>, không có một nguyên nhân đơn độc. Những yếu tố có thể làm tăng nguy cơ hoặc làm nặng thêm triệu chứng gồm:</p>" + ul(["Táo bón, phân cứng, phải rặn nhiều khi đại tiện", "Ngồi lâu trong nhà vệ sinh, kể cả vừa ngồi vừa dùng điện thoại", "Chế độ ăn ít chất xơ, ít uống nước, ít vận động", "Mang thai và sau sinh", "Thừa cân, béo phì", "Tuổi cao, tiêu chảy kéo dài, mang vác vật nặng thường xuyên"]), ""),
    ("Triệu chứng thường gặp", "<p>Chảy máu đỏ tươi khi đại tiện, sa búi trĩ, ngứa và kích ứng quanh hậu môn là những biểu hiện thường gặp.</p>" + ul(["<b>Chảy máu đỏ tươi</b> khi đi ngoài: máu dính trên giấy vệ sinh, nhỏ giọt hoặc phủ ngoài phân", "<b>Sa búi trĩ:</b> có thể tự co lên, hoặc cần dùng tay đẩy hoặc nằm thường xuyên bên ngoài", "Ngứa, ẩm ướt, cảm giác vướng hoặc khó chịu ở hậu môn", "<b>Đau:</b> trĩ nội không biến chứng thường ít đau; trĩ ngoại có thể đau rõ khi bị tắc mạch"]) + "<p>Chi tiết hơn về các dấu hiệu và khi nào cần khám sớm có ở <a href=\"@2\">Bài 2</a>.</p>", ""),
    ("Phân loại bệnh trĩ", "<p>Trĩ nội nằm phía trên <b>đường lược</b>; trĩ ngoại nằm phía dưới đường lược; trĩ hỗn hợp có cả hai thành phần. Phân biệt vị trí rất quan trọng, vì thắt vòng cao su chủ yếu điều trị trĩ nội và không dùng để xử lý đầy đủ búi trĩ ngoại lớn.</p><p>Xem thêm: <a href=\"@3\">phân biệt trĩ nội, trĩ ngoại và trĩ hỗn hợp</a> và <a href=\"@4\">phân độ trĩ Goligher I–IV</a>.</p>", ""),
    ("Chẩn đoán", "<p>Bác sĩ hỏi về thời điểm và lượng máu, triệu chứng sa hay đau, táo bón, thuốc đang dùng và các yếu tố nguy cơ. Việc khám có thể gồm quan sát hậu môn, thăm trực tràng và soi hậu môn. <b>Nội soi đại trực tràng</b> được cân nhắc theo tuổi, nguy cơ, dấu hiệu cảnh báo và chương trình tầm soát.</p>", ""),
    ("Điều trị", "<p>Điều trị tùy loại trĩ, triệu chứng và mức độ sa. Nền tảng là <b>tăng chất xơ, uống đủ nước phù hợp, tránh rặn và không ngồi lâu khi đại tiện</b>. Thuốc bôi hoặc đặt có thể giảm triệu chứng trong thời gian ngắn nhưng không làm biến mất búi trĩ sa lớn. Khi cần, bác sĩ có thể cân nhắc thắt vòng, tiêm xơ, quang đông hoặc phẫu thuật theo chỉ định.</p><p>Triệu chứng nhẹ có thể cải thiện khi điều chỉnh lối sống, nhưng búi trĩ sa do thay đổi cấu trúc thường <b>không tự biến mất hoàn toàn</b>. Không phải ai mắc trĩ cũng cần mổ: nhiều trường hợp đáp ứng điều trị bảo tồn hoặc thủ thuật.</p><p>Đọc thêm: <a href=\"@5\">điều trị bệnh trĩ tại nhà</a> và <a href=\"@6\">các phương pháp thủ thuật, Longo, laser và phẫu thuật</a>.</p>", "bac-thang"),
    ("Khi nào cần đi khám?", "<p>Hãy đi khám khi chảy máu mới xuất hiện hoặc tái diễn, sa búi trĩ, đau nhiều, khối sưng tím hoặc triệu chứng không cải thiện.</p>" + danger("Cần đánh giá khẩn khi", ["Chảy máu nhiều kèm choáng, ngất", "Đau dữ dội hoặc sốt"]) + "<p>Lưu ý: <b>trĩ không chuyển thành ung thư</b>, nhưng ung thư đại trực tràng có thể gây chảy máu tương tự. Vì vậy không tự kết luận mọi trường hợp ra máu là do trĩ.</p>", ""),
  ],
  faq=[("Bệnh trĩ có tự khỏi không?", "Triệu chứng nhẹ có thể cải thiện, nhưng búi trĩ sa do thay đổi cấu trúc thường không tự biến mất hoàn toàn."),
       ("Bệnh trĩ có gây ung thư không?", "Trĩ không chuyển thành ung thư, nhưng ung thư đại trực tràng có thể gây chảy máu tương tự."),
       ("Ai mắc trĩ cũng cần mổ không?", "Không. Nhiều trường hợp đáp ứng điều trị bảo tồn hoặc thủ thuật.")],
  figs={"Bệnh trĩ là gì?": ("tri-giai-phau-tri-noi-tri-ngoai.svg", "Sơ đồ mặt cắt ống hậu môn: trĩ nội phía trên đường lược và trĩ ngoại phía dưới đường lược", "Trĩ nội nằm phía trên đường lược, trĩ ngoại nằm phía dưới. Hình minh họa giáo dục sức khỏe, không theo tỉ lệ và không dùng để tự chẩn đoán."),
        "Điều trị": ("tri-cac-nhom-dieu-tri.svg", "Ba nhóm phương pháp điều trị trĩ: bảo tồn, thủ thuật tại phòng khám và phẫu thuật", "Điều trị đi từ bảo tồn, thủ thuật đến phẫu thuật tùy mức độ và đáp ứng.")}),

# ───────────────────────────── BÀI 2 ─────────────────────────────
dict(n=2, summary=['Máu đỏ tươi dính giấy hoặc phủ ngoài phân thường gặp ở trĩ, nhưng màu máu không đủ để xác định nguyên nhân.', 'Nứt kẽ hậu môn, viêm trực tràng, polyp và ung thư đại trực tràng cũng có thể gây chảy máu.', 'Khám sớm khi chảy máu lần đầu hoặc tái diễn, thiếu máu, sụt cân, đau bụng kéo dài hay thay đổi thói quen đại tiện.', 'Chảy máu nhiều kèm choáng, ngất cần cấp cứu (gọi 115).'], slug="dau-hieu-benh-tri-di-ngoai-ra-mau",
  h1="Dấu hiệu bệnh trĩ – khi nào đi ngoài ra máu cần đi khám?",
  short="Dấu hiệu bệnh trĩ – khi nào đi ngoài ra máu cần đi khám?",
  seo="Dấu hiệu bệnh trĩ – khi nào đi ngoài ra máu cần đi khám?",
  desc="Nhận biết chảy máu đỏ tươi, sa búi trĩ, ngứa và đau hậu môn; phân biệt dấu hiệu cần khám sớm.",
  kw="dấu hiệu bệnh trĩ",
  subtitle="Máu đỏ tươi khi đi ngoài thường được cho là trĩ, nhưng đây chưa phải là kết luận. Hãy biết dấu hiệu nào cần khám sớm.",
  meta="Người trưởng thành và gia đình · Thời gian đọc: 5–7 phút",
  intro="<p>Thấy máu trong phân hoặc trên giấy vệ sinh là điều khiến nhiều người lo lắng. Trĩ là nguyên nhân thường gặp, nhưng không phải nguyên nhân duy nhất. Bài viết giúp bạn nhận ra những dấu hiệu điển hình của bệnh trĩ, những bệnh khác cũng gây chảy máu, và các dấu hiệu cần đi khám sớm.</p>",
  sections=[
    ("Dấu hiệu thường gặp", "<p>Bệnh trĩ có thể gây chảy máu đỏ tươi khi đại tiện, sa búi trĩ, ngứa, ẩm ướt hoặc cảm giác vướng ở hậu môn. Mức độ biểu hiện thay đổi theo vị trí và giai đoạn bệnh.</p>" + ul(["Máu đỏ tươi khi đại tiện", "Búi trĩ sa ra ngoài", "Ngứa, ẩm ướt, kích ứng vùng hậu môn", "Cảm giác vướng, nặng hoặc không đi ngoài hết phân"]), "canh-bao"),
    ("Đi ngoài ra máu do trĩ thường như thế nào?", "<p>Máu có thể dính trên giấy vệ sinh, phủ ngoài phân hoặc nhỏ giọt sau khi đại tiện. Trĩ nội thường chảy máu <b>không đau</b>. Tuy nhiên, <b>màu máu và thời điểm chảy máu không đủ để xác định nguyên nhân</b>.</p>", ""),
    ("Những bệnh lý khác cũng gây chảy máu", "<p>Nhiều bệnh khác cũng gây chảy máu hậu môn – trực tràng, bao gồm:</p>" + ul(["<b>Nứt kẽ hậu môn:</b> thường gây đau rát khi và sau đại tiện", "<b>Viêm trực tràng:</b> có thể kèm mót rặn, tiêu chảy, nhầy hoặc máu", "<b>Polyp và ung thư đại trực tràng:</b> có thể gây chảy máu, thiếu máu, sụt cân hoặc thay đổi thói quen đại tiện"]), ""),
    ("Dấu hiệu cảnh báo", "<p>Nên khám sớm nếu có một trong các dấu hiệu sau:</p>" + ul(["Chảy máu lần đầu hoặc tái diễn", "Lượng máu tăng dần", "Thiếu máu, mệt mỏi", "Sụt cân không rõ nguyên nhân", "Đau bụng kéo dài", "Thay đổi khuôn phân hoặc thói quen đại tiện", "Có tiền sử gia đình ung thư đại trực tràng hoặc polyp tiến triển"]) + danger("Cần cấp cứu khi", ["Chảy máu nhiều kèm choáng, ngất", "Tình trạng toàn thân xấu đi nhanh"]), ""),
    ("Bác sĩ kiểm tra những gì?", "<p>Bác sĩ có thể khám hậu môn, thăm trực tràng, soi hậu môn và cân nhắc <b>nội soi đại trực tràng</b> dựa trên tuổi, nguy cơ và dấu hiệu báo động.</p>", ""),
    ("Người bệnh nên làm gì?", "<p>Hãy ghi nhận lượng máu, màu sắc, thời điểm xuất hiện, các triệu chứng kèm theo và thuốc đang dùng để cung cấp cho bác sĩ. Không tự kết luận là trĩ và không dùng thuốc kéo dài khi chưa được đánh giá.</p><p>Muốn biết các biện pháp chăm sóc phù hợp khi đã được chẩn đoán trĩ, xem <a href=\"@5\">Điều trị bệnh trĩ tại nhà</a>. Về phân loại, xem <a href=\"@3\">trĩ nội, trĩ ngoại và trĩ hỗn hợp</a>.</p>", ""),
  ],
  faq=[("Máu đỏ tươi có chắc chắn là trĩ không?", "Không. Có thể do nứt kẽ, viêm, polyp hoặc ung thư."),
       ("Trĩ nội chảy máu có đau không?", "Thường không đau nếu không có biến chứng hoặc bệnh phối hợp."),
       ("Khi nào cần cấp cứu?", "Chảy máu nhiều, choáng, ngất hoặc tình trạng toàn thân xấu.")],
  figs={"Dấu hiệu thường gặp": ("tri-dau-hieu-ra-mau-can-kham.svg", "So sánh dấu hiệu thường gặp ở bệnh trĩ và các dấu hiệu cần đi khám sớm", "Một số dấu hiệu gợi ý trĩ và những dấu hiệu cần đi khám sớm. Hình mang tính giáo dục, không dùng để tự chẩn đoán.")}),

# ───────────────────────────── BÀI 3 ─────────────────────────────
dict(n=3, summary=['Đường lược là mốc phân biệt: trĩ nội nằm phía trên, trĩ ngoại nằm phía dưới.', 'Trĩ nội thường chảy máu, sa búi và ít đau; trĩ ngoại có thể đau rõ khi tắc mạch.', 'Thắt vòng cao su chủ yếu dành cho trĩ nội, không dùng cho búi trĩ ngoại.', 'Trĩ hỗn hợp có cả hai thành phần, cần đánh giá cả hai khi chọn điều trị.'], slug="phan-biet-tri-noi-tri-ngoai-tri-hon-hop",
  h1="Phân biệt trĩ nội, trĩ ngoại và trĩ hỗn hợp",
  short="Phân biệt trĩ nội, trĩ ngoại và trĩ hỗn hợp",
  seo="Phân biệt trĩ nội, trĩ ngoại và trĩ hỗn hợp",
  desc="So sánh vị trí giải phẫu, triệu chứng và hướng điều trị của trĩ nội, trĩ ngoại và trĩ hỗn hợp.",
  kw="trĩ nội trĩ ngoại",
  subtitle="Vị trí của búi trĩ so với đường lược quyết định triệu chứng và cách điều trị.",
  meta="Người trưởng thành và gia đình · Thời gian đọc: 5–7 phút",
  intro="<p>Nghe bác sĩ nói “trĩ nội”, “trĩ ngoại” hay “trĩ hỗn hợp”, nhiều người không rõ khác nhau thế nào. Điểm khác biệt quan trọng nhất là búi trĩ nằm <b>phía trên hay phía dưới đường lược</b>. Vị trí này ảnh hưởng đến việc có đau hay không và phương pháp điều trị phù hợp.</p>",
  sections=[
    ("Vai trò của đường lược", "<p>Đường lược là mốc giải phẫu quan trọng trong ống hậu môn. <b>Trĩ nội</b> nằm phía trên đường lược; <b>trĩ ngoại</b> nằm phía dưới. Khác biệt thần kinh cảm giác góp phần giải thích vì sao trĩ nội thường ít đau hơn trĩ ngoại: vùng phía dưới đường lược được phủ bằng da và có nhiều thần kinh cảm giác hơn.</p>", "giai-phau"),
    ("Trĩ nội", "<p>Trĩ nội xuất phát từ các đệm hậu môn <b>phía trên đường lược</b>. Biểu hiện điển hình là chảy máu đỏ tươi và sa búi trĩ. Mức độ sa của trĩ nội được mô tả bằng phân độ Goligher I–IV (xem <a href=\"@4\">Bài 4</a>). Trĩ nội thường ít đau, trừ khi búi trĩ sa nghẹt hoặc có bệnh phối hợp như nứt kẽ hậu môn.</p>", ""),
    ("Trĩ ngoại", "<p>Trĩ ngoại nằm dưới đường lược, được phủ bởi da quanh hậu môn. Có thể sờ thấy khối ở rìa hậu môn. Khi <b>tắc mạch</b> (hình thành cục máu đông), khối thường căng, tím và đau đột ngột. Da thừa còn lại sau đợt sưng không phải lúc nào cũng cần phẫu thuật, nhưng cần được khám để phân biệt với các tổn thương khác. Xem thêm <a href=\"@7\">trĩ ngoại tắc mạch</a>.</p>", ""),
    ("Trĩ hỗn hợp", "<p>Có cả thành phần trĩ nội và trĩ ngoại. Người bệnh có thể vừa chảy máu, sa búi trĩ, vừa có khối ngoài hậu môn. Cần đánh giá cả hai thành phần khi lựa chọn điều trị.</p>", ""),
    ("So sánh nhanh", table(["", "Trĩ nội", "Trĩ ngoại", "Trĩ hỗn hợp"], [
        ["<b>Vị trí</b>", "Trên đường lược", "Dưới đường lược", "Cả hai"],
        ["<b>Triệu chứng chính</b>", "Chảy máu đỏ tươi, sa búi trĩ", "Khối ở rìa hậu môn, vướng; đau khi tắc mạch", "Kết hợp cả hai"],
        ["<b>Mức độ đau</b>", "Thường ít đau", "Có thể đau rõ khi tắc mạch", "Tùy thành phần"],
        ["<b>Hướng xử trí thường gặp</b>", "Bảo tồn; thắt vòng, tiêm xơ, quang đông ở trĩ nhẹ–vừa", "Bảo tồn; cắt bỏ ở một số trường hợp chọn lọc", "Cân nhắc phẫu thuật nếu lớn hoặc sa nặng"]]) + "<p>Bảng chỉ mang tính tham khảo; quyết định điều trị luôn cần bác sĩ đánh giá trực tiếp.</p>", ""),
    ("Điều trị khác nhau thế nào?", "<p><b>Thắt vòng cao su chủ yếu áp dụng cho trĩ nội</b>, không dùng cho búi trĩ ngoại vì vùng dưới đường lược có nhiều thần kinh cảm giác. Trĩ nội nhẹ có thể cải thiện bằng điều chỉnh đại tiện; một số trường hợp dai dẳng được cân nhắc thắt vòng, tiêm xơ hoặc quang đông. Trĩ ngoại tắc mạch có thể điều trị bảo tồn hoặc cắt bỏ ở người bệnh chọn lọc. Trĩ hỗn hợp lớn hoặc sa nặng có thể cần phẫu thuật.</p><p>Tìm hiểu chi tiết ở <a href=\"@6\">Bài 6: thủ thuật, Longo, laser và phẫu thuật</a>.</p>", "bac-thang"),
  ],
  faq=[("Trĩ ngoại có thắt vòng được không?", "Thắt vòng chủ yếu áp dụng cho trĩ nội."),
       ("Trĩ nội có đau không?", "Thường ít đau, trừ khi sa nghẹt hoặc có bệnh phối hợp."),
       ("Da thừa hậu môn có phải trĩ không?", "Cần khám để phân biệt da thừa sau trĩ với tổn thương khác.")],
  figs={"Vai trò của đường lược": ("tri-giai-phau-tri-noi-tri-ngoai.svg", "Sơ đồ mặt cắt ống hậu môn: trĩ nội phía trên đường lược và trĩ ngoại phía dưới đường lược", "Đường lược chia ống hậu môn: phía trên là trĩ nội, phía dưới là trĩ ngoại."),
        "Điều trị khác nhau thế nào?": ("tri-cac-nhom-dieu-tri.svg", "Ba nhóm phương pháp điều trị trĩ: bảo tồn, thủ thuật tại phòng khám và phẫu thuật", "Điều trị đi từ bảo tồn, thủ thuật đến phẫu thuật tùy mức độ.")}),

# ───────────────────────────── BÀI 4 ─────────────────────────────
dict(n=4, summary=['Phân độ Goligher I–IV mô tả mức sa của trĩ nội, không áp dụng cho trĩ ngoại.', 'Độ trĩ giúp định hướng nhưng không tự quyết định cách điều trị.', 'Bác sĩ chẩn đoán bằng hỏi bệnh, quan sát, thăm trực tràng và soi hậu môn; nội soi đại trực tràng khi có chỉ định.', 'Không nên tự xác định độ trĩ tại nhà và không tự ngừng thuốc chống đông.'], slug="phan-do-tri-goligher-chan-doan-benh-tri",
  h1="Phân độ trĩ Goligher và cách bác sĩ chẩn đoán",
  short="Phân độ trĩ Goligher và cách bác sĩ chẩn đoán",
  seo="Phân độ trĩ Goligher và cách bác sĩ chẩn đoán",
  desc="Tìm hiểu phân độ trĩ nội Goligher I–IV, quy trình khám và khi nào cần nội soi đại trực tràng.",
  kw="phân độ trĩ Goligher",
  subtitle="Độ trĩ cho biết mức sa của búi trĩ nội và giúp bác sĩ chọn hướng điều trị, nhưng không phải là yếu tố duy nhất.",
  meta="Người trưởng thành và gia đình · Thời gian đọc: 5–7 phút",
  intro="<p>“Trĩ độ 2”, “trĩ độ 3” là những cụm từ bạn thường nghe trong phòng khám. Đó là phân độ Goligher, một cách mô tả mức độ sa của trĩ nội. Bài viết giải thích bốn mức độ, vai trò của phân độ trong điều trị và quy trình bác sĩ chẩn đoán bệnh trĩ.</p>",
  sections=[
    ("Goligher là gì?", "<p>Đây là hệ thống phân độ trĩ nội dựa trên <b>mức độ sa của búi trĩ</b>. Phân độ giúp mô tả bệnh nhưng không thay thế việc đánh giá triệu chứng, thành phần trĩ ngoại, bệnh phối hợp và mong muốn của người bệnh.</p>", ""),
    ("Bốn mức độ", ol(["<b>Độ I:</b> chưa sa ra ngoài, có thể chảy máu.", "<b>Độ II:</b> sa khi đại tiện hoặc rặn nhưng tự co lên.", "<b>Độ III:</b> sa và cần dùng tay đẩy lên.", "<b>Độ IV:</b> sa thường xuyên, không thể đẩy lên hoặc không giữ được trong ống hậu môn."]) + "<p>Hệ thống Goligher chủ yếu mô tả sa của <b>trĩ nội</b>, không phân độ cho trĩ ngoại. Trĩ độ IV thường cần đánh giá phẫu thuật, nhưng quyết định vẫn tùy từng người bệnh.</p>", "do-goligher"),
    ("Phân độ có quyết định điều trị không?", "<p>Không hoàn toàn. Hai người cùng độ III có thể cần cách điều trị khác nhau tùy kích thước búi trĩ, thành phần ngoại, chảy máu, bệnh nền, thuốc chống đông, nguy cơ gây mê và mong muốn của người bệnh.</p>", ""),
    ("Quy trình chẩn đoán", "<p>Bác sĩ hỏi bệnh sử, thuốc đang dùng, tiền sử gia đình và mức độ ảnh hưởng đến sinh hoạt. Việc khám gồm quan sát hậu môn, thăm trực tràng và soi hậu môn. Thăm trực tràng không thay thế soi hậu môn khi đánh giá trĩ nội. Vì vậy bạn không nên tự xác định độ trĩ tại nhà; cần được khám đúng cách.</p>", ""),
    ("Khi nào cần nội soi đại trực tràng?", "<p>Bác sĩ cân nhắc nội soi khi chảy máu chưa giải thích được, thiếu máu, sụt cân, thay đổi thói quen đại tiện, tiền sử gia đình nguy cơ cao hoặc đến tuổi tầm soát. Chỉ định tùy bối cảnh lâm sàng của từng người. Xem thêm <a href=\"@2\">Bài 2: dấu hiệu cần đi khám</a>.</p>", ""),
    ("Chuẩn bị trước khi khám", "<p>Mô tả thời điểm chảy máu, lượng máu, đau hoặc sa, táo bón hoặc tiêu chảy và thuốc đang dùng. <b>Không tự ý ngừng thuốc chống đông hoặc thuốc kê đơn</b> khi chưa hỏi bác sĩ.</p><p>Về hướng điều trị theo mức độ, xem <a href=\"@5\">điều trị tại nhà</a> và <a href=\"@6\">thủ thuật, phẫu thuật</a>.</p>", ""),
  ],
  faq=[("Độ IV có bắt buộc mổ không?", "Thường cần đánh giá phẫu thuật, nhưng quyết định tùy từng bệnh nhân."),
       ("Goligher có phân độ trĩ ngoại không?", "Không, hệ thống này chủ yếu mô tả sa trĩ nội."),
       ("Tự xác định độ trĩ tại nhà được không?", "Không nên; cần khám đúng cách.")],
  figs={"Bốn mức độ": ("tri-phan-do-goligher.svg", "Bốn mức độ trĩ nội theo Goligher: độ I chưa sa, độ II tự co lên, độ III phải đẩy lên, độ IV sa cố định", "Phân độ trĩ nội Goligher I–IV theo mức độ sa. Hình minh họa giáo dục, không dùng để tự chẩn đoán.")}),

# ───────────────────────────── BÀI 5 ─────────────────────────────
dict(n=5, summary=['Tăng chất xơ từ từ và uống đủ nước giúp phân mềm, giảm rặn.', 'Không nhịn đại tiện, không rặn, không ngồi lâu trên bồn cầu.', 'Thuốc bôi hoặc đặt chỉ giảm triệu chứng ngắn hạn; thuốc có corticosteroid chỉ dùng ngắn ngày theo hướng dẫn.', 'Đi khám khi triệu chứng kéo dài, chảy máu tái diễn, đau nhiều hoặc có khối sưng tím.'], slug="dieu-tri-benh-tri-tai-nha-an-uong-sinh-hoat-thuoc",
  h1="Điều trị bệnh trĩ tại nhà: ăn uống, sinh hoạt và thuốc",
  short="Điều trị bệnh trĩ tại nhà: ăn uống, sinh hoạt và thuốc",
  seo="Điều trị bệnh trĩ tại nhà: ăn uống, sinh hoạt và thuốc",
  desc="Hướng dẫn tăng chất xơ, uống nước, điều chỉnh đại tiện, vệ sinh và sử dụng thuốc an toàn.",
  kw="điều trị bệnh trĩ tại nhà",
  subtitle="Phần lớn người bị trĩ nhẹ có thể cải thiện triệu chứng bằng điều chỉnh ăn uống và thói quen đại tiện.",
  meta="Người bệnh trĩ và người chăm sóc · Thời gian đọc: 6–8 phút",
  intro="<p>Chăm sóc tại nhà là bước nền tảng trong điều trị bệnh trĩ, và cũng là bước cần duy trì ngay cả khi bạn đã được làm thủ thuật. Mục tiêu là <b>làm mềm phân, giảm rặn và giảm khó chịu</b>. Bài viết hướng dẫn các biện pháp an toàn, đồng thời nêu những điều không nên làm.</p>",
  sections=[
    ("Ai có thể chăm sóc tại nhà?", "<p>Chăm sóc tại nhà thường phù hợp với triệu chứng nhẹ, chưa có biến chứng hoặc đã được bác sĩ hướng dẫn. Nếu chảy máu mới xuất hiện, tái diễn hoặc đau nhiều thì cần được khám (xem <a href=\"@2\">Bài 2</a>).</p>", ""),
    ("Tăng chất xơ", "<p>Ăn nhiều rau xanh, trái cây, các loại đậu, yến mạch và ngũ cốc nguyên hạt giúp làm mềm phân và giảm rặn. Nhiều khuyến nghị dinh dưỡng đưa ra mức khoảng 25–30 g chất xơ mỗi ngày cho người trưởng thành. Hãy <b>tăng từ từ</b> để hạn chế đầy hơi.</p><p>Có thể cân nhắc bổ sung <b>psyllium</b> khi chế độ ăn chưa đáp ứng, dùng cùng lượng nước phù hợp.</p>", "an-uong"),
    ("Uống nước và thói quen đại tiện", "<p>Uống đủ nước theo nhu cầu cơ thể; điều chỉnh nếu có bệnh tim, thận hoặc đang được chỉ định hạn chế dịch. Đi ngoài khi có cảm giác mót, <b>không nhịn đại tiện</b> kéo dài, không rặn và tránh ngồi lâu trên bồn cầu (không dùng điện thoại trong nhà vệ sinh). Nếu bị táo bón hoặc tiêu chảy kéo dài, cần được điều trị.</p>", ""),
    ("Vận động và vệ sinh", "<p>Đi bộ và vận động đều đặn giúp ruột hoạt động tốt. Vệ sinh nhẹ nhàng bằng nước hoặc giấy mềm không hương liệu, tránh chà xát mạnh. Ngâm nước ấm có thể giúp dễ chịu (thường vài phút đến khoảng 10–15 phút, vài lần mỗi ngày). Cách này có thể làm giảm khó chịu nhưng không làm mất búi trĩ sa, và bằng chứng điều trị còn hạn chế; tránh nước quá nóng.</p>", ""),
    ("Thuốc điều trị triệu chứng", "<p>Thuốc bôi hoặc đặt gây tê, bảo vệ da hoặc làm se có thể giảm khó chịu ngắn hạn. Thuốc chứa <b>corticosteroid</b> tại chỗ chỉ nên dùng ngắn ngày theo hướng dẫn, không tự dùng kéo dài vì có thể làm mỏng da và gây tác dụng không mong muốn. Thuốc làm mềm phân hoặc bổ sung chất xơ được cân nhắc theo nguyên nhân gây táo bón.</p>", ""),
    ("Những điều không nên làm", ul(["Tự chích hoặc cắt búi trĩ", "Đắp lá hoặc hóa chất, tự ý dùng các mẹo truyền miệng", "Lạm dụng thuốc bôi chứa steroid", "Tự ngừng thuốc chống đông khi chưa hỏi bác sĩ", "Tin vào quảng cáo cam kết khỏi vĩnh viễn"]) + "<p>Hiện chưa có bằng chứng cho thấy thức ăn cay trực tiếp gây trĩ; tuy vậy món cay có thể làm khó chịu ở một số người, nếu thấy rát hậu môn sau khi ăn cay bạn có thể giảm bớt.</p>", ""),
    ("Khi nào chăm sóc tại nhà không đủ?", "<p>Hãy đi khám nếu triệu chứng kéo dài, sa búi trĩ ảnh hưởng sinh hoạt, chảy máu tái diễn, đau nhiều hoặc có khối sưng tím. Chảy máu nhiều, choáng, ngất hoặc sốt cần được đánh giá khẩn. Khi chăm sóc tại nhà không đủ, bác sĩ sẽ cân nhắc <a href=\"@6\">thủ thuật hoặc phẫu thuật</a>.</p>", "bac-thang"),
  ],
  faq=[("Ngâm nước ấm có chữa khỏi trĩ không?", "Có thể giảm khó chịu nhưng không làm mất búi trĩ sa."),
       ("Dùng thuốc bôi lâu dài được không?", "Không nên tự dùng kéo dài; steroid tại chỗ cần giới hạn thời gian."),
       ("Ăn cay có gây trĩ không?", "Không có bằng chứng thức ăn cay trực tiếp gây trĩ; có thể làm khó chịu ở một số người.")],
  figs={"Tăng chất xơ": ("tri-an-uong-chat-xo-nuoc.svg", "Rau, trái cây, ngũ cốc nguyên hạt, đậu và nước uống giúp làm mềm phân", "Chất xơ và nước giúp làm mềm phân, giảm rặn khi đi ngoài."),
        "Khi nào chăm sóc tại nhà không đủ?": ("tri-cac-nhom-dieu-tri.svg", "Ba nhóm phương pháp điều trị trĩ: bảo tồn, thủ thuật tại phòng khám và phẫu thuật", "Khi chăm sóc tại nhà không đủ, bác sĩ cân nhắc thủ thuật hoặc phẫu thuật.")}),

# ───────────────────────────── BÀI 6 ─────────────────────────────
dict(n=6, summary=['Không có phương pháp tốt nhất cho mọi người; lựa chọn tùy loại trĩ, mức độ, bệnh nền và mong muốn.', 'Thắt vòng, tiêm xơ, quang đông là thủ thuật tại phòng khám, thường cho trĩ nội nhẹ đến vừa.', 'Cắt trĩ, Longo, HAL/THD và laser có chỉ định, lợi ích và giới hạn riêng; laser không đồng nghĩa không đau hay không tái phát.', 'Sau điều trị vẫn cần chất xơ, đủ nước, vệ sinh và tái khám.'], slug="phuong-phap-dieu-tri-benh-tri-longo-laser-phau-thuat",
  h1="Điều trị bệnh trĩ: thủ thuật, Longo, laser và phẫu thuật",
  short="Điều trị bệnh trĩ: thủ thuật, Longo, laser và phẫu thuật",
  seo="Điều trị bệnh trĩ: thủ thuật, Longo, laser và phẫu thuật",
  desc="So sánh thắt vòng, tiêm xơ, Milligan–Morgan, Ferguson, Longo, laser và HAL/THD.",
  kw="phẫu thuật bệnh trĩ",
  subtitle="Không có phương pháp tốt nhất cho tất cả. Lựa chọn tùy loại trĩ, mức độ, bệnh nền và mong muốn của bạn.",
  meta="Người bệnh trĩ và gia đình · Thời gian đọc: 8–10 phút",
  intro="<p>Khi điều trị bảo tồn không đủ, bác sĩ có thể đề nghị thủ thuật tại phòng khám hoặc phẫu thuật. Nhiều tên kỹ thuật như thắt vòng, Longo, laser, HAL/THD khiến người bệnh khó chọn. Bài viết so sánh các phương pháp để bạn hiểu và có câu hỏi phù hợp khi trao đổi với bác sĩ.</p>",
  sections=[
    ("Khi nào cần thủ thuật hoặc phẫu thuật?", "<p>Bác sĩ cân nhắc khi triệu chứng dai dẳng dù điều trị bảo tồn, trĩ nội độ III–IV hoặc trĩ nội chảy máu/sa ảnh hưởng chất lượng sống, trĩ hỗn hợp lớn, sa nặng hoặc có biến chứng. Quyết định dựa trên khám, bệnh nền và mong muốn của người bệnh. Trước đó cần chăm sóc đầy đủ (xem <a href=\"@5\">Bài 5</a>) và xác định độ trĩ (xem <a href=\"@4\">Bài 4</a>).</p>", "bac-thang"),
    ("Thủ thuật tại phòng khám", "<p><b>Thắt vòng cao su</b> gây thiếu máu khu trú và xơ hóa búi trĩ nội, thường dùng ở trĩ nội độ I–III phù hợp. <b>Tiêm xơ</b> có thể hữu ích ở một số trường hợp chảy máu. <b>Quang đông hồng ngoại</b> tạo xơ ở trĩ nội nhỏ. Các thủ thuật này không xử lý đầy đủ búi trĩ ngoại lớn và đôi khi cần lặp lại. Với trĩ độ IV (sa cố định), thắt vòng không phải lựa chọn thường quy và thường cần đánh giá phẫu thuật.</p>", ""),
    ("Milligan–Morgan và Ferguson", "<p>Milligan–Morgan là cắt trĩ kiểu mở; Ferguson cắt trĩ và khâu đóng vết mổ. Hai kỹ thuật này có thể xử lý thành phần nội và ngoại đáng kể, thường cân nhắc ở trĩ hỗn hợp lớn hoặc độ III–IV. Đau sau mổ là vấn đề cần trao đổi; cần bảo tồn cầu niêm mạc/da và cơ thắt để hạn chế hẹp hậu môn, tổn thương cơ thắt.</p>", ""),
    ("Phẫu thuật Longo", "<p>Longo dùng máy khâu vòng cắt một vòng niêm mạc – dưới niêm mạc phía trên đường lược, kéo treo phần đệm trĩ sa. Phương pháp chủ yếu tác động lên trĩ nội, không trực tiếp cắt thành phần ngoại. Ở bệnh nhân phù hợp, đau sớm có thể ít hơn cắt trĩ kinh điển; tuy nhiên một số nghiên cứu ghi nhận tái sa hoặc cần can thiệp lại cao hơn trong theo dõi dài hạn. Biến chứng có thể gồm chảy máu, đau, mót rặn, hẹp và hiếm gặp biến chứng vùng chậu nghiêm trọng. Không phải lựa chọn mặc định cho mọi trĩ độ III–IV.</p>", ""),
    ("Điều trị bằng laser", "<p>Laser không phải một kỹ thuật duy nhất. Laser hemorrhoidoplasty thường đưa sợi quang vào mô trĩ để tạo nhiệt và làm co nhỏ búi trĩ; các kỹ thuật khác có cách tác động khác nhau. Một số nghiên cứu ghi nhận giảm đau sớm hoặc hồi phục nhanh ở bệnh nhân chọn lọc, nhưng thiết bị, bước sóng, năng lượng và quy trình không đồng nhất; bằng chứng dài hạn còn hạn chế. <b>Laser không đồng nghĩa không đau, không biến chứng hoặc không tái phát.</b></p>", ""),
    ("HAL/THD", "<p>HAL hoặc THD dùng đầu dò Doppler xác định nhánh động mạch cấp máu để thắt, có thể phối hợp khâu treo niêm mạc (mucopexy). Một số người bệnh có thể ít đau hơn cắt trĩ, nhưng nguy cơ tái phát/tái sa có thể cao hơn ở bệnh sa nặng.</p>", ""),
    ("So sánh các phương pháp", table(["Phương pháp", "Thường cân nhắc cho", "Điểm cần lưu ý"], [
        ["Thắt vòng cao su", "Trĩ nội độ I–III", "Không xử lý trĩ ngoại lớn; có thể cần lặp lại"],
        ["Tiêm xơ / quang đông", "Trĩ nội nhẹ, chảy máu", "Hiệu quả thường ngắn hạn; có thể cần lặp lại"],
        ["Milligan–Morgan / Ferguson", "Trĩ hỗn hợp lớn, độ III–IV", "Đau sau mổ; cần bảo tồn cầu da/niêm mạc và cơ thắt"],
        ["Longo", "Chủ yếu trĩ nội sa", "Không cắt thành phần ngoại; có thể tái sa hoặc cần can thiệp lại"],
        ["Laser", "Bệnh nhân chọn lọc", "Kỹ thuật không đồng nhất; bằng chứng dài hạn còn hạn chế"],
        ["HAL/THD", "Bệnh nhân chọn lọc", "Có thể tái phát/tái sa cao hơn ở bệnh sa nặng"]]), ""),
    ("Chọn phương pháp nào?", "<p>Không có phương pháp tốt nhất cho tất cả. Thắt vòng thường phù hợp một số trĩ nội độ I–III; cắt trĩ kinh điển có vai trò với trĩ hỗn hợp lớn hoặc sa nặng; Longo chủ yếu xử lý sa trĩ nội; laser cần hiểu rõ kỹ thuật cụ thể; HAL/THD cần cân nhắc ở nhóm phù hợp. Hãy hỏi bác sĩ về lợi ích, đau, tái phát, biến chứng, thời gian nghỉ và chi phí.</p>", ""),
    ("Chăm sóc sau điều trị", "<p>Tuân thủ hướng dẫn giảm đau, làm mềm phân, ăn chất xơ, uống nước phù hợp, vệ sinh và tái khám. Báo cơ sở điều trị khi chảy máu nhiều, bí tiểu, sốt, đau tăng bất thường hoặc có dấu hiệu nhiễm trùng.</p>", ""),
  ],
  faq=[("Longo tốt hơn cắt trĩ truyền thống không?", "Không cho mọi người; có thể ít đau sớm ở bệnh nhân phù hợp nhưng không xử lý trực tiếp trĩ ngoại."),
       ("Laser có không đau và không tái phát không?", "Không. Có thể đau, biến chứng và tái phát; kết quả tùy kỹ thuật và lựa chọn bệnh nhân."),
       ("Trĩ độ IV có thể thắt vòng không?", "Thường cần đánh giá phẫu thuật; thắt vòng không phải lựa chọn thường quy cho trĩ sa cố định.")],
  figs={"Khi nào cần thủ thuật hoặc phẫu thuật?": ("tri-cac-nhom-dieu-tri.svg", "Ba nhóm phương pháp điều trị trĩ: bảo tồn, thủ thuật tại phòng khám và phẫu thuật", "Điều trị đi từ bảo tồn, thủ thuật đến phẫu thuật tùy mức độ và đáp ứng.")}),

# ───────────────────────────── BÀI 7 ─────────────────────────────
dict(n=7, summary=['Thai kỳ làm tăng nguy cơ trĩ do táo bón, áp lực vùng chậu và rặn.', 'Ưu tiên chăm sóc bảo tồn; không tự dùng thuốc và hỏi bác sĩ sản khoa trước khi dùng.', 'Trĩ ngoại tắc mạch gây khối sưng tím, đau đột ngột; không tự chích, rạch hoặc nặn.', 'Khám sớm khi đau dữ dội, khối tím mới xuất hiện, chảy máu nhiều, sốt hoặc có mủ.'], slug="benh-tri-khi-mang-thai-tri-ngoai-tac-mach",
  h1="Bệnh trĩ khi mang thai và trĩ ngoại tắc mạch",
  short="Bệnh trĩ khi mang thai và trĩ ngoại tắc mạch",
  seo="Bệnh trĩ khi mang thai và trĩ ngoại tắc mạch",
  desc="Nguyên nhân và cách chăm sóc bệnh trĩ khi mang thai; nhận biết và xử trí trĩ ngoại tắc mạch.",
  kw="bệnh trĩ khi mang thai",
  subtitle="Thai kỳ làm tăng nguy cơ trĩ. Hiểu cách chăm sóc an toàn và nhận biết trĩ ngoại tắc mạch.",
  meta="Thai phụ, người nhà và người trưởng thành · Thời gian đọc: 6–8 phút",
  intro="<p>Nhiều phụ nữ lần đầu bị trĩ trong thai kỳ hoặc sau sinh. Bên cạnh đó, một tình trạng đau đột ngột ở hậu môn là <b>trĩ ngoại tắc mạch</b> có thể gặp ở bất kỳ ai. Bài viết giải thích nguyên nhân, cách chăm sóc an toàn và những dấu hiệu cần khám ngay.</p>",
  sections=[
    ("Vì sao thai phụ dễ mắc trĩ?", "<p>Thay đổi nội tiết có thể làm chậm nhu động ruột và gây táo bón. Tử cung lớn làm tăng áp lực vùng chậu; thay đổi thể tích máu và rặn khi đại tiện hoặc sinh cũng góp phần.</p>", "thai-ky"),
    ("Triệu chứng và ảnh hưởng", "<p>Thai phụ có thể chảy máu đỏ tươi, ngứa, sa búi trĩ hoặc đau hậu môn. Một số trường hợp cải thiện sau sinh khi áp lực vùng chậu giảm, nhưng không phải tất cả. <b>Chảy máu trong thai kỳ vẫn cần được đánh giá.</b></p>", ""),
    ("Chăm sóc trong thai kỳ", "<p>Ưu tiên chất xơ, nước phù hợp, vận động nhẹ nếu không có chống chỉ định sản khoa, không nhịn đại tiện và tránh rặn. Ngâm nước ấm có thể giảm khó chịu. Trao đổi với bác sĩ sản khoa trước khi dùng thuốc hoặc chất bổ sung. Xem thêm <a href=\"@5\">Điều trị bệnh trĩ tại nhà</a>.</p>", ""),
    ("Thuốc và thủ thuật khi mang thai", "<p>Không tự ý dùng thuốc uống, đặt hoặc bôi, nhất là chế phẩm phối hợp nhiều hoạt chất. Thường ưu tiên điều trị bảo tồn; thủ thuật hoặc phẫu thuật được trì hoãn nếu an toàn, trừ khi có biến chứng hoặc chỉ định đặc biệt. Cần phối hợp chuyên khoa sản và hậu môn – trực tràng.</p>", ""),
    ("Trĩ ngoại tắc mạch là gì?", "<p>Là tình trạng hình thành cục máu đông trong đám rối tĩnh mạch dưới da quanh hậu môn. Thường có <b>khối sưng căng, tím, đau đột ngột</b> và đau tăng khi ngồi hoặc đại tiện. Cần phân biệt với áp xe quanh hậu môn (có thể kèm sốt, nóng đỏ lan hoặc mủ). Xem thêm <a href=\"@3\">phân biệt trĩ nội, trĩ ngoại</a>.</p>", ""),
    ("Xử trí trĩ ngoại tắc mạch", "<p>Tùy thời điểm khởi phát, mức đau, kích thước, bệnh nền và mong muốn. Có trường hợp điều trị bảo tồn bằng giảm đau phù hợp, làm mềm phân, ngâm ấm và theo dõi; trường hợp đau dữ dội hoặc chọn lọc có thể cân nhắc cắt bỏ. <b>Không tự chích, rạch hoặc nặn tại nhà.</b> Về các phương pháp can thiệp xem <a href=\"@6\">Bài 6</a>.</p>", ""),
    ("Khi nào cần khám ngay?", danger("Khám sớm khi", ["Đau dữ dội", "Khối tím mới xuất hiện", "Chảy máu nhiều", "Sốt, có mủ hoặc đau tăng"]) + "<p>Thai phụ nên liên hệ bác sĩ sản khoa khi có chảy máu hay đau đáng kể.</p>", ""),
  ],
  faq=[("Trĩ khi mang thai có hết sau sinh không?", "Có thể cải thiện nhưng đôi khi còn triệu chứng hoặc sa kéo dài."),
       ("Thai phụ có được phẫu thuật không?", "Thường ưu tiên bảo tồn và trì hoãn nếu an toàn; quyết định tùy chỉ định."),
       ("Trĩ ngoại tắc mạch lúc nào cũng mổ không?", "Không; có thể điều trị bảo tồn hoặc cắt bỏ ở trường hợp chọn lọc.")],
  figs={"Vì sao thai phụ dễ mắc trĩ?": ("tri-cham-soc-thai-ky.svg", "Bốn lưu ý chăm sóc trĩ khi mang thai: chất xơ, nước, vận động nhẹ và không nhịn đại tiện", "Chăm sóc trĩ trong thai kỳ ưu tiên biện pháp bảo tồn và trao đổi với bác sĩ sản khoa.")}),
]
