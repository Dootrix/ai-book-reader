import Link from "next/link";

export default function Home() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 flex items-center justify-center p-4">
      <div className="max-w-4xl mx-auto text-center">
        <h1 className="text-6xl font-bold text-gray-900 mb-4">
          📚 AI Book Reader
        </h1>
        <p className="text-xl text-gray-600 mb-8">
          Your intelligent companion for reading and understanding books
        </p>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mt-12">
          <Link href="/notes" className="bg-white p-6 rounded-lg shadow-md hover:shadow-lg transition-shadow">
            <h3 className="text-lg font-semibold mb-2">📝 Smart Notes</h3>
            <p className="text-gray-600">Take AI-powered notes while reading</p>
          </Link>
          <Link href="/bookmarks" className="bg-white p-6 rounded-lg shadow-md hover:shadow-lg transition-shadow">
            <h3 className="text-lg font-semibold mb-2">🔖 Bookmarks</h3>
            <p className="text-gray-600">Save important passages and references</p>
          </Link>
          <div className="bg-white p-6 rounded-lg shadow-md">
            <h3 className="text-lg font-semibold mb-2">🤖 AI Insights</h3>
            <p className="text-gray-600">Get AI-generated summaries and insights</p>
          </div>
        </div>
      </div>
    </div>
  );
}
