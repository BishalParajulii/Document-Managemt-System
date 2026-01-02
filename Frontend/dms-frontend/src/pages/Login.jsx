import { useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../api/axios";
import "../css/Login.css";


const Login = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();
    setError("");
    setLoading(true);

    try {
      const res = await api.post("login/", {
        username,
        password,
      });

      localStorage.setItem("access", res.data.access);
      localStorage.setItem("refresh", res.data.refresh);
      localStorage.setItem("user" , res.data.username);

      navigate("/documents");
    } catch (err) {
      console.log(err)
      setError("Invalid username or password");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="login-wrapper">
      {/* LEFT */}
      <div className="login-info">
        <h1>DMS</h1>
        <p className="subtitle">Secure Document Management System</p>
      </div>

      {/* RIGHT */}
      <div className="login-form-container">
        <form className="login-form" onSubmit={handleLogin}>
          <h2>Welcome Back</h2>

          <div className="input-group">
            <input
              required
              value={username}
              onChange={(e) => setUsername(e.target.value)}
            />
            <label>Username</label>
          </div>

          <div className="input-group">
            <input
              type="password"
              required
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
            <label>Password</label>
          </div>

          {error && <p className="error">{error}</p>}

          <button disabled={loading}>
            {loading ? "Signing in..." : "Login"}
          </button>
        </form>
      </div>
    </div>
  );
};

export default Login;
