// Danh sách các câu chúc
const quotes = [
    "Chúc bạn một ngày vui vẻ và tràn đầy năng lượng!",
    "Mọi điều tốt đẹp nhất sẽ đến với bạn hôm nay!",
    "Hãy luôn mỉm cười vì bạn xứng đáng được hạnh phúc!",
    "Chúc bạn thành công trong mọi dự định của mình!",
    "Hãy tận hưởng từng khoảnh khắc tuyệt vời trong cuộc sống!",
    "Niềm vui lớn nhất là lan tỏa yêu thương đến mọi người!",
    "Chúc một ngày đầy ắp tiếng cười và niềm vui!"
];

// Hàm để tạo câu chúc ngẫu nhiên
function generateRandomQuote() {
    const randomIndex = Math.floor(Math.random() * quotes.length);
    document.getElementById("random-quote").textContent = quotes[randomIndex];
}

// Hiển thị câu chúc ngẫu nhiên khi tải trang
document.addEventListener("DOMContentLoaded", generateRandomQuote);

