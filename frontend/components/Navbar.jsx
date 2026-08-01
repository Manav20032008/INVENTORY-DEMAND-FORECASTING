import { NavLink } from "react-router-dom";

const links = [
  { to: "/", label: "Predict", end: true },
  { to: "/history", label: "History" },
  { to: "/analytics", label: "Analytics" },
];

export default function Navbar() {
  return (
    <header className="navbar">
      <div className="navbar-inner container">
        <div className="brand">
          <span className="brand-icon">📦</span>
          <div>
            <h1>Inventory Demand</h1>
            <p>XGBoost Forecasting Platform</p>
          </div>
        </div>
        <nav className="nav-links">
          {links.map((link) => (
            <NavLink
              key={link.to}
              to={link.to}
              end={link.end}
              className={({ isActive }) => (isActive ? "nav-link active" : "nav-link")}
            >
              {link.label}
            </NavLink>
          ))}
        </nav>
      </div>
    </header>
  );
}
