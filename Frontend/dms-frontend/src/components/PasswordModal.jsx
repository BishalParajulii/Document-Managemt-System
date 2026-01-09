// components/PasswordModal.jsx
import { useState } from "react";

const PasswordModal = ({ onClose, onVerify }) => {
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    const success = await onVerify(password);
    if (!success) {
      setError("Incorrect password, try again!");
    }
  };

  return (
    <div className="modal-backdrop">
      <div className="modal-content">
        <h3>Enter Password</h3>
        <form onSubmit={handleSubmit}>
          <input
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            autoFocus
          />
          <button type="submit">Submit</button>
          <button type="button" onClick={onClose}>Cancel</button>
        </form>
        {error && <p style={{ color: "red" }}>{error}</p>}
      </div>
    </div>
  );
};

export default PasswordModal;
