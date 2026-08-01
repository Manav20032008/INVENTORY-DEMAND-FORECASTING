import AnalyticsDashboard from "../components/AnalyticsDashboard";
import LoadingSpinner from "../components/LoadingSpinner";
import ErrorAlert from "../components/ErrorAlert";
import useAnalytics from "../hooks/useAnalytics";

export default function Analytics() {
  const { analytics, predictions, loading, error, reload } = useAnalytics();

  return (
    <section className="page">
      <div className="page-header history-header">
        <div>
          <h2>Analytics Dashboard</h2>
          <p>Aggregate metrics and charts from stored prediction history.</p>
        </div>
        <button type="button" className="btn btn-secondary" onClick={reload}>
          Refresh
        </button>
      </div>

      <ErrorAlert message={error} onRetry={reload} />

      {loading ? <LoadingSpinner message="Loading analytics dashboard..." /> : null}

      {!loading && analytics ? (
        <AnalyticsDashboard analytics={analytics} predictions={predictions} />
      ) : null}
    </section>
  );
}
