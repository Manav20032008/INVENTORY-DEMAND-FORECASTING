import { useState } from "react";
import HistoryTable from "../components/HistoryTable";
import LoadingSpinner from "../components/LoadingSpinner";
import ErrorAlert from "../components/ErrorAlert";
import Pagination from "../components/Pagination";
import usePredictions from "../hooks/usePredictions";

const PAGE_SIZE = 15;

export default function History() {
  const [storeFilter, setStoreFilter] = useState("");
  const [page, setPage] = useState(1);
  const { predictions, loading, error, reload } = usePredictions({
    page,
    limit: PAGE_SIZE,
    store: storeFilter || null,
  });

  const handleStoreChange = (event) => {
    setStoreFilter(event.target.value);
    setPage(1);
  };

  const clearFilter = () => {
    setStoreFilter("");
    setPage(1);
  };

  return (
    <section className="page">
      <div className="page-header history-header">
        <div>
          <h2>Prediction History</h2>
          <p>Browse stored forecasts with store filtering and pagination.</p>
        </div>
        <div className="history-actions">
          <input
            type="number"
            min="1"
            placeholder="Filter by store ID"
            value={storeFilter}
            onChange={handleStoreChange}
            aria-label="Filter by store ID"
          />
          {storeFilter ? (
            <button type="button" className="btn btn-secondary btn-sm" onClick={clearFilter}>
              Clear
            </button>
          ) : null}
          <button type="button" className="btn btn-secondary" onClick={reload}>
            Refresh
          </button>
        </div>
      </div>

      <ErrorAlert message={error} onRetry={reload} />

      {loading ? <LoadingSpinner message="Loading prediction history..." /> : null}

      {!loading && predictions.length > 0 ? (
        <Pagination
          page={page}
          limit={PAGE_SIZE}
          itemCount={predictions.length}
          onPageChange={setPage}
        />
      ) : null}

      <HistoryTable predictions={predictions} loading={loading} />

      {!loading && predictions.length > 0 ? (
        <Pagination
          page={page}
          limit={PAGE_SIZE}
          itemCount={predictions.length}
          onPageChange={setPage}
        />
      ) : null}
    </section>
  );
}
