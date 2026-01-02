import "../css/Sidebar.css";

const Sidebar = ({ active, setActive }) => {
  return (
    <div className="sidebar">
      <div className="sidebar-logo">
        <h2>DMS</h2>
        <span>Document System</span>
      </div>

      <nav className="sidebar-menu">
        <button
          className={`sidebar-btn ${active === "all" ? "active" : ""}`}
          onClick={() => setActive("all")}
        >
          📁 <span>All Documents</span>
        </button>

        <button
          className={`sidebar-btn ${active === "mine" ? "active" : ""}`}
          onClick={() => setActive("mine")}
        >
          👤 <span>My Documents</span>
        </button>
      </nav>
    </div>
  );
};

export default Sidebar;
