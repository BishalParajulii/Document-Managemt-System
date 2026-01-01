const Topbar = () => {
  const user = localStorage.getItem("user") || "User";

  return (
    <div style={styles.topbar}>
      <h3>Documents Dashboard</h3>
      <span>{user}</span>
    </div>
  );
};

const styles = {
  topbar: {
    height: "60px",
    background: "#f8fafc",
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
    padding: "0 20px",
    borderBottom: "1px solid #e5e7eb",
  },
};

export default Topbar;
