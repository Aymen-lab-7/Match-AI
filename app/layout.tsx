import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import "./globals.css";
import Script from "next/script";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "SkinDupe | Match AI",
  description: "Visual Recognition Engine for Skincare and Fashion",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <head>
        {/* إضافة مكتبة ml5.js لتمكين الذكاء الاصطناعي المحلي (Local AI) */}
        {/* هذا يحل مشكلة الـ 404 وقيود الـ API في منطقتك */}
        <Script 
          src="https://unpkg.com/ml5@latest/dist/ml5.min.js" 
          strategy="beforeInteractive"
        />
      </head>
      <body
        className={`${geistSans.variable} ${geistMono.variable} antialiased bg-black`}
      >
        {children}
      </body>
    </html>
  );
}