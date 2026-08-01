import {
  Area,
  AreaChart,
  CartesianGrid,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
} from "recharts";

function formatDate(iso) {
  return new Date(iso).toLocaleDateString(undefined, {
    month: "short",
    day: "numeric",
    hour: "2-digit",
    minute: "2-digit",
  });
}

export default function PredictionsTrendChart({ predictions }) {
  if (!predictions.length) {
    return (
      <div className="chart-empty">
        <p>No prediction data yet for trend chart.</p>
      </div>
    );
  }

  const data = [...predictions]
    .sort((a, b) => new Date(a.created_at) - new Date(b.created_at))
    .map((row) => ({
      label: formatDate(row.created_at),
      prediction: Number(row.prediction.toFixed(2)),
      store: row.store,
    }));

  return (
    <ResponsiveContainer width="100%" height={280}>
      <AreaChart data={data} margin={{ top: 8, right: 8, left: 0, bottom: 0 }}>
        <defs>
          <linearGradient id="predictionGradient" x1="0" y1="0" x2="0" y2="1">
            <stop offset="5%" stopColor="#2563eb" stopOpacity={0.35} />
            <stop offset="95%" stopColor="#2563eb" stopOpacity={0} />
          </linearGradient>
        </defs>
        <CartesianGrid strokeDasharray="3 3" stroke="#e2e8f0" />
        <XAxis dataKey="label" tick={{ fontSize: 11 }} interval="preserveStartEnd" />
        <YAxis tick={{ fontSize: 11 }} width={48} />
        <Tooltip
          contentStyle={{
            borderRadius: 10,
            border: "1px solid #e2e8f0",
            boxShadow: "0 8px 24px rgba(15, 23, 42, 0.08)",
          }}
          formatter={(value) => [value, "Predicted sales"]}
        />
        <Area
          type="monotone"
          dataKey="prediction"
          stroke="#2563eb"
          strokeWidth={2}
          fill="url(#predictionGradient)"
        />
      </AreaChart>
    </ResponsiveContainer>
  );
}
