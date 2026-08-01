import { Link } from "react-router-dom"

function formatPrediction(value) {
  return Number(value).toFixed(2)
}

function formatTimestamp(iso) {
  return new Date(iso).toLocaleString(undefined, {
    year: "numeric",
    month: "short",
    day: "numeric",
    hour: "2-digit",
    minute: "2-digit",
  })
}

export default function HistoryTable({ predictions, loading }) {
  if (loading) return null

  if (!predictions.length) {
    return (
      <div className="card empty-state">
        <div className="empty-state__icon" aria-hidden="true">
          📋
        </div>
        <h3>No predictions yet</h3>
        <p>Run a forecast from the home page and results will appear here automatically.</p>
        <Link to="/" className="btn btn-primary">
          Go to Predict
        </Link>
      </div>
    )
  }

  return (
    <div className="card table-card">
      <div className="card-header table-card__header">
        <div>
          <h2>Recent forecasts</h2>
          <p>Sorted by most recent first</p>
        </div>
        <span className="badge badge--muted">{predictions.length} on this page</span>
      </div>
      <div className="table-wrapper">
        <table className="data-table">
          <thead>
            <tr>
              <th>ID</th>
              <th>Store</th>
              <th>Item</th>
              <th>Predicted sales</th>
              <th>Created</th>
            </tr>
          </thead>
          <tbody>
            {predictions.map((row) => (
              <tr key={row.id}>
                <td>
                  <span className="mono">#{row.id}</span>
                </td>
                <td>
                  <span className="badge badge--store">Store {row.store}</span>
                </td>
                <td>
                  <span className="badge badge--item">Item {row.item}</span>
                </td>
                <td>
                  <strong className="prediction-value">{formatPrediction(row.prediction)}</strong>
                </td>
                <td className="timestamp">{formatTimestamp(row.created_at)}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  )
}
