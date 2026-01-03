import "../css/Topbar.css";
import { HiArrowUpTray } from "react-icons/hi2";
import { useNavigate } from "react-router-dom";

const Topbar = ({ onUpload }) => {
  const navigate = useNavigate();
  const username = localStorage.getItem("user") || "User";

  const handleLogout = () => {
    localStorage.clear();
    navigate("/");
  };

  return (
    <div className="topbar">
      {/* LEFT */}
      <div className="topbar-left">
        <h2>📁 Document Dashboard</h2>
      </div>

      {/* RIGHT */}
      <div className="topbar-right">
        {/* Upload Button */}
        <button className="upload-btn" onClick={onUpload}>
          <HiArrowUpTray size={18} />
          Upload
        </button>

        {/* User Info */}
        <div className="user-info">
          <span className="avatar">{username.charAt(0).toUpperCase()}</span>
          <span className="username">{username}</span>
        </div>

        {/* Logout */}
        <button className="logout-btn" onClick={handleLogout}>
          Logout
        </button>
      </div>
    </div>
  );
};

export default Topbar;
