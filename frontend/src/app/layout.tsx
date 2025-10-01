import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "AI Book Reader",
  description: "AI-assisted book reader with notes and bookmarks",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className="antialiased">
        {children}
      </body>
    </html>
  );
}
