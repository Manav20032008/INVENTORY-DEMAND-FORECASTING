import { useCallback, useEffect, useState } from "react";
import { fetchAnalytics } from "../services/analyticsService";
import { fetchPredictions } from "../services/predictionService";

export default function useAnalytics() {
  const [analytics, setAnalytics] = useState(null);
  const [predictions, setPredictions] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  const loadAnalytics = useCallback(async () => {
    setLoading(true);
    setError("");
    try {
      const [analyticsData, predictionsData] = await Promise.all([
        fetchAnalytics(),
        fetchPredictions({ page: 1, limit: 100 }),
      ]);
      setAnalytics(analyticsData);
      setPredictions(Array.isArray(predictionsData) ? predictionsData : []);
    } catch (err) {
      setError(err.message);
      setAnalytics(null);
      setPredictions([]);
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    loadAnalytics();
  }, [loadAnalytics]);

  return { analytics, predictions, loading, error, reload: loadAnalytics };
}
