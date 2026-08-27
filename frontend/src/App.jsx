import { useEffect, useState } from "react";


function App() {
  const [quotes, setQuotes] = useState([]);
  const [count, setCount] = useState(0);
  const [lastScrapedAt, setLastScrapedAt] = useState(null);
  const [refreshFailed, setRefreshFailed] = useState(false);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [search, setSearch] = useState("");
  const [selectedTag, setSelectedTag] = useState("");


  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/quotes/")
      .then((response) => {
        if (!response.ok) {
          throw new Error("Failed to load quotes");
        }

        return response.json();
      })
      .then((data) => {
        setQuotes(data.quotes);
        setCount(data.count);
        setLastScrapedAt(data.last_scraped_at);
        setRefreshFailed(data.refresh_failed);
        setError(null);
      })
      .catch((error) => {
        setError(error.message);
      })
      .finally(() => {
        setLoading(false);
      });
  }, []);


  function formatDate(dateString) {
    if (!dateString) {
      return "Never";
    }

    return new Date(dateString).toLocaleString();
  }

  const filteredQuotes = quotes.filter((quote) => {
    const searchTerm = search.toLowerCase();

    const matchesSearch =
      quote.text.toLowerCase().includes(searchTerm) ||
      quote.author.toLowerCase().includes(searchTerm);

    const matchesTag =
      selectedTag === "" ||
      quote.tags.includes(selectedTag);

    return matchesSearch && matchesTag;
  });

  const allTags = [
    ...new Set(
      quotes.flatMap((quote) => quote.tags)
    ),
  ].sort();


  return (
    <main>
      <h1>Quote Scraper</h1>

      {loading && <p>Loading quotes...</p>}

      {error && <p>Error: {error}</p>}

      {refreshFailed && (
        <p>
          Unable to refresh quotes. Showing previously saved data.
        </p>
      )}

      {!loading && !error && (
        <>
          <p>Total quotes: {count}</p>

          <p>
            Last updated: {formatDate(lastScrapedAt)}
          </p>

          <input
            type="text"
            placeholder="Search quotes or authors..."
            value={search}
            onChange={(event) => setSearch(event.target.value)}
          />

          <select
            value={selectedTag}
            onChange={(event) => setSelectedTag(event.target.value)}
          >
            <option value="">All tags</option>

            {allTags.map((tag) => (
              <option key={tag} value={tag}>
                {tag}
              </option>
            ))}
          </select>

          {filteredQuotes.map((quote) => (
            <article key={quote.id}>
              <p>"{quote.text}"</p>

              <p>- {quote.author}</p>

              <div>
                {quote.tags.map((tag) => (
                  <span key={tag}>
                    {tag}{" "}
                  </span>
                ))}
              </div>
            </article>
          ))}
        </>
      )}
    </main>
  );
}


export default App;