document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('sendMessageForm');
    const responseMessage = document.getElementById('response-message');
    const submitButton = document.getElementById('submitButton');

    form.addEventListener('submit', async (event) => {
        event.preventDefault();

        // Tampilkan status loading
        submitButton.disabled = true;
        submitButton.textContent = 'Mengirim...';
        responseMessage.classList.add('hidden');

        const formData = new FormData(form);
        const chatId = formData.get('chatId');
        const text = formData.get('messageText');

        // Ganti URL ini dengan URL API backend Anda yang sebenarnya
        // Jika backend berjalan di mesin yang sama, cukup gunakan path
        const apiUrl = '/send_message';

        try {
            const response = await fetch(apiUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    chat_id: chatId,
                    text: text,
                }),
            });

            const result = await response.json();

            if (response.ok && result.success) {
                showResponseMessage(result.message || 'Pesan berhasil dikirim!', 'success');
                form.reset(); // Kosongkan form setelah berhasil
            } else {
                showResponseMessage(result.error || 'Terjadi kesalahan yang tidak diketahui.', 'error');
            }
        } catch (error) {
            console.error('Error:', error);
            showResponseMessage('Gagal terhubung ke server. Periksa konsol untuk detail.', 'error');
        } finally {
            // Kembalikan tombol ke keadaan normal
            submitButton.disabled = false;
            submitButton.textContent = 'Kirim Pesan';
        }
    });

    function showResponseMessage(message, type) {
        responseMessage.textContent = message;
        responseMessage.className = type; // 'success' atau 'error'
        responseMessage.classList.remove('hidden');
    }
});
