import React from 'react';

// This is a placeholder for the main dashboard page.
// In a real application, this component would:
// 1. Handle the Telegram Web App authentication data on load.
// 2. Exchange the Telegram data for a JWT from the backend API.
// 3. Store the JWT and use it for subsequent API requests.
// 4. Fetch and display the user's projects.
// 5. Provide an interface for uploading new projects.

const DashboardPage = () => {
  return (
    <div className="min-h-screen bg-gray-100 text-gray-800">
      <header className="bg-white shadow-md">
        <nav className="container mx-auto px-6 py-4">
          <h1 className="text-2xl font-bold text-blue-600">Panel Hosting Dashboard</h1>
        </nav>
      </header>
      <main className="container mx-auto px-6 py-8">
        <h2 className="text-3xl font-semibold mb-6">Selamat Datang!</h2>

        <div className="bg-white p-8 rounded-lg shadow-lg">
          <h3 className="text-xl font-bold mb-4">Upload Proyek Baru</h3>
          <p className="mb-4">
            Fitur upload akan tersedia di sini. Anda akan dapat mengunggah file .zip proyek Anda untuk dideploy secara otomatis.
          </p>
          <button
            disabled
            className="bg-gray-400 text-white font-bold py-2 px-4 rounded cursor-not-allowed"
          >
            Pilih File .zip (Segera Hadir)
          </button>
        </div>

        <div className="mt-8">
          <h3 className="text-xl font-bold mb-4">Proyek Anda</h3>
          <div className="bg-white p-8 rounded-lg shadow-lg">
            <p>Daftar proyek Anda yang sedang berjalan akan ditampilkan di sini.</p>
          </div>
        </div>
      </main>
    </div>
  );
};

export default DashboardPage;
