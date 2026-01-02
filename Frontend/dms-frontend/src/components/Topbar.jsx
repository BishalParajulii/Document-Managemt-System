import "../css/Topbar.css";

const Topbar = () => {
  const username = localStorage.getItem("user") || "Guest";

  const handleLogout = () => {
    localStorage.clear();
    window.location.href = "/";
  };

  return (
    <div className="topbar">
      <div className="topbar-left">
        <h2>📁 Document Dashboard</h2>
      </div>

      <div className="topbar-right">
        <div className="user-info">
          <span className="avatar">
            {username.charAt(0).toUpperCase()}
          </span>
          <span className="username">{username}</span>
        </div>

        <button className="logout-btn" onClick={handleLogout}>
          Logout
        </button>
      </div>
    </div>
  );
};

export default Topbar;
