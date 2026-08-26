import { useState } from "react";


function App() {
  const [quotes, setQuotes] = useState([]);
  const [count, setCount] = useState(0);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);


  function scrapeQuotes() {
    setLoading(true);
    setError(null);

    fetch("http://127.0.0.1:8000/api/quotes/")
      .then((response) => {
        if (!response.ok) {
          throw new Error("Failed to fetch quotes");
        }

        return response.json();
      })
      .then((data) => {
        setQuotes(data.quotes);
        setCount(data.count);
      })
      .catch((error) => {
        setError(error.message);
      })
      .finally(() => {
        setLoading(false);
      });
  }


  return (
    <main>
      <h1>Quote Scraper</h1>

      <button onClick={scrapeQuotes} disabled={loading}>
        {loading ? "Scraping..." : "Scrape Quotes"}
      </button>

      {loading && <p>Scraping all pages. Please wait...</p>}

      {error && <p>Error: {error}</p>}

      {!loading && quotes.length > 0 && (
        <p>Total quotes scraped: {count}</p>
      )}

      {quotes.map((quote, index) => (
        <div key={index}>
          <p>"{quote.text}"</p>
          <p>- {quote.author}</p>
        </div>
      ))}
    </main>
  );
}


export default App;