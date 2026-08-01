import { Routes, Route } from "react-router-dom";
import MainLayout from "../layouts/MainLayout";
import Home from "../pages/Home";
import History from "../pages/History";
import Analytics from "../pages/Analytics";
import NotFound from "../pages/NotFound";

export default function AppRoutes() {
  return (
    <Routes>
      <Route element={<MainLayout />}>
        <Route index element={<Home />} />
        <Route path="history" element={<History />} />
        <Route path="analytics" element={<Analytics />} />
        <Route path="*" element={<NotFound />} />
      </Route>
    </Routes>
  );
}
