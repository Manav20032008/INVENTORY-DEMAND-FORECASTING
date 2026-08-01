import api from "./api"

export const fetchAnalytics = async () => {
  const response = await api.get("/api/v1/analytics")
  return response.data
}

export const fetchHealth = async () => {
  const response = await api.get("/health")
  return response.data
}
