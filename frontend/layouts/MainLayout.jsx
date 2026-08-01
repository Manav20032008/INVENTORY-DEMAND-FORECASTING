import { Outlet } from "react-router-dom";
import Navbar from "../components/Navbar";

export default function MainLayout() {
  return (
    <div className="app-shell">
      <Navbar />
      <main className="container">
        <Outlet />
      </main>
      <footer className="footer">
        <p>&copy; Inventory Demand Forecasting &mdash; ML powered sales prediction for local stores</p>
      </footer>
    </div>
  );
}
