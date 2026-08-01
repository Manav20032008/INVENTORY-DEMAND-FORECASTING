import StatCard from "./StatCard"
import PredictionsTrendChart from "./PredictionsTrendChart"
import StoreBreakdownChart from "./StoreBreakdownChart"
import PredictionRangeBar from "./PredictionRangeBar"

export default function AnalyticsDashboard({ analytics, predictions }) {
  if (!analytics) return null

  const hasData = analytics.total_predictions > 0

  return (
    <div className="dashboard">
      <section className="dashboard__stats">
        <StatCard
          label="Total predictions"
          value={analytics.total_predictions}
          hint="Stored in PostgreSQL"
          accent="blue"
        />
        <StatCard
          label="Average forecast"
          value={analytics.average_prediction.toFixed(2)}
          hint="Mean predicted sales"
          accent="cyan"
        />
        <StatCard
          label="Highest forecast"
          value={analytics.highest_prediction.toFixed(2)}
          hint="Peak demand signal"
          accent="green"
        />
        <StatCard
          label="Lowest forecast"
          value={analytics.lowest_prediction.toFixed(2)}
          hint="Minimum recorded"
          accent="amber"
        />
        <StatCard
          label="Unique stores"
          value={analytics.unique_stores}
          hint="Distinct store IDs"
          accent="violet"
        />
        <StatCard
          label="Unique items"
          value={analytics.unique_items}
          hint="Distinct item IDs"
          accent="rose"
        />
      </section>

      {!hasData ? (
        <div className="card empty-state dashboard-empty">
          <div className="empty-state__icon" aria-hidden="true">
            📊
          </div>
          <h3>Dashboard waiting for data</h3>
          <p>Create your first prediction to unlock charts and aggregate metrics.</p>
        </div>
      ) : (
        <section className="dashboard__charts">
          <article className="card chart-card chart-card--wide">
            <div className="card-header">
              <h2>Prediction trend</h2>
              <p>Recent forecast values over time (last {predictions.length} records)</p>
            </div>
            <PredictionsTrendChart predictions={predictions} />
          </article>

          <article className="card chart-card">
            <div className="card-header">
              <h2>Store breakdown</h2>
              <p>Average predicted sales by store</p>
            </div>
            <StoreBreakdownChart predictions={predictions} />
          </article>

          <article className="card chart-card">
            <div className="card-header">
              <h2>Forecast range</h2>
              <p>Low, average, and high across all history</p>
            </div>
            <PredictionRangeBar analytics={analytics} />
          </article>
        </section>
      )}
    </div>
  )
}
