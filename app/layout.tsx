import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "Match AI | Intelligent Dupe Search",
  description: "Discover affordable alternatives for your favorite products using AI.",
  // ربط الحساب بـ Impact للبدء في جني العمولات 💰
  verification: {
    other: {
      "impact-site-verification": ["448ccace-d7a0-442b-95b1-4f0414f87f50"],
    },
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <main className="min-h-screen bg-black text-white">
          {/* يمكنك إضافة Navbar هنا لاحقاً */}
          {children}
        </main>
      </body>
    </html>
  );
}