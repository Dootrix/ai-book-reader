export default function Home() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 dark:from-gray-900 dark:to-gray-800">
      <div className="container mx-auto px-4 py-16">
        <div className="text-center">
          <h1 className="text-5xl font-bold text-gray-900 dark:text-white mb-4">
            AI Book Reader
          </h1>
          <p className="text-xl text-gray-600 dark:text-gray-300 mb-12">
            Your intelligent companion for reading, taking notes, and bookmarking
          </p>
          
          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8 mt-16">
            <div className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-lg">
              <div className="text-3xl mb-4">📚</div>
              <h3 className="text-xl font-semibold mb-2 text-gray-900 dark:text-white">
                Smart Reading
              </h3>
              <p className="text-gray-600 dark:text-gray-300">
                AI-powered reading assistance to enhance your comprehension and learning experience.
              </p>
            </div>
            
            <div className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-lg">
              <div className="text-3xl mb-4">✍️</div>
              <h3 className="text-xl font-semibold mb-2 text-gray-900 dark:text-white">
                Note Taking
              </h3>
              <p className="text-gray-600 dark:text-gray-300">
                Capture your thoughts and insights with our intuitive note-taking system.
              </p>
            </div>
            
            <div className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-lg">
              <div className="text-3xl mb-4">🔖</div>
              <h3 className="text-xl font-semibold mb-2 text-gray-900 dark:text-white">
                Bookmarks
              </h3>
              <p className="text-gray-600 dark:text-gray-300">
                Save important passages and easily return to them whenever you need.
              </p>
            </div>
          </div>
          
          <div className="mt-16">
            <div className="bg-white dark:bg-gray-800 p-8 rounded-lg shadow-lg max-w-2xl mx-auto">
              <h2 className="text-2xl font-bold mb-4 text-gray-900 dark:text-white">
                Getting Started
              </h2>
              <div className="text-left space-y-4 text-gray-600 dark:text-gray-300">
                <div className="flex items-start space-x-3">
                  <span className="flex-shrink-0 w-6 h-6 bg-blue-500 text-white rounded-full flex items-center justify-center text-sm font-bold">1</span>
                  <span>Upload or import your books and documents</span>
                </div>
                <div className="flex items-start space-x-3">
                  <span className="flex-shrink-0 w-6 h-6 bg-blue-500 text-white rounded-full flex items-center justify-center text-sm font-bold">2</span>
                  <span>Start reading with AI assistance</span>
                </div>
                <div className="flex items-start space-x-3">
                  <span className="flex-shrink-0 w-6 h-6 bg-blue-500 text-white rounded-full flex items-center justify-center text-sm font-bold">3</span>
                  <span>Take notes and create bookmarks as you read</span>
                </div>
              </div>
              <div className="mt-8">
                <button className="bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 px-6 rounded-lg transition-colors">
                  Start Reading
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
