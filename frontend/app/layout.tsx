import type { Metadata } from "next";
import Link from "next/link";
import "./globals.css";

export const metadata: Metadata = {
  title: "AI Book Reader",
  description: "AI assisted book reader",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className="antialiased">
        <nav className="bg-white shadow-sm border-b">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="flex justify-between h-16">
              <div className="flex items-center">
                <Link href="/" className="text-xl font-bold text-gray-900">
                  📚 AI Book Reader
                </Link>
              </div>
              <div className="flex items-center space-x-8">
                <Link href="/notes" className="text-gray-600 hover:text-gray-900">
                  📝 Notes
                </Link>
                <Link href="/bookmarks" className="text-gray-600 hover:text-gray-900">
                  🔖 Bookmarks
                </Link>
              </div>
            </div>
          </div>
        </nav>
        {children}
      </body>
    </html>
  );
}
