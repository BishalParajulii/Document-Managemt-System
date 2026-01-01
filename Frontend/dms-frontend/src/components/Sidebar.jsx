const Sidebar = ({ active, setActive }) => {
  return (
    <div style={styles.sidebar}>
      <h2 style={styles.logo}>DMS</h2>

      <button
        style={active === "all" ? styles.activeBtn : styles.btn}
        onClick={() => setActive("all")}
      >
        📁 All Documents
      </button>

      <button
        style={active === "mine" ? styles.activeBtn : styles.btn}
        onClick={() => setActive("mine")}
      >
        👤 My Documents
      </button>

      <button style={styles.logout}>🚪 Logout</button>
    </div>
  );
};

const styles = {
  sidebar: {
    width: "220px",
    background: "#0f172a",
    color: "white",
    padding: "20px",
    display: "flex",
    flexDirection: "column",
    gap: "15px",
  },
  logo: { marginBottom: "20px" },
  btn: {
    background: "transparent",
    color: "white",
    border: "none",
    textAlign: "left",
    padding: "10px",
    cursor: "pointer",
  },
  activeBtn: {
    background: "#1e293b",
    color: "white",
    border: "none",
    padding: "10px",
    textAlign: "left",
  },
  logout: {
    marginTop: "auto",
    background: "#dc2626",
    color: "white",
    border: "none",
    padding: "10px",
    cursor: "pointer",
  },
};

export default Sidebar;
